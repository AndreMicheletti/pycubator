import random

def executar_rodada(game_data, turno):
    alvo = "inimigo" if turno == 0 else "jogador"
    atacante = "jogador" if turno == 0 else "inimigo"
    ataque = game_data.obter_atributo(atacante, "ataque")
    defesa = game_data.obter_atributo(alvo, "defesa")
    dano = rolar_dado(ataque) - rolar_dado(defesa)
    game_data.aplica_dano(alvo, max(dano, 0))


def rolar_dado(lados):
    return random.randint(1, lados)
