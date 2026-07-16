
def algoritmo_sjf(lista):

  #retorna la lista de procesos ordenada en base a su llegada
  lista.sort(key=lambda p: (p.llegada, p.rafaga))


  return lista, 2