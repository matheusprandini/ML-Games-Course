# Interação Agentes x Ambientes

A interação entre os agentes e os ambientes é ilustrada na imagem abaixo. Basicamente, o ambiente envia um _frame_ (imagem do jogo) que será processado processado pelo agente, o qual realiza sua tomada de decisão, efetuando uma ação no ambiente, o qual gera um novo _frame_ a partir de tal ação e assim sucessivamente.

![Interação Agente x Ambiente](https://user-images.githubusercontent.com/26909849/153315996-a80f1157-22e7-4302-9497-ec1c8377a884.jpg)

Os [agentes](../ml-games-course/agents/) implementados até o momento no projeto são os seguintes:

- **Random:** agente randômico, o qual seleciona ações de modo aleatório.

- **Human:** agente humano, o qual realiza ações a partir do _input_ de um jogador humano.

- **NeuralNetwork:** agente baseado em rede neural, o qual processa o frame e retorna a melhor ação encontrada.

## Seleção do Agente

Para selecionar um agente específico, basta preencher o valor da variável ```AGENT``` com ```Random```, ou ```Human```, ou ```NeuralNetwork```.

Exemplos:

```
AGENT="Random"
```

```
AGENT="Human"
```

```
AGENT="NeuralNetwork"
```
