# Jogos

Os jogos 2D aqui estudados são o _Catch game_ e o _Snake game_. Eles são considerado jogos simples e, portanto, ótimos laboratórios para implementação e validação de técnicas de aprendizagem de máquina.

## Catch Game

Nesse primeiro jogo, o agente tem o controle sobre uma barra na parte inferior da tela e o objetivo é capturar todos os elementos que caem da parte superior da tela, conforme imagem abaixo. Cada elemento capturado representa um vitória e cada elemento não capturado representa uma derrota. 

![catch](https://user-images.githubusercontent.com/26909849/153114688-2e1b4708-4ef9-4e9c-84c9-481be64f5213.png)

As ações possíveis para o agente são: 

- **LEFT:** mover para a esquerda;
- **RIGHT:** mover para a direita;
- **NOTHING:** não se movimentar (ficar parado). 

## Snake Game

Nesse segundo jogo, o agente controla a _snake_ e o seu objetivo é chegar até a posição onde se encontra a maçã. Alcançar tal objetivo representa vitória, no entanto, morrer (bater em alguma das paredes que limitam o tamanho da tela) e, consequentemente, não alcançando o objetivo, representa derrota. A maçã é representada pelo _pixel_ vermelho, a cabeça da _snake_ (a qual guia o seu movimento) é representada pelo _pixel_ verde, conforme ilustrado na figura abaixo.

![snake](https://user-images.githubusercontent.com/26909849/153115323-db853de4-cf08-4da0-83b0-200bee716631.png)

As ações possíveis para o agente são: 

- **LEFT:** mover para a esquerda;
- **RIGHT:** mover para a direita;
- **UP:** mover para cima;
- **DOWN:** mover para baixo. 

O agente pode realizar nenhum movimento, assim a ação considera é aquela corresponde à direção atual da _snake_ (isto é, a última ação tomada pelo agente).

## Seleção do Jogo

Para selecionar um jogo específico, basta preencher o valor da variável ```GAME``` com ```Catch``` ou ```Snake```.

Exemplos:

```
GAME="Catch"
```

```
GAME="Snake"
```
