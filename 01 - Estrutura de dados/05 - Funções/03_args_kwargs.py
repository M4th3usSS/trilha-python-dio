# nargs -> argumentos passados por posicionamento
# *args -> demais parâmetros passados por posicionamento e separados por vírgula (tuplas)
# **kwargs -> parâmetros passados por nome (arg=value)

#                pos_arg       *args  **Kwargs
def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)


exibir_poema(
    "Sex-feira, 26 de Agosto de 2022", # primeiro argumento de posição (data_extenso)

    "Zen of Python", # args[0]
    "Beautiful is better than ugly.", # args[1]
    "Explicit is better than implicit.", # args[2]
    "Simple is better than complex.", # args[3]
    "Complex is better than complicated.", # args[4]
    "Flat is better than nested.", # args[5]
    "Sparse is better than dense.", # args[6]
    "Readability counts.", # args[7]
    "Special cases aren't special enough to break the rules.", # args[8]
    "Although practicality beats purity.", # args[9]
    "Errors should never pass silently.", # args[10]
    "Unless explicitly silenced.", # args[11]
    "In the face of ambiguity, refuse the temptation to guess.", # args[12]
    "There should be one-- and preferably only one --obvious way to do it.", # args[13]
    "Although that way may not be obvious at first unless you're Dutch.", # args[14]
    "Now is better than never.", # args[15]
    "Although never is often better than *right* now.", # args[16]
    "If the implementation is hard to explain, it's a bad idea.", # args[17]
    "If the implementation is easy to explain, it may be a good idea.", # args[18]
    "Namespaces are one honking great idea -- let's do more of those!", # args[19]

    autor="Tim Peters", # Primeiro Kwargs
    ano=1999, # Segundo Kwargs
)
