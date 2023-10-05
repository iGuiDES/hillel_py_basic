schoolchildren = int(input('Введіть кількість школярів: '))
apples = int(input('Введіть кількість яблук: '))

got_apples = apples // schoolchildren
balance_basket = apples % schoolchildren

print('Кожному школяру дісталося яблук: ', got_apples)
print('У кошику залишилося: ', balance_basket, 'яблук')
