
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
                # Si hay candidatos, aplicamos SJF: ordenamos por la ráfaga más corta.
                # En caso de empate en ráfaga, desempatamos por el que llegó primero.
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
                        proceso.Tretorno= proceso.fin -proceso.llegada
                        proceso.Tespera= proceso.inicio -proceso.llegada
                        proceso.Trestante =0 
                        
                    else:
                        proceso.Trestante = proceso.Trestante -quantum 
                                        
                    tiempo_total = (quantum)+tiempo_total

            round =round+1       



    lista= ordenar_lista(lista)

    for proceso in lista:
       print( f"ID: {proceso.id} | Llegada: {proceso.llegada} | Ráfaga: {proceso.rafaga} | Prioridad: {proceso.prioridad} | Inicio: {proceso.inicio} | Fin: {proceso.fin} | Retorno: {proceso.Tretorno} | Espera: {proceso.Tespera}")



   