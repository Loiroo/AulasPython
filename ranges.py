" Precisamos conhecer o loop for para usar o os ranges "

" Ranges são utilizados para gerar sequências numéricas, não de forma aleatória "



" Forma 1 - início padrão no 0, e passo de 1 em 1 "

for num in range(11):
    print(num)

" Forma 2 - início especificado pelo usuário, e passo de 1 em 1 "

for num in range(4, 11):
    print(num)

" Forma 3 - início especificado pelo usuário, e passo especificado pelo usuário "

for num in range(5, 50, 5):
    print(num)

" Forma 4 - início especificado pelo usuário, e passo especificado pelo usuário (inverso) "

for num in range(10, -1, -1):
    print(num)