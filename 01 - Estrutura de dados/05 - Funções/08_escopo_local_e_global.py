def salario_bonus(bonus):
    global salario
    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"Lista auxiliar = {lista_aux}")
    salario += bonus
    return salario

lista = [1]
salario = 2000

print(f"Lista = {lista}")
print(f"Salário = {salario}")

salario_com_bonus = salario_bonus(500) 
print(f"Salário bônus = {salario_com_bonus}")
