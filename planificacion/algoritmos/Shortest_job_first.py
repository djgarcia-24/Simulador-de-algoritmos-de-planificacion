def algoritmo_sjf(lista):
  #retorna la lista de procesos ordenada en base a su tiempo de rafaga, de menor a mayor
  n= len(lista)
  for i in range(n):
    swap = False
    for j in range(0, n - i - 1):
      if lista[j].rafaga > lista[j + 1].rafaga:
        lista[j], lista[j + 1] = lista[j + 1], lista[j]
        swap = True

    if not swap:
      break
  return lista
