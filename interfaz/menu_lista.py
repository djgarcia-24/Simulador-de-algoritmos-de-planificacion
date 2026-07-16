from planificacion.proceso import Proceso

def seleccion_lista():
    while True:
        #distintas opciones de lista
        print("\n"+"="*55+"\n   MENÚ DE INICIO\n"+"="*55)
        print(" 1) Procesos precargados A\n 2) Procesos precargados B\n 3) Crear procesos\n 4) Cargar procesos\n 5) Salir\n")
        match input("Ingresa una opción (1-5): "):
            case "1":
                lista = [Proceso("1", 0, 8, 3),Proceso("2", 1, 4, 1),Proceso("4", 3, 5, 2) ,Proceso("3", 2, 9, 4)]
                return lista             
            case "2":
                lista = [Proceso("1", 0, 10, 2),Proceso("2", 2, 3, 1),Proceso("3", 4, 6, 3) ,Proceso("4", 6, 1, 1), Proceso("5", 8, 4, 2)]
                return lista
            case "3":
                print("\n[+] Creando procesos...")
            case "4":
                print("\n[+] Cargando procesos...")
            case "5":
                break
            case _:
                print("\n[!] Opción inválida.")