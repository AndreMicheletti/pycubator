def cria_personagem(nome, hp, ataque, defesa):
    return dict(nome=nome, hp=hp, ataque=ataque, defesa=defesa, vivo=True)

jogador = cria_personagem("Jogador", 100, 20, 12)
inimigo = cria_personagem("Inimigo", 50, 10, 8)
rodada = 1
vitoria = None
rodada_atual = {}

def encontra_personagem(nome):
    if nome == "Jogador":
        return jogador
    elif nome == "Inimigo":
        return inimigo
    else:
        raise ValueError(f"Personagem '{nome}' não encontrado.")

def aplica_dano(nome_personagem, dano):
    personagem = encontra_personagem(nome_personagem)
    personagem["hp"] -= dano
    rodada_atual["dano"] = dano
    rodada_atual["alvo"] = nome_personagem

def obter_atributo(nome_personagem, atributo):
    personagem = encontra_personagem(nome_personagem)
    if atributo in personagem.keys():
        return personagem[atributo]
    else:
        raise ValueError(f"Atributo '{atributo}' não encontrado para o personagem '{nome_personagem}'.")

def elimina_personagem(nome_personagem):
    personagem = encontra_personagem(nome_personagem)
    personagem["vivo"] = False

def encerra_jogo(vitoria):
    vitoria = "jogador" if vitoria else "inimigo"
