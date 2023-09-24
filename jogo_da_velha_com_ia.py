simbolos = ["X", "O"]
pontuacao = {
    "EMPATE": 0,
    "X": 1,
    "O": -1
}

# Cria o Tabuleiro (Array)


def criarTabuleiro():
    tabuleiro = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    return tabuleiro

# Função para chamar o tabuleiro


def imprimeTabuleiro(tabuleiro):
    for i in range(3):
        print("|".join(tabuleiro[i]))
        if (i < 2):
            print("-----")

# Filtra erros do usuário (Digitação)


def testaTabuleiro(mensagem):
    try:
        n = int(input(mensagem))
        if (n >= 1 and n <= 3):
            return n - 1
        else:
            print("Número precisa estar entre (1 e 3)")
            return testaTabuleiro(mensagem)
    except:
        print("Deve ser um número entrre (1 e 3)")
        return testaTabuleiro(mensagem)

# Verifica se a casa escolhida esta vazia


def verificaMovimento(tabuleiro, linha, coluna):
    if (tabuleiro[linha][coluna] == " "):
        return True
    else:
        return False

# Marca o simbolo na casa escolhida


def fazMovimento(tabuleiro, linha, coluna, jogador):
    tabuleiro[linha][coluna] = simbolos[jogador]

# Passa por todas as condições de vitória possíveis e verificar se o jogador/IA ganhou


def verificaGanhador(tabuleiro):
    # linhas
    for i in range(3):
        if (tabuleiro[i][0] == tabuleiro[i][1] and tabuleiro[i][1] == tabuleiro[i][2] and tabuleiro[i][0] != " "):
            return tabuleiro[i][0]

    # coluna
    for i in range(3):
        if (tabuleiro[0][i] == tabuleiro[1][i] and tabuleiro[1][i] == tabuleiro[2][i] and tabuleiro[0][i] != " "):
            return tabuleiro[0][i]

    # primeira diagonal
    if (tabuleiro[0][0] != " " and tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][2]):
        return tabuleiro[0][0]

    # secundaria diagonal
    if (tabuleiro[0][2] != " " and tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][0]):
        return tabuleiro[0][2]

    for i in range(3):
        for j in range(3):
            if (tabuleiro[i][j] == " "):
                return False

    return "EMPATE"

# Analisa todas as possibilidades de movimento por rodada


def movimentoIA(tabuleiro, jogador):
    possibilidades = defineposicoes(tabuleiro)
    melhorValor = None
    melhorMovimento = None
    for possibilidades in possibilidades:
        tabuleiro[possibilidades[0]][possibilidades[1]] = simbolos[jogador]
        valor = miniMax(tabuleiro, jogador)
        tabuleiro[possibilidades[0]][possibilidades[1]] = " "
        if (melhorValor is None):
            melhorValor = valor
            melhorMovimento = possibilidades
        elif (jogador == 0):
            if (valor > melhorValor):
                melhorValor = valor
                melhorMovimento = possibilidades
        elif (jogador == 1):
            if (valor < melhorValor):
                melhorValor = valor
                melhorMovimento = possibilidades

    return melhorMovimento[0], melhorMovimento[1]

# Passa as casas vazias para IA


def defineposicoes(tabuleiro):
    posicoes = []
    for i in range(3):
        for j in range(3):
            if (tabuleiro[i][j] == " "):
                posicoes.append([i, j])
    return posicoes

# Coração da IA faz um cálculo para chegar na melhor jogada possível


def miniMax(tabuleiro, jogador):
    resultado = verificaGanhador(tabuleiro)
    if (resultado):
        return pontuacao[resultado]
    jogador = (jogador + 1) % 2

    possibilidades = defineposicoes(tabuleiro)
    melhorValor = None
    for possibilidades in possibilidades:
        tabuleiro[possibilidades[0]][possibilidades[1]] = simbolos[jogador]
        valor = miniMax(tabuleiro, jogador)
        tabuleiro[possibilidades[0]][possibilidades[1]] = " "

        if (melhorValor is None):
            melhorValor = valor
        elif (jogador == 0):
            if (valor > melhorValor):
                melhorValor = valor
        elif (jogador == 1):
            if (valor < melhorValor):
                melhorValor = valor

    return melhorValor

# Função main do programa da START na aplicação


def jogar():
    jogador = 1
    tabuleiro = criarTabuleiro()
    ganhador = verificaGanhador(tabuleiro)

    while (not ganhador):
        imprimeTabuleiro(tabuleiro)
        print("===============")
        if (jogador == 0):
            linha, coluna = movimentoIA(tabuleiro, jogador)
        else:
            # linha, coluna = movimentoIA(tabuleiro, jogador)
            linha = testaTabuleiro("Digite uma linha: ")
            coluna = testaTabuleiro("Digite uma coluna: ")

        if (verificaMovimento(tabuleiro, linha, coluna)):
            fazMovimento(tabuleiro, linha, coluna, jogador)
            jogador = (jogador + 1) % 2
        else:
            print("A posição Ocupada!")

        ganhador = verificaGanhador(tabuleiro)

    print("===============")
    imprimeTabuleiro(tabuleiro)
    if (ganhador == "O"):
        print("VOCÊ VENCEU")
    elif (ganhador == "X"):
        print("CPU VENCEU")
    elif (ganhador == "EMPATE"):
        print(ganhador)
    print("===============")


jogar()
