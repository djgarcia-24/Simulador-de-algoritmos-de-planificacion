from planificacion.algoritmos.First_come_first_served import algoritmo_fcfs 
from planificacion.algoritmos.Round_robin import algoritmo_round_robin 
from planificacion.algoritmos.Shortest_job_first import algoritmo_sjf 

def seleccion_algoritmo_planificacion(lista):
    while True:
        print("\n" + "-" * 55)
        print("   SELECCIÓN DE ALGORITMO DE PLANIFICACIÓN")
        print("-" * 55)
        print("  1) FCFS")
        print("  2) SJF")
        print("  3) Prioridad")
        print("  4) RR")
        print("  5) Cancelar y volver al menú principal")
        print("-" * 55)
        
        opcion_alg = input("Elige el algoritmo a ejecutar (1-5): ")
        #distintas opciones de algoritmos
        match opcion_alg:
            case "1":
                return algoritmo_fcfs(lista)
            case "2":
                return algoritmo_sjf(lista)                
            case "3":
                return 
                break
            case "4":
                quantum = input("Ingresa el valor del Quantum para Round Robin: ")
                if quantum.isdigit():
                    quantum = int(quantum)

                    lista_ordenada_RR, tipo = algoritmo_round_robin(lista)

                    return lista_ordenada_RR, tipo, quantum
                else:
                    print("\n[!] Error: El Quantum debe ser un número entero válido.")
            case "5":
                print("\nCancelando... Volviendo al menú principal.")
                break
            case _:
                print("\n[!] Opción inválida. Por favor, ingresa un número del 1 al 5.")