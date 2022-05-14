from os import system 

opcoes = ['X', 'O']
pos = []

def mudar_vez():
    global vez
    if vez == 'X':
        vez = 'O'
    else:
        vez = 'X'

def status():
    cont = False
    ret = []

    # verifica as linhas
    for i in range(3): 
        for j in range(3):
            if pos[i][j] != vez: 
                cont = False
                break
            cont = True

        if cont:
            return True

    
    # verifica colunas
    for i in range(3):
        for j in range(3):
            if pos[j][i] != vez:
                cont = False
                break
            cont = True

        if cont:
            return True

    # comparar diagonal principal
    for i in range(3):
        if pos[i][i] != vez:
            break

        if i == 2:
            return True

    j = 2
    # compara diagonal secundaria
    for i in range(3):
        if pos[i][j] != vez:
            return False

        j -= 1

        if i == 2:
            return True
    
    return False

def novo_jogo():
    global vez
    global pos
    pos = []
    vez = 'X'

    i = 0
    j = 3

    for x in range(0,3): 
        pos.append(list(range(i,j)))
        i += 3
        j += 3

def limpar_tela():
    system("clear")

def mostrar_jogo():
    print(f'''
_{pos[0][0]}_|_{pos[0][1]}_|_{pos[0][2]}_
_{pos[1][0]}_|_{pos[1][1]}_|_{pos[1][2]}_
 {pos[2][0]} | {pos[2][1]} | {pos[2][2]}''')   

def colocar_peca(i):
    
    if i <= 2:
        lin = 0
        col = i
    elif i <= 5:
        lin = 1
        col = i - 3
    else:
        lin = 2
        col = i - 6

    if isinstance(pos[lin][col], int):
        pos[lin][col] = vez
        return True

    return False

limpar_tela()
novo_jogo()
while True:
    mostrar_jogo()
    print(f"\n\nVez do jogador: {vez}\n")
    
    op = input('Escolha uma posição: ')

    if not op.isnumeric():
        limpar_tela()
        print("num é num")
        continue 

    if int(op) not in range(0, 9):
        limpar_tela()
        print("Opção Inválida!")
        continue
    
    if not colocar_peca(int(op)):
        limpar_tela()
        print("Posição ocupada!")
        continue 
     
    limpar_tela()
 
    if status():
        limpar_tela()
        mostrar_jogo()
        print("Você ganhou!")
        print("Deseja continuar? (y/n)")
        continuar = input("")

        if continuar == 'y':
           novo_jogo()
        else:
            print("ADEUS!")
            break
    else:  
        mudar_vez()
