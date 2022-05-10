''' Jogo da forca simples usando listas '''
from random import choice

palavras = ['perfume', 'batata', 'alface', 'tomate']
digitadas = []
erros = 0
palavra_secreta = ''
escondida = ''

# Classe com cores para printar no terminal
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def gerar_palavra_secreta():
    return choice(palavras)

def gerar_palavra():
    palavra_escondida = esconder_palavra() 
    return palavra_escondida

def esconder_palavra():
    return ['_' for i in palavra_secreta]

def novo_jogo():
    global erros
    global palavra_secreta
    global escondida
    global digitadas

    erros = 0
    palavra_secreta = gerar_palavra_secreta()
    escondida = esconder_palavra()
    digitadas = []

print(palavra_secreta)
def revelar_letra(letra):
    for i, x in enumerate(palavra_secreta):
        if x == letra:
            escondida[i] = palavra_secreta[i]
    return escondida

novo_jogo()
while True:
    try:
        letra = input('Informe uma letra: ')

        if len(letra) > 1:
            print("Digite apenas uma letra.\n\n")
            continue
        
        if letra.lower() not in 'abcdefghijklmnopqrstuvwxyz':
            print("Isso não é uma letra\n\n")
            continue
        
        if letra.lower() in digitadas:
            print("Letra repetida. \n\n")
            continue

        letra = letra.lower()
    
        digitadas.append(letra)
        
        if letra in palavra_secreta:
            print(f'{bcolors.OKGREEN} Essa letra tem, hein! {bcolors.ENDC}')
            print(f'{revelar_letra(letra)}\n\n')

        else:
            print(f"{bcolors.FAIL} Elou! {bcolors.ENDC}\n\n")
            erros += 1

            if erros == 6:
                print(f''' 
                Fim de Jogo.

                A palavra secreta era: {palavra_secreta}
                        ''')

                novo_jogo()
                continue

        if '_' not in escondida:
            print("PARABÉNS VOCÊ ACERTOU!!!")
            novo_jogo()
            continue

        print(f'Letras já digitadas: {digitadas}\n\n')

            


    except EOFError:
        print("Usuário vacilão não digitou nada")

