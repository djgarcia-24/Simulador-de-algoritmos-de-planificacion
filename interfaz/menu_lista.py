from planificacion.proceso import Proceso

def seleccion_lista():
    while True:
        print("\n"+"="*55+"\n   MENÚ DE INICIO\n"+"="*55)
        print(" 1) Procesos precargados A\n 2) Procesos precargados B\n 3) Crear procesos\n 4) Cargar procesos\n 5) Salir\n")
        match input("Ingresa una opción (1-5): "):
            case "1":
                lista = [Proceso("1", 0, 8, 3),Proceso("2", 1, 4, 1),Proceso("4", 3, 5, 2) ,Proceso("3", 2, 9, 4)]
                return lista 
            
            case "2":
                print("\n[+] Cargando Lista B...")
            case "3":
                print("\n[+] Creando procesos...")
            case "4":
                print("\n[+] Cargando procesos...")
            case "5":
                break
            case _:
                print("\n[!] Opción inválida.")