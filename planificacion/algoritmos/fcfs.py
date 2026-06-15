def algoritmo_fcfs(lista):
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
