''' Jogo da forca simples usando listas '''
from os import system

from random import choice
from unidecode import unidecode

from palavras import palavras

digitadas = []
erros = 0
palavra_secreta = ''
escondida = ''

# Classe com cores para printar no terminal
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[90m'
    OKYELLOW = '\033[93m'
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
        if unidecode(x) == letra:
            escondida[i] = x
    
def formatar(obj):
    return ' '.join(obj)

def limpar_tela():
    system('clear')

novo_jogo()
limpar_tela()
while True:
    try:
        print(f'\n\t\t{formatar(escondida)}\n\n')
        letra = input('Informe uma letra (sem acento): ')

        if len(letra) > 1:
            limpar_tela()
            print("Digite apenas uma letra.\n\n")
            continue
         
        if letra.lower() not in 'abcdefghijklmnopqrstuvwxyz':
            limpar_tela()
            print("Isso não é uma letra\n\n")
            continue
        
        if letra.lower() in digitadas:
            limpar_tela()
            print("Letra repetida. \n\n")
            print(f'Palavras que já foram:\n {formatar(digitadas)}\n')
            continue

        letra = letra.lower()
    
        digitadas.append(letra)
        
        if letra in unidecode(palavra_secreta):
            limpar_tela()
            print(f'{bcolors.OKYELLOW} Essa letra tem, hein! {bcolors.ENDC}')
            revelar_letra(letra)

        else:
            limpar_tela()
            print(f"{bcolors.FAIL} Elou! {bcolors.ENDC}\n\n")
            erros += 1

            if erros == 6:
                limpar_tela()
                print(f''' 
                Fim de Jogo.

                A palavra secreta era: {palavra_secreta}
                        ''')

                novo_jogo()
                continue

        if '_' not in escondida:
            limpar_tela()
            print(f'A palavra era: {palavra_secreta}')
            print(f'{bcolors.OKCYAN} PARABÉNS VOCÊ ACERTOU!!! {bcolors.ENDC}')
            novo_jogo()
            continue

        print(f'Letras já digitadas: \n\n {formatar(digitadas)}\n\n')

    except EOFError:
        print("Usuário vacilão não digitou nada")

