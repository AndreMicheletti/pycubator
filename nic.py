def consegue_comprar(saldo_atual, preco_item):
    if saldo_atual >= preco_item:
       return True
    else:
        return False


def comprar(saldo_atual, preco_item):
    return saldo_atual - preco_item


minhas_moedas =20

preco_espada = 60

# DESAFIO:
# Use a função `consegue_comprar` para decidir se você consegue comprar a espada.
# Se sim, chame a função comprar e imprima que a espada foi comprada.
# Se não, imprima que seu saldo é insuficiente.
# No final, a variável `minhas_moedas` deve ter o valor correto.

# -- seu código aqui \/


if consegue_comprar(minhas_moedas, preco_espada):
   print("voce comprou a espada,seja util!")
   minhas_moedas = comprar(minhas_moedas, preco_espada)
else:
  print("o dono da loja te deu um pé na bunda pois voce é pobre.")

print(f"Saldo final: {minhas_moedas} G") 
