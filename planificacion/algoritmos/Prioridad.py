
def algoritmo_prioridad(lista):

  #retorna la lista de procesos ordenada en base a su llegada y prioridad
  lista.sort(key=lambda p: (p.llegada, -p.prioridad))


  return lista, 3