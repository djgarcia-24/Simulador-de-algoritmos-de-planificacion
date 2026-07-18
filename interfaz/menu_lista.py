from planificacion.proceso import Proceso
import sys

def seleccion_lista():
    while True:

        print("\n"+"="*55+"\n   MENÚ DE INICIO\n"+"="*55+"\nEjemplo de Proceso: P( id, llegada, burst, prioridad)\n")

  
        print("""1) Procesos precargados A: P('1', 0, 8, 3), P('2', 1, 4, 1), P('4', 3, 5, 2), P('3', 2, 9, 4)
2) Procesos precargados B: P('1', 0, 10, 2), P('2', 2, 3, 1), P('3', 4, 6, 3), P('4', 6, 1, 1), P('5', 8, 4, 2)  
3) Procesos precargados C: P('1', 1, 6, 3), P('2', 2, 2, 1), P('3', 3, 1, 4), P('4', 4, 4, 2), P('5', 16, 2, 1)
4) Crear procesos
5) Cargar procesos
6) Salir""")
       
       
        match input("Ingresa una opción (1-6): "):
            case "1":
                lista = [Proceso("1", 0, 8, 3),Proceso("2", 1, 4, 1),Proceso("4", 3, 5, 2) ,Proceso("3", 2, 9, 4)]
                return lista             
            case "2":
                lista = [Proceso("1", 0, 10, 2),Proceso("2", 2, 3, 1),Proceso("3", 4, 6, 3) ,Proceso("4", 6, 1, 1), Proceso("5", 8, 4, 2)]
                return lista
            case "3":
                lista = [Proceso("1", 1, 6, 3),   Proceso("2", 2, 2, 1), Proceso("3", 3, 1, 4), Proceso("4", 4, 4, 2),  Proceso("5", 16, 2, 1)]
                return lista
            case "4":
                print("\n[+] Creando procesos...")
            case "5":
                print("\n[+] Cargando procesos...")
                break
            case "6":
                sys.exit()  # Stops the program immediately

                break
            case _:
                print("\n[!] Opción inválida.")