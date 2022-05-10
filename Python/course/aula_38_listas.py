'''
Listas em python
insert, pop, del, clear, extend, append
'''

personagens = ['Naruto', 'obito', 'goku']
numeros = list(range(1,5))
primos = ['2', 'tres', 'cinco']
 
personagens.append("bills")
print(personagens)

numeros.extend(primos)
print(f'extend: {numeros}')

numeros.insert(2, primos)
print(f'insert: {numeros}')

# remove o último elemento e retorna ele
print(numeros.pop())

# remove o elemento 'i' e retorna ele
print(numeros.pop(2))

for i in numeros:
    print(i)

for i, x in enumerate(numeros):
    print(i, x)
