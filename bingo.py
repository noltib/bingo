import random

def gerar_cartela(linhas, colunas, intervalos):
    cartela = []
    for coluna, intervalo in zip(range(colunas), intervalos):
        numeros = random.sample(range(intervalo[0], intervalo[1] + 1), linhas)
        for i, num in enumerate(numeros):
            if len(cartela) <= i:
                cartela.append([])
            cartela[i].append(num)
    return cartela

def exibir_cartela(jogador, cartela, dezenas_sorteadas):
    print(f"Jogador: {jogador}")
    for linha in cartela:
        linha_exibida = [
            f"({num:02})" if num in dezenas_sorteadas else f" {num:02} " for num in linha
        ]
        print(" ".join(linha_exibida))
    print()


def verificar_vencedor(cartela, dezenas_sorteadas):
    return all(num in dezenas_sorteadas for linha in cartela for num in linha)

def configurar_jogo(modo):
    if modo == "0":  
        jogadores = {1: gerar_cartela(2, 3, [(1, 10), (11, 20), (21, 30)]),
                     2: gerar_cartela(2, 3, [(1, 10), (11, 20), (21, 30)])}
        dezenas_disponiveis = list(range(1, 31))
    else: 
        jogadores = {1: gerar_cartela(3, 4, [(1, 10), (11, 20), (21, 30), (31, 40)]),
                     2: gerar_cartela(3, 4, [(1, 10), (11, 20), (21, 30), (31, 40)]),
                     3: gerar_cartela(3, 4, [(1, 10), (11, 20), (21, 30), (31, 40)]),
                     4: gerar_cartela(3, 4, [(1, 10), (11, 20), (21, 30), (31, 40)])}
        dezenas_disponiveis = list(range(1, 41))
    return jogadores, dezenas_disponiveis

def bingo():
    print("Indique o modo de jogo:\n0 - RÁPIDO\n1 - DEMORADO")
    modo = input("Escolha o modo (0 ou 1): ").strip()
    
    jogadores, dezenas_disponiveis = configurar_jogo(modo)
    dezenas_sorteadas = []
    vencedores = []

    random.shuffle(dezenas_disponiveis)

    while dezenas_disponiveis and not vencedores:

        dezena_atual = dezenas_disponiveis.pop(0)
        dezenas_sorteadas.append(dezena_atual)
        dezenas_sorteadas.sort()

        print(f"=> Última dezena sorteada: {dezena_atual:02}")
        print("Dezenas sorteadas até o momento:", " ".join(f"{num:02}" for num in dezenas_sorteadas))
        print()

        for jogador, cartela in jogadores.items():
            exibir_cartela(jogador, cartela, dezenas_sorteadas)

        for jogador, cartela in jogadores.items():
            if verificar_vencedor(cartela, dezenas_sorteadas) and jogador not in vencedores:
                vencedores.append(jogador)
        
        if not vencedores:
            input("Digite ENTER para continuar\n")

    print("Jogadores vencedores:")
    for vencedor in vencedores:
        print(f"Jogador {vencedor} é o ganhador! \\o/")


bingo()
