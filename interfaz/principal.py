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

lista = seleccion_lista()
lista = seleccion_algoritmo_planificacion(lista)
scheduler(lista, 0)