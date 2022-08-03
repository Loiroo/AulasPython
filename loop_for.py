" Loop for "

" Loop: Estrutura de repetição "
" For: Uma dessas estrutura "

" Utilizamos loops para iteraar sobre sequências ou sobre valores iteráveis "

nome = 'Loiro'
lista = [1, 3 , 5]
numeros = range(1, 10)

" Exemplo de for 1 iterando uma string "
for letra in nome:
    print(letra)

" Exemplo de for 2 iterando sobre uma lista "
for numero in lista:
    print(numero)

"Exemplo de for 3 iterando sobre um range "
for numero in range(1, 10):
    print(numero)

for indice, letra in enumerate(nome):
    print(nome[indice])


qtd = int(input('Quantas vezes esse loop vai rodar?'))
soma = 0
for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
    print(f'A Soma é {soma}')

