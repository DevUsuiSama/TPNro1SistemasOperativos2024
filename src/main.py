#
# Created on Tue Sep 03 2024
#
# Copyright (c) 2024 UsuiSama
#

import random
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox

# Explicación
# 1. Definición de Clases:
#   * Proceso: Representa un proceso con un ID, memoria requerida y estado.
#   * Simulador: Gestiona la memoria y los procesos, incluyendo la cola de listos y bloqueados.
# 2. Lógica de Simulación:
#   * agregar_proceso: Añade un proceso a la cola de listos si hay suficiente memoria, de lo contrario, lo añade a la cola de bloqueados.
#   * liberar_memoria: Libera la memoria ocupada por un proceso.
#   * ejecutar_proceso: Ejecuta el siguiente proceso en la cola de listos.
#   * finalizar_proceso: Finaliza el proceso en ejecución y libera su memoria.
#   * actualizar_procesos: Actualiza el estado de los procesos, moviendo procesos de la cola de bloqueados a la de listos si hay suficiente memoria.
# 3. Interfaz Gráfica:
#   * InterfazSimulador: Crea la interfaz gráfica usando Tkinter, mostrando el estado de los procesos y la memoria disponible en tiempo real.

# Explicación (Nuevo - 1)
# 1. Modificación en Simulador:
#   * En el método agregar_proceso, ahora se agrega el proceso a la lista self.procesos para que esté disponible para la interfaz.
# 2. Actualización en InterfazSimulador:
#   * En el método agregar_proceso, se llama a self.actualizar_interfaz() después de agregar un proceso para asegurarse de que la interfaz se actualice inmediatamente.

# Explicación (Nuevo - 2)
# 1. Método finalizar_proceso_aleatorio en Simulador:
#   * Selecciona un proceso aleatorio de la cola de listos.
#   * Libera la memoria del proceso y cambia su estado a ‘Terminado’.
#   * Muestra un mensaje de diálogo indicando que el proceso ha finalizado.
# 2. Interfaz Gráfica:
#   * Añade un botón para finalizar procesos aleatoriamente.
#   * Actualiza la interfaz después de finalizar un proceso aleatorio.

# -- ESTRUCTURA DE LOS PROCESO Y MEMORIA --

class Proceso:
    def __init__(self, id, memoria_requerida):
        self.id = id
        self.memoria_requerida = memoria_requerida
        self.estado = 'Listo'

class Simulador:
    def __init__(self, memoria_total):
        self.memoria_total = memoria_total
        self.memoria_disponible = memoria_total
        self.procesos = []
        self.cola_listos = []
        self.cola_bloqueados = []
        self.proceso_ejecutando = None

    def agregar_proceso(self, proceso):
        self.procesos.append(proceso)
        if proceso.memoria_requerida <= self.memoria_disponible:
            self.cola_listos.append(proceso)
            self.memoria_disponible -= proceso.memoria_requerida
        else:
            self.cola_bloqueados.append(proceso)

    def liberar_memoria(self, proceso):
        self.memoria_disponible += proceso.memoria_requerida

    def ejecutar_proceso(self):
        if self.cola_listos:
            self.proceso_ejecutando = self.cola_listos.pop(0)
            self.proceso_ejecutando.estado = 'Ejecutando'

    def finalizar_proceso(self):
        if self.proceso_ejecutando:
            self.liberar_memoria(self.proceso_ejecutando)
            self.proceso_ejecutando.estado = 'Terminado'
            messagebox.showinfo("Proceso Finalizado", f"El proceso {self.proceso_ejecutando.id} ha finalizado.")
            self.proceso_ejecutando = None

    def finalizar_proceso_aleatorio(self):
        if self.cola_listos:
            proceso_a_finalizar = random.choice(self.cola_listos)
            self.cola_listos.remove(proceso_a_finalizar)
            self.liberar_memoria(proceso_a_finalizar)
            proceso_a_finalizar.estado = 'Terminado'
            messagebox.showinfo("Proceso Finalizado", f"El proceso {proceso_a_finalizar.id} ha finalizado.")
            self.actualizar_procesos()

    def actualizar_procesos(self):
        if self.proceso_ejecutando:
            self.finalizar_proceso()
        self.ejecutar_proceso()
        for proceso in self.cola_bloqueados:
            if proceso.memoria_requerida <= self.memoria_disponible:
                self.cola_bloqueados.remove(proceso)
                self.cola_listos.append(proceso)
                self.memoria_disponible -= proceso.memoria_requerida

# -- INTERFAZ GRÁFICA DE USUARIO --

class InterfazSimulador:
    def __init__(self, root, simulador):
        self.simulador = simulador
        self.root = root
        self.root.title("Simulador de Gestión de Procesos")
        
        self.label_memoria = tk.Label(root, text=f"Memoria Disponible: {self.simulador.memoria_disponible}")
        self.label_memoria.pack()

        self.tree = ttk.Treeview(root, columns=("ID", "Memoria", "Estado"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Memoria", text="Memoria")
        self.tree.heading("Estado", text="Estado")
        self.tree.pack()

        self.boton_agregar = tk.Button(root, text="Agregar Proceso", command=self.agregar_proceso)
        self.boton_agregar.pack()

        self.boton_finalizar = tk.Button(root, text="Finalizar Proceso Aleatorio", command=self.finalizar_proceso_aleatorio)
        self.boton_finalizar.pack()

        self.actualizar_interfaz()

    def agregar_proceso(self):
        id_proceso = len(self.simulador.procesos) + 1
        memoria_requerida = random.randint(1, 100)
        proceso = Proceso(id_proceso, memoria_requerida)
        self.simulador.agregar_proceso(proceso)
        self.actualizar_interfaz()

    def finalizar_proceso_aleatorio(self):
        self.simulador.finalizar_proceso_aleatorio()
        self.actualizar_interfaz()

    def actualizar_interfaz(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for proceso in self.simulador.procesos:
            self.tree.insert("", "end", values=(proceso.id, proceso.memoria_requerida, proceso.estado))
        self.label_memoria.config(text=f"Memoria Disponible: {self.simulador.memoria_disponible}")
        self.root.after(1000, self.actualizar_interfaz)

if __name__ == "__main__":
    memoria_total = 500
    simulador = Simulador(memoria_total)
    root = tk.Tk()
    interfaz = InterfazSimulador(root, simulador)
    root.mainloop()

