# Aula 02 - <code>for</code> loop e Funções

---

## Recaptulação

- `variável` -> "Poção variável" que recebe um valor. Você usa quantas vezes quiser, e ela nunca acaba.
- `tipos de variável` -> "Cores do líquido" que a Poção recebe. Cada tipo de uma "cor" e é diferente do outro
- `operadores de matemática` -> Também chamado `operadores aritméticos`, são para fazer conta:
  - `+   -   /   *`
- `if/else` -> "Portal Condicional" que decide entre executar uma coisa ou outra
- `identação` -> A quantidade de espaços no começo de cada linha que define em que "bloco" ela está

--

## Onde buscar _conhecimento_ ?

- https://andremicheletti.github.io/pycubator/
- https://www.w3schools.com/python/python_intro.asp -- Usar com google tradutor
- Simplesmente googlar "COmo fazer ... em python"

--

## Comentários

Começe uma linha com `#` e ela vai ser totalmente ignorada pelo programa.
Útil para fazer comentários para o programador (você mesmo)

```python
# Isso é um comentário
# Não vai ser executado
print("Isso vai")
```

> Coloque isso no seu **caderninho de referências**

--

# Loop Temporal

Para fazer uma mesma sequência de comandos rodar mais de uma vez, usamos o `for x in range(3)`

> Coloque isso no seu **caderninho de referências**

```python
for i in range(5):
  # Esse print vai rodar 5 vezes. Faz o teste ai menó
  print("OI")
```

--

A função `range` recebe um valor numérico X e cria uma lista de números, de 0 à X

Usamos ela como uma maneira fácil de escrever um código que "repete X vezes"

```python
lista = range(5)
# A variável lista vai ter o valor de [0, 1, 2, 3, 4]
```

--

# Funções

Uma **função** é como um "Pergaminho de Função" que você escreve sua magia uma vez e "guarda".
Toda vez que você quiser executar aquela magia, você "invoca" o seu pergaminho.

Para definir uma **função** use a palavra reservada `def`

Exemplo:

```python
def saudacoes():
  # Esses prints vão ficar "guardados" no pergaminho "saudacoes" 
  print("Olá, viajante...")
  print("Me chamo Yoda")
```

Se você rodar esse programa, ele não vai **fazer nada**.

--

Você precisa **INVOCAR** sua função para executar ela. Vamos invocar a função uma vez.

Para invocar a função, colocamos o nome dela e depois um abre e fecha parenteses `()`

```python
# Vai executar aqueles dois prints
saudacoes()
```

--

Você pode invocar a função quantas vezes quiser.

```python
# Vai executar aqueles dois prints
saudacoes()
saudacoes()
saudacoes()
```

---

## HORA DO VAMO VE

### (Exercícios)

--

Código inicial para o exercício

```python
print("--- Início do Combate ---")

player_ataque = 15
monstro_defesa = 8
player_hp = 50

# Cálculo simples de dano
dano_causado = player_ataque - monstro_defesa

if dano_causado > 0:
    print(f"Você acertou o monstro e causou {dano_causado} de dano!")
else:
    print("O ataque foi fraco demais e não causou dano.")

```

--

## 🚀 Missão 1:  O Fator Sorte (Módulo random)

Objetivo: O ataque não pode ser sempre fixo. Você deve importar a biblioteca `random` e fazer o ataque ter um fator aleatório (um dado de RPG).

Dica: "Pesquisem como gerar um número inteiro aleatório entre 1 e 6 em Python usando random."

--

##  🛡️ Missão 2: A Esquiva do Monstro

Objetivo: Adicionar a variável monstro_esquiva com um numero de 0 a 100 (ex: 20). Antes de calcular o dano, o sistema gera uma chance aleatória de 1 a 100. Se cair abaixo da esquiva, o monstro desvia e o dano é zero.

Dica: "Usem a lógica do if que aprenderam na aula 1 combinada com um novo número aleatório."  

--

## 🔄 Missão 3: A Batalha de 3 Rounds (Aplicando o for)

Objetivo: O combate não pode acabar em uma rodada.
Coloque todo o código do turno dentro de um loop for para acontecer 3 vezes seguidas.

Dica: "Como fazer um bloco de código se repetir exatamente 3 vezes usando `range`?"  

--

## 📊 Missão 4: O Status Final do Herói (Atualizando Variáveis e Funções)

Objetivo: Agora o monstro contra-ataca! A cada round, o player também perde um pouco de HP.
O ataque do monstro pode ser um número gerado aleatóriamente entre 0 e 20.

No final dos 3 rounds, exiba o HP restante do player.

> Desafio extra de arquitetura: Transformar o cálculo de dano em uma função para o código não ficar gigante.  
