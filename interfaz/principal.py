import sys
import os

#evita que se creen nuevas carpetas al correr el programa
sys.dont_write_bytecode = True
 
#se guarda la ruta del proyecto para poder hacer los imports
ruta_actual = os.path.dirname(os.path.abspath(__file__))
ruta_padre = os.path.dirname(ruta_actual)
sys.path.append(ruta_padre)

#imports
from core.scheduler import scheduler
from menu_algoritmo import seleccion_algoritmo_planificacion
from menu_lista import seleccion_lista

#se selecciona la lista 
lista = seleccion_lista()
#la lista es organizada segun el algorimto de planificacion escogido y se le asigna a la variable planificacion
planificacion = seleccion_algoritmo_planificacion(lista)

#si algoritmo escogido es RR este devolvera una tupla, que se desempacara en la lista ordenada y el quantum
if isinstance( planificacion , tuple):
    lista,quantum = planificacion
    scheduler(lista, 1, quantum)
else:
    lista =planificacion
    scheduler(lista, 0, 0)

