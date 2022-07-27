" Recebendo Dados "

print("Qual o seu nome?")

" Entrada de dados "
nome = input()
print("Seja bem vindo(a) {0}.".format(nome))


" Segunda entrada de dados "
print("Qual a sua idade {0}?" .format(nome))
idade = input()

" Saída "
print("{0} tem {1} anos.".format(nome,idade))
print(f'{nome} nasceu em {2022 - int(idade)}')

