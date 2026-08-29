def cria_personagem(nome, hp, ataque, defesa):
    return dict(nome=nome, hp=hp, ataque=ataque, defesa=defesa, vivo=True)

class GameData:

    def __init__(self) -> None:
        self.jogador = cria_personagem("jogador", 100, 20, 12)
        self.inimigo = cria_personagem("inimigo", 50, 10, 8)
        self.rodada = 1
        self.vitoria = None
        self.rodada_atual = {}

    def encontra_personagem(self, nome):
        if nome == "jogador":
            return self.jogador
        elif nome == "inimigo":
            return self.inimigo
        else:
            raise ValueError(f"Personagem '{nome}' não encontrado.")

    def aplica_dano(self, nome_personagem, dano):
        personagem = self.encontra_personagem(nome_personagem)
        personagem["hp"] -= dano
        self.rodada_atual["dano"] = dano
        self.rodada_atual["alvo"] = nome_personagem

    def obter_atributo(self, nome_personagem, atributo):
        personagem = self.encontra_personagem(nome_personagem)
        if atributo in personagem.keys():
            return personagem[atributo]
        else:
            raise ValueError(f"Atributo '{atributo}' não encontrado para o personagem '{nome_personagem}'.")

    def elimina_personagem(self, nome_personagem):
        personagem = self.encontra_personagem(nome_personagem)
        personagem["vivo"] = False

    def encerra_jogo(self, jogador_venceu):
        self.vitoria = "jogador" if jogador_venceu else "inimigo"

    def executar_rodada(self):
        from combat import executar_rodada
        self.rodada_atual = {}
        turno = self.rodada % 2
        executar_rodada(self, turno)
        self.rodada += 1
        return self.rodada_atual
