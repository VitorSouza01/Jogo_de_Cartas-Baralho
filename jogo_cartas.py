
# Jogo de Cartas - Baralho

# Importando a biblioteca Random que gera números aleatórios
import random

# Variáveis
naipes = '♢ ♠ ♡ ♣'.split()
cartas = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()


# Funções
# Cria um baralho com 52 cartas
def criar_baralho(aleatorio=False):
    baralho = [(n, c) for c in cartas for n in naipes]
    if aleatorio:
        random.shuffle(baralho)
    return baralho


# Gerencia a mão de cartas de acordo com o baralho gerado
def distribuir_cartas(baralho):
    return (baralho[0::4], baralho[1::4], baralho[2::4], baralho[3::4])


# Inicia um jogo de cartas para 4 jogadores
def jogar():
    cartas = criar_baralho(aleatorio=True)
    jogadores = 'Jogador_1 Jogador_2 Jogador_3 Jogador_4'.split()
    maos = {j: m for j, m in zip(jogadores, distribuir_cartas(cartas))}

    for jogador, cartas in maos.items():
        carta = ' '.join(f"{j}{c}" for (j, c) in cartas)
        print(f'{jogador}: {carta}')


# Execução
print("[Jogo de Cartas - Baralho]\n")
if __name__ == '__main__':
    jogar()
