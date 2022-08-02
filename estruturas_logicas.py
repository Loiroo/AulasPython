" Estruturas Lógicas: and, or, not, is "

" Operadores unários: not, is "

" Operadores binários: and, or "


ativo = True
logado = False

if ativo and logado:
    print('Usuários ativo no sistema')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')


if not ativo:
    print('Você precisa ativar sua conta, Por favor, cheque seu e-mail')
else:
    print('Bem vindo!')


if logado is False:
    print('Você precisa ativar sua conta, Por favor, cheque seu e-mail')
else:
    print('Bem vindo!')