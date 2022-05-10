"""
String (f-string)

Nota: Strings são IMUTÁVEIS 
"""

name = "José Ba"
n1 = 10
n2 = 12.9232342

# Formata string definindo um tamanho de 10 caracteres
# e preenchendo a esquerda com cerquilha '#'
print(f'{name:#>10s}')

# Formatação de casas decimais
print(f'{n1:.1f}')
print(f'{n2:5.1f}')
print(f'{n2:.5f}')

hi = "Hello I'm the polar"

# hi[0] = 'h' <- NÃO Funciona 
hi = 'h' + hi[1:] # concatena 'h' a uma fatia de 'hi'

# hi[::2] - retorna o fatiamento da string do inicio ao final passo 2
print(hi[::2]) 

# hi[:7] - retorna o fatiamento da string até a posição 7 passo 2
print(hi[:7:2])

