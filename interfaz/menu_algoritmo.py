from planificacion.algoritmos.fcfs import algoritmo_fcfs 

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
        
        match opcion_alg:
            case "1":
                return algoritmo_fcfs(lista)
                break
            case "2":
                break
            case "3":
                break
            case "4":

                quantum = input("\n[?] Ingresa el valor del Quantum para Round Robin: ")
                if quantum.isdigit():
                    quantum = int(quantum)
                    
                    break
                else:
                    print("\n[!] Error: El Quantum debe ser un número entero válido.")
            case "5":
                print("\nCancelando... Volviendo al menú principal.")
                break
            case _:
                print("\n[!] Opción inválida. Por favor, ingresa un número del 1 al 5.")