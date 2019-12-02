def list_reverse(lst):
  items = len(lst) -1
  newList = []
  while items >= 0:
    newList.append(lst[items])
    items -= 1
  print(newList)

list_reverse([1, 2, 3, 4])
