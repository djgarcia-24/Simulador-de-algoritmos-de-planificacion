import sys
from pathlib import Path

#evita que se creen nuevas carpetas al correr el programa
sys.dont_write_bytecode = True
 
#se guarda la ruta actual proyecto para poder hacer los imports
ruta_padre = str(Path(__file__).resolve().parent.parent)
sys.path.insert(0, ruta_padre)

#imports
from core.scheduler import scheduler

from core.scheduler import imprimir_detalles_algoritmo



from interfaz.menu_algoritmo import seleccion_algoritmo_planificacion
from interfaz.menu_lista import seleccion_lista

#se selecciona la lista 
lista = seleccion_lista()

    


#la lista es organizada segun el algoritmo de planificacion escogido y se le asigna a la variable planificacion
planificacion = seleccion_algoritmo_planificacion(lista)

# la variable tipo de algoritmo tendra 4 posibles codigos indentificando a cada algoritmo
# 1 fcfs, 2 sjf, 3 prioridad, 4 RR,



#caso fcfs, sjf y prio  donde la tupla sera de 2 
if(len(planificacion)==2 ):
    lista, tipo_de_algoritmo = planificacion  
    #devolvera los detalles de la ejecucion
    d= scheduler(lista, tipo_de_algoritmo, 0)

    #imprimimos los detalles
    imprimir_detalles_algoritmo(d)



    #en caso de ser RR se retornaran 3 cosas en una tupla
elif ( len(planificacion) == 3):
    lista, tipo_de_algoritmo, quantum = planificacion
    #devolvera los detalles de la ejecucion
    d = scheduler(lista, tipo_de_algoritmo, quantum)

    #imprimimos los detalles
    imprimir_detalles_algoritmo(d)


    # en caso de ser doble algoritmo de combinacion   fcfs, sjf, prioridad se retornaran 4 cosas
elif(len(planificacion) == 4):
    lista1, tipo1, lista2, tipo2  = planificacion


    #devolvera los detalles de la ejecucion 1
    d1=scheduler(lista1, tipo1, 0)
    #imprimimos los detalles
    imprimir_detalles_algoritmo(d1)
    #devolvera los detalles de la ejecucion 2
    d2 = scheduler(lista2, tipo2, 0)
    #imprimimos los detalles
    imprimir_detalles_algoritmo(d2)


    tep1, trp1 = d1.Tiempo_de_espera_promedio, d1.Tiempo_de_respuesta_promedio
    tep2, trp2 = d2.Tiempo_de_espera_promedio, d2.Tiempo_de_respuesta_promedio  

    #si d1 tiene menores tiempos promedios, gana
    if tep1 < tep2 and trp1 < trp2:
        print(f"{d1.tipo_de_algoritmo} es el mejor.")

    #si d2 tiene menores tiempos promedios, gana
    elif tep2 < tep1 and trp2 < trp1:
        print(f"{d2.tipo_de_algoritmo} es el mejor.")

    #si entre d1 y d2 no hay claro ganador se declara empate
    else:
        print("Algoritmo ganador inconcluso: No hay un claro vencedor.")
    
elif(len(planificacion) == 5):
    #en caso de que RR se combine con algun otro algoritmo se retornan 5 cosas en la tupla 

    lista1, tipo1, lista2, tipo2, quantum  = planificacion
    
    #devolvera los detalles de la ejecucion 1
    d1 = scheduler(lista1, tipo1, quantum)
    #imprimimos los detalles
    imprimir_detalles_algoritmo(d1)
    
    #devolvera los detalles de la ejecucion 2
    d2 = scheduler(lista2, tipo2, quantum)

    #imprimimos los detalles
    imprimir_detalles_algoritmo(d2)

    tep1, trp1 = d1.Tiempo_de_espera_promedio, d1.Tiempo_de_respuesta_promedio
    tep2, trp2 = d2.Tiempo_de_espera_promedio, d2.Tiempo_de_respuesta_promedio  

    #si d1 tiene menores tiempos promedios, gana
    if tep1 < tep2 and trp1 < trp2:
        print(f"{d1.tipo_de_algoritmo} es el mejor.")

    #si d2 tiene menores tiempos promedios, gana
    elif tep2 < tep1 and trp2 < trp1:
        print(f"{d2.tipo_de_algoritmo} es el mejor.")

    #si entre d1 y d2 no hay claro ganador se declara empate
    else:
        print("Algoritmo ganador inconcluso: No hay un claro vencedor.")



    



    

    
