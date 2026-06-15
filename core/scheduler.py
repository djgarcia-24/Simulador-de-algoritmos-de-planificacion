def scheduler( lista, bool_RR): 
    
    #basado en como te entreguen la lista (el algoritmo), ya va a estar ordenado
    #te va a llegar la lista ordenada por el algoritmo 
    #despues al imprimir resultados se ordenada por orden de llegada

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


    for proceso in lista:
        print( f"ID: {proceso.id} | Llegada: {proceso.llegada} | Ráfaga: {proceso.rafaga} | Prioridad: {proceso.prioridad} | Inicio: {proceso.inicio} | Fin: {proceso.fin} | Retorno: {proceso.Tretorno} | Espera: {proceso.Tespera}")



