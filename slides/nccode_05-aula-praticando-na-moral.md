# Aula 05 - Praticando <code>na moral</code>

---

## DINÂMICA

Eu vou ser a **CPU**

Cada um vai ser uma **FUNÇÃO**, ou uma **VARIÁVEL**

--

```python
ataque = 10

ataque + 5
```

--

```python
ataque = 10

dobra_ataque(ataque)
```

--

```python
ataque = 10

ataque = dobra_ataque(ataque)
```

--

```python
ataque = 10

ataque = dobra_ataque(ataque)
ataque = reduz_ataque(ataque)
```

--

```python
ataque = 10

ataque = reduz_ataque(dobra_ataque(ataque))
```

---

## Exercícios

Vamos praticar esses exercícios para obter entendimento do que está acontecendo do código, e fixar os conceitos de `variável`,  `valor`, `função`, etc.

--

Copiem e rodem o código abaixo. Olhem o que sai no terminal e me expliquem por que a vida do herói virou `None` (nada) em vez de `130`.

```python
def usar_pocao_com_print(vida_atual):
    nova_vida = vida_atual + 30
    print(f"Curou! Nova vida: {nova_vida}")

vida_heroi = 100

# Tentando curar o herói:
vida_heroi = usar_pocao_com_print(vida_heroi)

print(f"Vida real do herói agora: {vida_heroi}")
```

--

O seu char matou um boss e ganhou o dobro de gold, mas quando foi olhar a carteira, continuava pobre. Conserte o código!

**Rode o código primeiro**

```python
def dobrar_moedas(moedas_atuais):
    return moedas_atuais * 2

minhas_moedas = 50

# O herói ganhou o bônus:
dobrar_moedas(minhas_moedas)

print(f"Minhas moedas no final: {minhas_moedas} G")
```

--

```python
def consegue_comprar(saldo_atual, preco_item):
    if saldo_atual >= preco_item:
        return True
    else:
        return False

def comprar(saldo_atual, preco_item):
  return saldo_atual - preco_item

minhas_moedas = 30
preco_espada = 50

# DESAFIO:
# Use a função `consegue_comprar` para decidir se você consegue comprar a espada.
# Se sim, chame a função comprar e imprima que a espada foi comprada.
# Se não, imprima que seu saldo é insuficiente.
# No final, a variável `minhas_moedas` deve ter o valor correto.

# -- seu código aqui \/

# ---

print(f"Saldo final: {minhas_moedas} G")
```

--

```python
import random

def rolar_dado_de_loot():
    # Sorteia um número de 1 a 6
    numero_sorteado = random.randint(1, 6)
    return numero_sorteado

# DESAFIO:
# 1. Role o dado chamando a função e capture o resultado em 'resultado_drop'
# 2. Complete o código:
#    - Se tirar 6: Ganha "Espada Lendária"
#    - Se tirar 4 ou 5: Ganha "Poção de Vida"
#    - Se tirar 1, 2 ou 3: "Nada dropou..."

resultado_drop = ...

print(f"Número que caiu: {resultado_drop}")
# Escreva os 'if/elif/else' aqui usando a variável resultado_drop
```
