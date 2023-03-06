primeiro_valor = input('Digite o primeiro valor:')
segundo_valor = input('Digite o segundo valor:')

primeiro_valor = int(primeiro_valor)
segundo_valor = int(segundo_valor)

if primeiro_valor > segundo_valor:
    print(f' O {primeiro_valor=} É maior que o {segundo_valor=}')

elif primeiro_valor < segundo_valor:
    print(f' {primeiro_valor=} É menor que o {segundo_valor=}')

else:
    print(f' Primeiro valor = {primeiro_valor} é igual ao  {segundo_valor=}')    