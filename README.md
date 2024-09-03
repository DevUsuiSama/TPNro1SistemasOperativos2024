# Sistemas Operativos (Simulación)

- Asignatura: Sistemas Operativos
- Carrera: Ingeniería en Sistemas de Información
- Profesor: Ing. Juan de Dios Benitez y Lic. Ana Itati Malañuk

## Descripción

El único propósito de este proyecto es la de investigar y experimentar sobre la gestión de proceso y asignación de memoria.

## Tipos de Algoritmos Utilizado

### Algoritmo de Gestión de Memoria:
* First Fit: Este algoritmo asigna la memoria al primer bloque disponible que sea lo suficientemente grande para el proceso. En nuestro caso, cuando un proceso solicita memoria, se verifica si hay suficiente memoria disponible y se asigna directamente si es posible.
Algoritmo de Planificación de Procesos:
* Round Robin (simplificado): Aunque no implementamos un temporizador explícito, la idea es que los procesos se ejecutan en un orden cíclico. Si hay más de un proceso en la cola de listos, se ejecutan uno tras otro.

## Tipo de Memoria Utilizado

### Memoria Principal (RAM):
* Simulamos la memoria principal con una cantidad fija de memoria total (memoria_total) y una cantidad de memoria disponible (memoria_disponible). Los procesos solicitan y liberan memoria de esta memoria principal.

## Detalles del Simulador
### Colas de Procesos:
* Cola de Listos: Contiene los procesos que están listos para ejecutarse.
* Cola de Bloqueados: Contiene los procesos que están esperando a que se libere memoria.
## Estados de los Procesos:
* Listo: El proceso está listo para ejecutarse.
* Ejecutando: El proceso está actualmente en ejecución.
* Bloqueado: El proceso está esperando a que se libere memoria.
* Terminado: El proceso ha finalizado su ejecución.

## Investigador

- Usui, José Fernando 👈(ﾟヮﾟ👈)