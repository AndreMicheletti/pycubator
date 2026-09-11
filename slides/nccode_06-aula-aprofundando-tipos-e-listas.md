# Aula 06 - Aprofundando <code>tipos</code> e <code>listas</code>

--

🛡️ Missão 1: Forjando a Identidade (String e Int)

O escrivão da guilda precisa registrar você, mas ele está misturando números com textos.

Objetivo: Crie uma variável nome (`string`) e uma variável nivel (`int`). Imprima na tela a frase: `"O aventureiro [nome] chegou ao nível [nivel]!"`

Desafio: Você não pode simplesmente somar uma string com um int usando o sinal de + sem dar erro.

Missão de Pesquisa: Descubra o que são f-strings no Python ou como converter um int para string (str()).

--

🗡️ Missão 2: O Dano Crítico (Float e Int)

Você acertou o ponto fraco do monstro! O dano base é um número inteiro, mas o multiplicador de crítico é um número "quebrado" (float).

Objetivo: Crie `dano_base = 25` e `multiplicador = 1.5`. Calcule o dano total multiplicando os dois.

Desafio: O resultado será um número float (ex: 37.5). Um monstro não pode perder "meio" ponto de vida.

Missão de Pesquisa: Pesquise como converter um `float` em um `int (arredondando para baixo) em Python.

--

📜 Missão 3: O Grito de Batalha (Manipulação de String)

Você encontrou um Pergaminho de Feitiço, mas para conjurá-lo, ele precisa ser gritado a plenos pulmões.

Objetivo: Crie a variável `feitico = input()`. Imprima essa string inteira em MAIÚSCULAS.
Depois, faça ele imprimir ela em minúsculo.

Desafio: Você não pode reescrever a variável manualmente. Tem que fazer o Python transformar o texto.

Missão de Pesquisa: Procure por "como deixar string maiúscula em Python"

--

🎒 Missão 4: A Primeira Mochila (Introdução às Listas)

Você ganhou sua primeira mochila! Ela pode guardar várias poções em espaços numerados (índices).

Objetivo: Crie uma lista chamada inventario contendo 3 itens de texto: `"Poção de Vida", "Corda", "Adaga".`

Desafio: Imprima na tela apenas o segundo item da sua mochila (`"Corda"`).

Missão de Pesquisa: Lembre-se, na programação, a contagem dos slots não começa no número 1. Em qual número ela começa?

--

💎 Missão 5: O Loot do Goblin (Adicionando à Lista)

Você derrotou um Goblin saquear seu corpo e encontrou um "Dente de Ouro".

Objetivo: Pegue a lista inventario da missão anterior e adicione o "Dente de Ouro" nela. Imprima o inventário completo no final.

Desafio: Você não pode recriar a lista do zero, precisa adicionar o item à lista que já existe.

Missão de Pesquisa: Como adicionar um item ao final de uma lista em Python?

--

🧪 Missão 6: Consumindo a Poção (Removendo da Lista)

Seu HP caiu! Você precisa beber a "Poção de Vida" que está na sua mochila.

Objetivo: Remova a "Poção de Vida" do seu inventario. Imprima como a mochila ficou após o uso.

Desafio: Se você usar o feitiço de remoção errado, pode acabar apagando o item errado ou destruindo a mochila inteira.

Missão de Pesquisa: Como remover um item específico de uma lista pelo seu nome?

--

⚖️ Missão 7: Sobrecarga (Tamanho da Lista)

O seu personagem é fraco e só consegue carregar no máximo 5 itens na mochila.

Objetivo: Crie um if que verifique a quantidade de itens no seu inventario. Se for maior que 5, imprima "Você está sobrecarregado!".

Desafio: Como o Python sabe quantos itens existem dentro de uma lista [ ] sem que você tenha que contar manualmente?

Missão de Pesquisa: Descubra como pegar o tamanho (quantidade de elementos) de uma lista em Python

--

🗺️ Missão 8: O Mapa Rasgado (String para Lista)

Você encontrou uma pista desenhada na parede: "Norte,Leste,Sul,Oeste,Norte". É uma única string separada por vírgulas.

Objetivo: Transforme essa string única em uma Lista contendo 5 itens separados.

Desafio: É muito demorado digitar item por item na mão. O Python tem um truque mágico para fatiar textos baseados em um caractere (no caso, a vírgula).

Missão de Pesquisa: Como dividir uma string em uma lista em Python?

--

💰 Missão 9: A Loja do Mercador (Matemática de Listas)

O mercador te ofereceu 4 espadas. Os preços delas são: [150, 85, 300, 210].

Objetivo: Imprima na tela qual é o valor da espada MAIS CARA e da MAIS BARATA.

Desafio: Sem usar a estrutura de loop (for) e sem olhar manualmente, faça o Python descobrir o maior e o menor número da lista.

Missão de Pesquisa: Pesquise as funções matemáticas nativas de listas no Python

--

🐉 Missão 10: O Boss - A Última Esperança (Índice Reverso)

O dragão está prestes a te atacar. Sua única chance de sobreviver é usar o último item que você colocou na sua mochila.

Objetivo: Imprima na tela o último item da sua lista de inventario.

Desafio: Você NÃO sabe qual é o tamanho da sua lista. Ela pode ter 3 itens ou 100 itens. Como mandar o Python pegar o último item não importando o tamanho dela?

Missão de Pesquisa: Pesquise sobre "índices negativos em listas no Python". O que acontece se você pedir o item da posição -1?
