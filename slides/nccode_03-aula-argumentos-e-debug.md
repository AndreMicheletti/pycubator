# Aula 03 - Funções com argumentos e retorno / <code>debugging</code>

---

## Funções com argumento

As funções podem receber qualquer número de `argumentos`. Os argumentos são valores
passados para a função que ela vai utilizar para realizar a ação dela.

A função é um `Pergaminho da Função`, e os argumentos são os "ingredientes"
ao invocar o pergaminho.

#### Exemplo

Pense num `Pergaminho da Cura` em que, para funcionar, você precisa dizer o nome
da pessoa que quer curar ao utilizá-lo. Nesse caso, o nome da pessoa é um `argumento`.

--

Os argumentos são definidos depois do parenteses da definição da função.

```python
def pergaminho_da_cura(nome):
  print(f"O alvo chamado {nome} foi curado em 10 hp!")
```

#### Olha só!!

Eles são como **variáveis** que só existem **dentro daquela função**. 
No exemplo, se eu tentar usar o `nome` fora da função, vai dar **erro**.

--

Mais de um argumento:

```python
def pergaminho_da_cura_dupla(nome1, nome2):
  print(f"Os alvos {nome1} e {nome2} foram curados em 10 hp!")


def pergaminho_da_bola_elemental(alvo1, alvo2, elemento):
  print(f"Os alvos {alvo1} e {alvo2} recebem 20 hp de dano do tipo {elemento}")

# Chamando as funções

pergaminho_da_cura_dupla("Andre", "Papai Noel")

pergaminho_da_bola_elemental("Orc", "Cyclope", "Fogo")
```


---

## Funções com retorno

As funções que definimos podem apenas executar um código para realizar uma ação externa,
ou podem ser usadas para calcular algum novo valor que desejamos.

Isso nos ajuda a criar um código limpo e organizado, e reutilizar o código
evitando repetições.

--

Para isso usamos a palavra especial `return` e algum valor.

```python
def meu_nome():
  return "Andre"
```

Assim, o código que chamar essa função, poderá atribuir o resultado a uma `variável`

```python
nome = meu_nome()
# Nome agora vai ter o valor "Andre"
```

--

É uma boa ideia sempre pensar em `funções` como **AÇÕES**, e `variáveis` como **VALORES**.

```python
def calcular_dano(ataque, defesa):
  return ataque - defesa

ataque_player = 20
ataque_monstro = 10

defesa_player = 7
defesa_monstro = 5

if turno == "player":
  dano_recebido = calcular_dano(ataque_player, defesa_monstro)
else:
  dano_recebido = calcular_dano(ataque_monstro, defesa_player)
```

--

Mais exemplos:

```python
import random

def pegar_nome_do_player():
  print("Digite seu nome:")
  nome = input()
  return nome

def rolar_dado():
  valor_aleatorio = random.randint(1, 6)
  return valor_aleatorio

def rolar_ataque_com_bonus(ataque, nome_jogador):
  if nome_jogador == "Goku":
    return ataque + 20
  else:
    return ataque
```

---

## Debugging

Uma habilidade que vocês **DEVEM** praticar é fazer o `debug` do código.

Que significa apenas 

> entender **o que o código está fazendo na prática**.

--

- Dica 1: Rodem o código frequentemente
- Dica 2: Coloquem `print` para imprimir o valor das `variáveis`
- Dica 3: Façam uma coisa de cada vez e vão evoluindo o código

---

## Exercício

A ideia da aula de hoje é praticar MUITO

E usar o método "construir aos poucos"

> Os objetivos devem ser concluídos na ordem

--

### Objetivo 1

Crie uma função `rolar_dado` que te dá sempre um valor aleatório entre 1 e 6

--

## Objetivo 2

Crie uma função `criar_atributo` que recebe um argumento chamado `base` e outro chamado `multiplicador`

A função deve chamar `rolar_dado` e te retornar o valor `base` + o resultado do `rolar_dado` multiplicado por `multiplicador`

Exemplo de resultado: Se eu chamar a função com `base=10` e `multiplicador=2`, e por acaso meu `rolar_dado` der `4`, a função deve retornar:

`10 + (4 * 2)` -> `18`

--

## Objetivo 3

Substitua no seu programa do simulador de batalha, para criar as variáveis:

- ataque_jogador
- defesa_jogador
- ataque_monstro
- defesa_monstro

Todas elas recebem um valor gerado pela chamada para `criar_atributo`

--

## Objetivo 4

Crie uma função `rodar_turno_combate`. Ela deve ser chamada dentro de um `for` e
deve ter toda a lógica de combate usando os atributos gerados anteriormente.

A ideia é o final do arquivo ficar assim:

```python
for x in range(5):
  rodar_turno_combate()
```
