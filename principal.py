import sys
from pathlib import Path

#evita que se creen nuevas carpetas al correr el programa
sys.dont_write_bytecode = True
 
#se guarda la ruta actual proyecto para poder hacer los imports
ruta_padre = str(Path(__file__).resolve().parent.parent)
sys.path.insert(0, ruta_padre)

#imports
from core.scheduler import scheduler
from interfaz.menu_algoritmo import seleccion_algoritmo_planificacion
from interfaz.menu_lista import seleccion_lista

#se selecciona la lista 
lista = seleccion_lista()


#la lista es organizada segun el algoritmo de planificacion escogido y se le asigna a la variable planificacion
planificacion = seleccion_algoritmo_planificacion(lista)

# la variable tipo de algoritmo tendra 4 posibles codigos indentificando a cada algoritmo
# 1 fcfs, 2 sjf, 3 prioridad, 4 RR,


if(len(planificacion)==2 ):
    lista, tipo_de_algoritmo = planificacion  
    scheduler(lista, tipo_de_algoritmo, 0)

elif ( len(planificacion) == 3):
    lista, tipo_de_algoritmo, quantum = planificacion
    scheduler(lista, tipo_de_algoritmo, quantum)
    
