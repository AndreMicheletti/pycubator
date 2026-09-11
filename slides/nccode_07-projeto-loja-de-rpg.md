# Aula 07 - Projeto: Loja de <code>RPG</code>

--

## Resumo do Projeto

Vamos criar um programa de `linha de comando` que vai executar em loop até o usuário sair do programa.

O programa vai ser uma **Loja de RPG**, onde você poderá comprar itens usando suas moedas. Vamos expandir esse programa nas próximas aulas.

--

## Programa exemplo

Copie e cole esse código no seu terminal. Execute usando `python` + o nome do arquivo.

```python

opcao = ""
nomes = []

while opcao.lower() != "s":
  print("\n\n\n\n\n")
  print(" -- BEM-VINDO ao programa EXEMPLO --")
  print(" O que gostaria de fazer agora:")
  print(" A -> [A]dicionar nome")
  print(" B -> [B]ritadeira")
  print(" C -> [C]ancelar nome")
  print(" V -> [V]er nomes")
  print(" S -> [S]air")

  opcao = input("Digite sua opção: ")
  opcao = opcao.lower()

  if opcao == "a":
    novo_nome = input("\nDigite o novo nome: ")
    nomes.append(novo_nome)
    print(f"Nome {novo_nome} adicionado!")
  elif opcao = "b":
    print("TRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR\n" * 20)
  elif opcao = "c":
    posicao = input("Digite a posição desejada para remover")
    posicao = int(posicao)
    removido = nomes.pop(posicao)
    print(f"Nome {removido} foi removido")
  elif opcao = "v":
    print(f"Nomes:\n{nomes}")
  elif opcao = "s":
    print("TCHAU!")
  else:
    print("Opção inválida!")

```

--

## `Loja de RPG`

**Crie sua loja RPG** na **temática** que você quiser. Alguns exemplos:

- Loja de poções
- Loja de espadas
- Loja de pergaminhos de magia
- Taverna (comidas e bebidas)

--

## Objetivos

O usuário vai começar com um número definido de moedas. Então ele vai poder comprar itens.

Defina o valor dos itens no começo do programa.

Crie um programa que roda até o usuário digitar a opção de sair. As opções serão:

1. Ver Inventário -- deve imprimir a lista de inventário e as moedas atuais
2. Ver vitrine -- deve imprimir a lista dos itens da loja
3. Comprar item -- deve pedir a posição do item da loja, e comprar se for possível.
4. Sair

Você pode escolher como fazer a escolha das opções: por letras, ou números (ou senhas secretas, por que não?)

--

## Código inicial

```python

moedas_jogador = 50

itens_jogador = []

itens_loja = ["Poção de vida ++", "Espada velha", "Kuat 1.5L", "Excalibur [Fogo][+DMG][+MAG]"]
itens_loja_precos = [10, 25, 1, 1000]

opcao = ""

## Continue o programa \/

```

--

## Objetivos extra

1. Adicione a opção de "Vender"
2. Adicione a opção de "Ver detalhes do item"
