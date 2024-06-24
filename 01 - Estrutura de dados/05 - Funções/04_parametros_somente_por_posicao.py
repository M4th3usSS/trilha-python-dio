# / --> os argumentos anteriores devem ser passados obrigatoriamento por posicionamento!

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


# criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido
criar_carro("Palio", 1999, "ABC-1234", "Fiat", "1.0", "Gasolina")

