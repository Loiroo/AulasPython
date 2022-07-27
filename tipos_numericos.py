" Tipo Numérico "

num = 1_000_000
print(num)





" Tipo Float "

" Tipo Real, decimais "
" OBS: O separador de casas decimais na programação é ponto "

" Errado "
valor_errado = 1,44
print(valor_errado)
print(type(valor_errado))

" Certo "
valor_certo = 1.44
print(valor_certo)
print(type(valor_certo))


" Converter float para int "
" OBS: Ao converter você perde precição "

valor_float = int(valor_certo)
print(valor_float)
print(type(valor_float))







" Tipo Booleano "

" 2 constantes, True ou False "
" OBS: Sempre com a inicial maiuscula "

ativo = True
print(ativo)

" Negação (not) "
" Com a negação você inverte a constante "

print(not ativo)

" Ou (or)"
" É uma operação binária, depende de dois valores, pelo menos um precisa ser verdadeiro "

ativo1 = False
ativo2 = True

print(ativo1 or ativo2)







" Tipo String "

" Em Python, um dado é considerado string quando estiver entre àspas -> 'abc', '123', '1.2' "

nome = 'loiro'
print(nome)
print(type(nome))