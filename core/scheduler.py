from planificacion.algoritmo import Algoritmo




def ordenar_lista(lista):
  #retorna la lista de procesos ordenada en base a su tiempo de llegada, de menor a mayor
  n= len(lista)
  for i in range(n):
    swap = False
    for j in range(0, n - i - 1):
      if lista[j].llegada > lista[j + 1].llegada:
        lista[j], lista[j + 1] = lista[j + 1], lista[j]
        swap = True

    if not swap:
      break
  return lista


def imprimir_lista(lista):
    lista= ordenar_lista(lista)

    for proceso in lista:
       print( f"ID: {proceso.id} | Llegada: {proceso.llegada} | Ráfaga: {proceso.rafaga} | Prioridad: {proceso.prioridad} | Inicio: {proceso.inicio} | Fin: {proceso.fin} | Retorno: {proceso.Tretorno} | Espera: {proceso.Tespera}")





#calculo de idle_time, TER y TRP 
def desempeno_algoritmo(lista, tipo, quantum ):

    #primero haremos el calculo del idle 
    #el idle de RR es un caso especial asi que lo manejamos aparte
    if(tipo ==4):
        #si el burst time no es divisible por el quantum,      q- el restante , sera el tiempo idle


        idle = 0
        for p in lista:
            restante = p.rafaga % quantum
            if restante != 0:
                idle += (quantum - restante)    

    else:    
        #aqui manejaremos los idles de fcfs, sjf y prioridad
        #ordenamos la lista cronologicamente segun los inicios 
        lista_temporal = sorted(lista, key=lambda p: p.inicio)

        idle = 0
        t = 0  # Empezamos en el tiempo 0 y tiempo idle 0

        for p in lista_temporal:
            #si un proceso inicia despues de que termina el otro (si su tiempo inicio es mayor a su tiempo fin)
            if p.inicio > t:

                #se guarda la diferencia entre fin de uno e inicio del otro
                espacio_idle = p.inicio - t
                #y se suma al tiempo idle total
                idle += espacio_idle

            #ahora tiempo pasa a ser el tiempo fin del proceso que acabamos de evaluar, en base a este nuevo tiempo fin calcularemos la diferencia con el siguiente
            # y asi sucesivamente hasta tener un total de todos los procesos 
            t = p.fin

    #ahora el calculo de los tiempos promedios
    Tiempo_de_espera_promedio =0
    Tiempo_de_respuesta_promedio =0

    for proceso in lista:
        Tiempo_de_espera_promedio= proceso.Tespera +Tiempo_de_espera_promedio
        Tiempo_de_respuesta_promedio = proceso.Tretorno +Tiempo_de_respuesta_promedio

    Tiempo_de_espera_promedio = Tiempo_de_espera_promedio/ len(lista)
    Tiempo_de_respuesta_promedio = Tiempo_de_respuesta_promedio / len(lista)

    datos_algoritmo = Algoritmo(idle, Tiempo_de_espera_promedio, Tiempo_de_respuesta_promedio)

    return datos_algoritmo


    







def scheduler( lista, tipo, quantum): 
    #procesamiento de lista ordenada como FCFS
    if(tipo ==1):
        for  index, proceso in enumerate(lista):
            if(index ==0 ):
                #primer proceso
                proceso.inicio = proceso.llegada
                proceso.fin= proceso.llegada+proceso.rafaga
                proceso.Tretorno= proceso.fin -proceso.llegada
                proceso.Tespera= proceso.inicio -proceso.llegada
            elif(proceso.llegada <= lista[index -1].fin):
                #llega antes de que termine el proceso anterior 
                proceso.inicio = lista[index -1].fin
                proceso.fin= proceso.inicio+proceso.rafaga
                proceso.Tretorno= proceso.fin -proceso.llegada
                proceso.Tespera= proceso.inicio -proceso.llegada            
            elif(proceso.llegada > lista[index -1].fin):
                #llega despues de que haya terminado el proceso anterior ( hay idle time)
                proceso.inicio = lista[index -1].fin+  abs( lista[index-1].fin-proceso.llegada )
                proceso.fin= proceso.inicio+proceso.rafaga
                proceso.Tretorno= proceso.fin -proceso.llegada
                proceso.Tespera= proceso.inicio -proceso.llegada

    elif (tipo ==2):     #procesamiento de lista con SJF

        t = 0
        pendientes = lista.copy() # pendientes sera igual a la lista original
        terminados = []      


        #mientras existan pendientes el loop sigue
        while pendientes:
            # candidatos es igual a todos los procesos con llegada menor o igual a t
            candidatos = [p for p in pendientes if p.llegada <= t]
            
            if candidatos:

                candidatos.sort(key=lambda p: (p.rafaga, p.llegada))

                #el primero de la lista que ya ordenamos en base a llegada y rafaga es el primer candidato
                actual = candidatos[0]
 
 
                actual.inicio = t
                actual.fin = actual.inicio + actual.rafaga
                actual.Tretorno = actual.fin - actual.llegada
                actual.Tespera = actual.inicio - actual.llegada


                t = t+ actual.rafaga
                
                pendientes.remove(actual)
                terminados.append(actual) 
            else:
                # Si no hay candidatos, significa que en tiempo t no ha llegado nadie 
                #adelantaremos t a la proxima llegada
                t = pendientes[0].llegada
                
        # al final del while terminados tendra todos los procesos listos 
        lista = terminados

    elif(tipo == 3):

        t = 0
        pendientes = lista.copy() # pendientes sera igual a la lista original
        terminados = []      

        #mientras existan pendientes el loop sigue
        while pendientes:
            # candidatos es igual a todos los procesos con llegada menor o igual a t


            candidatos = [p for p in pendientes if p.llegada <= t]
            
            if candidatos:

                #ordenando por -prioridad permite que las mayorores prioridades queden primero 
                candidatos.sort(key=lambda p: (-p.prioridad, p.llegada))

                #el primero de la lista que ya ordenamos en base a llegada y prioridad es el primer candidato
                actual = candidatos[0]
 
                actual.inicio = t
                actual.fin = actual.inicio + actual.rafaga
                actual.Tretorno = actual.fin - actual.llegada
                actual.Tespera = actual.inicio - actual.llegada

                t = t+ actual.rafaga

                pendientes.remove(actual)
                terminados.append(actual) 
            else:
                # Si no hay candidatos, significa que en tiempo t no ha llegado nadie 
                #adelantaremos t a la proxima llegada
                t = min(p.llegada for p in pendientes)
                
        # al final del while terminados tendra todos los procesos listos 
        lista = terminados

    #procesamiento de lista con algoritmo RR
    elif(tipo  == 4):


        round=1
        terminado = False        
        
        tiempo_total=0
        #si la variable terminado es verdadera para todos los procesos, al terminar el ultimo ciclo for el ciclo while dejara de cumplirse, terminando con todos los calculos
        while(  not terminado  ):        
            terminado = True
        
            for index, proceso in enumerate(lista):
                #evaluamos si el proceso tiene tiempo restante diferente de 0, si es asi, ya lo habiamos procesado y se ignora, si no se evalua   
                if(proceso.Trestante ==0):
                    terminado = terminado and True 
                else:
                    terminado = terminado and False
                    if( round == 1 and index == 0 ):
                        proceso.inicio = proceso.llegada
                    elif(round == 1):
                        proceso.inicio = index*quantum
                        
                    if(proceso.Trestante <=quantum):
                        #proceso.fin = (round-1)*quantum+proceso.Trestante+tiempo_total
                        
                        proceso.fin = ((tiempo_total))+proceso.Trestante
                        proceso.Tretorno= abs(  proceso.fin -proceso.llegada)
                        proceso.Tespera= abs(proceso.inicio -proceso.llegada  )
                        proceso.Trestante =0 
                        
                    else:
                        proceso.Trestante = proceso.Trestante -quantum 
                                        
                    tiempo_total = (quantum)+tiempo_total

            round =round+1



    imprimir_lista(lista)

    datos_alg = desempeno_algoritmo(lista, tipo, quantum)






    print(     "\nIdle : "+  str(datos_alg.idle  )  
          +"\nTER: "+   str(datos_alg.Tiempo_de_espera_promedio  ) 
          + "\nTRP: "  +str(datos_alg.Tiempo_de_respuesta_promedio ))