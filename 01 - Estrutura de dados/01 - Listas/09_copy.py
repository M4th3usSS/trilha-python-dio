lista = [1, "Python", [40, 30, 20]]

l2 = lista.copy()

print(lista)  # [1, "Python", [40, 30, 20]]

print(id(lista), id(l2))

l2[0] = 2

print(lista)
print(l2)