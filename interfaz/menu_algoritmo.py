from planificacion.algoritmos.First_come_first_served import algoritmo_fcfs 
from planificacion.algoritmos.Round_robin import algoritmo_round_robin 
from planificacion.algoritmos.Shortest_job_first import algoritmo_sjf 
from planificacion.algoritmos.Prioridad import algoritmo_prioridad 
import sys


def seleccion_algoritmo_planificacion(lista):
    while True:
        print("\n" + "-" * 55)
        print("   SELECCIÓN DE ALGORITMO DE PLANIFICACIÓN")
        print("-" * 55)
        print("  1) FCFS")
        print("  2) SJF")
        print("  3) Prioridad")
        print("  4) RR")
        print("  5) Salir y cerrar")

        print("  \nEn caso de querer comparar dos algoritmos escribir sus dos identificadores de manera contigua en cualquier orden  \nEjemplo: 12 o 21 para fcfs y sjf")

    
        print("-" * 55)
        
        opcion_alg = input("Elige el algoritmo a ejecutar (1-5): ")

        #distintas opciones de algoritmos
        match opcion_alg:
            case "1":
                return algoritmo_fcfs(lista)
            case "2":
                return algoritmo_sjf(lista)                
            case "3":
                return algoritmo_prioridad(lista)
            case "4":
                quantum = input("Ingresa el valor del Quantum para Round Robin: ")
                if quantum.isdigit():
                    quantum = int(quantum)

                    lista_ordenada_RR, tipo = algoritmo_round_robin(lista)

                    return lista_ordenada_RR, tipo, quantum
                else:
                    print("\n[!] Error: El Quantum debe ser un número entero válido.")



            # --- Comparaciones dobles ---
            
            # 12 o 21: FCFS + SJF
            case "12" | "21":
                lista1, tipo1 = algoritmo_fcfs(lista)
                lista2, tipo2 = algoritmo_sjf(lista)
                return lista1, tipo1, lista2, tipo2

            # 13 o 31: FCFS + Prioridad
            case "13" | "31":
                lista1, tipo1 = algoritmo_fcfs(lista)
                lista2, tipo2 = algoritmo_prioridad(lista)
                return lista1, tipo1, lista2, tipo2

            # 14 o 41: FCFS + RR
            case "14" | "41":
                quantum = input("Ingresa el valor del Quantum para Round Robin: ")
                if quantum.isdigit():
                    quantum = int(quantum)
                    lista1, tipo1 = algoritmo_fcfs(lista)
                    lista2, tipo2 = algoritmo_round_robin(lista)
                    return lista1, tipo1, lista2, tipo2, quantum
                else:
                    print("\n[!] Error: El Quantum debe ser un número entero válido.")

            # 23 o 32: SJF + Prioridad
            case "23" | "32":
                lista1, tipo1 = algoritmo_sjf(lista)
                lista2, tipo2 = algoritmo_prioridad(lista)
                return lista1, tipo1, lista2, tipo2

            # 24 o 42: SJF + RR
            case "24" | "42":
                quantum = input("Ingresa el valor del Quantum para Round Robin: ")
                if quantum.isdigit():
                    quantum = int(quantum)
                    lista1, tipo1 = algoritmo_sjf(lista)
                    lista2, tipo2 = algoritmo_round_robin(lista)
                    return lista1, tipo1, lista2, tipo2, quantum
                else:
                    print("\n[!] Error: El Quantum debe ser un número entero válido.")

            # 34 o 43: Prioridad + RR
            case "34" | "43":
                quantum = input("Ingresa el valor del Quantum para Round Robin: ")
                if quantum.isdigit():
                    quantum = int(quantum)
                    lista1, tipo1 = algoritmo_prioridad(lista)
                    lista2, tipo2 = algoritmo_round_robin(lista)
                    return lista1, tipo1, lista2, tipo2, quantum
                else:
                    print("\n[!] Error: El Quantum debe ser un número entero válido.")  
            
            
            case "5":
                print("\nSaliendo.")
                sys.exit()  # Stops the program immediately

                break
            case _:
                print("\n[!] Opción inválida. Por favor, ingresa un número del 1 al 5.")