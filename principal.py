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

#si el algoritmo escogido es RR este devolvera una tupla, que se desempacara en la lista ordenada y el quantum
#de no ser asi solo se devolvera una lista ordenada segun el algoritmo de planificacion
if isinstance( planificacion , tuple):
    lista,quantum = planificacion
    scheduler(lista, 1, quantum)
else:
    lista =planificacion
    scheduler(lista, 0, 0)

