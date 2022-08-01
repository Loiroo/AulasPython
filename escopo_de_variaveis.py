" Escopo de variáveis "

" Dos casos de escopo: "

" 1 - Variáveis globais "
"   - Variáveis globais são reconhecidas, ou seja, seu escopo compreender, todo o programa "

" 2 - Variáveis locais "
"   - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas "

" Python é uma linguagem de tipagem dinâmica "


" Exemplo de variável global "

numero = 10
print(numero)
print(type(numero))



" Exemplo de variável local "

numero2 = 20
if numero2 > 10:
    novo = numero + 10
    print(novo)