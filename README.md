# ML-Games-Course

Código Base para a disciplina Aprendizagem de Máquina aplicada a Jogos.

## Dependências

### Python

Recomenda-se utilizar, no mínimo, a versão Python 3.6.9.

- Comando para instalação: ```sudo apt install -y python3-pip```

### Ambiente Virtual

É recomendado realizar a criação de um ambiente virtual para instalar as dependências do projeto.

Fora do diretório do projeto, execute os seguintes comandos:

- Instalação do vituralenv: ```sudo apt-get install python3-venv```

- Criação do ambiente: ```python3 -m venv ml-games```

- Ativação do ambiente: ```source ml-games/bin/activate```

### Instalação de Dependências

As versões das libs utilizadas no projeto estão no arquivo ```requirements.txt```. Dessa forma, basta executar os seguinte comandos com o ambiente virtual ativado:

- ```pip3 install --upgrade pip```
- ```pip3 install -r requirements.txt```

## Configuração

É necessário criar um arquivo ```.env``` no diretório raiz do projeto (ele contém as variáveis de ambiente necessárias para executar com sucesso). Ele é formado pelas variáveis abaixo (exemplo no arquivo ```.env.example```):

|   **Nome**   |  **Valor _Default_**  |    **Descrição**    |
| :---:        |     :---:      |          :---: |
|PYGAME_X_POSITION| 400 | Representa a posição da janela do pygame no eixo horizontal    |
|PYGAME_Y_POSITION| 200 | Representa a posição da janela do pygame no eixo vertical      |
|LOG_LEVEL| INFO | Indica o nível do Log |
|CATCH_NAME| Catch Game | Representa o nome do jogo Catch |
|CATCH_GRID_HEIGHT| 400 | Representa o tamanho vertical do grid do jogo Catch |
|CATCH_GRID_WIDTH| 400 | Representa o tamanho horizontal do grid do jogo Catch |
|CATCH_BALL_VELOCITY| 20 | Representa a velocidade da bola do jogo Catch |
|SNAKE_NAME| Snake Game | Representa o nome do jogo Snake |
|SNAKE_GRID_HEIGHT| 200 |Representa o tamanho vertical do grid do jogo Snake |
|SNAKE_GRID_WIDTH| 200 | Representa o tamanho horizontal do grid do jogo Snake |
|GAME| Snake | Representa o jogo que será executado |
|AGENT| Human | Representa o agente que será utilizado |
|NUM_TRIES| 10 | Representa o número de tentativas do agente no ambiente |
|TYPE| PLAY | Representa o modo de execução do agente |
|MODEL_MODE| MLP | Representa o tipo de rede neural a ser utilizada (utilizado apenas quando ```AGENT=NeuralNetwork```) |
|BALANCED_DATA| 1 | Representa se o processo de preparação irá balancear ou não os dados (default como 1 - True) |
|BATCH_SIZE| 64 | Representa o tamanho do lote de exemplos utilizado no treinamento de redes neurais |
|LEARNING_RATE| 0.05 | Representa a taxa de aprendizado |
|LOSS_NAME| mean_squared_eror | Representa a função de perda |
|OPTIMIZER_NAME| sgd | Representa o otimizador |
|NUM_EPOCHS| 50 | Representa o número de épocas no treinamento de redes neurais |
|SPLIT_FRACTION| 0.8 | Representa a fração de divisão dos exemplos utilizados para o treinamento (no caso de 0.8, representa 80% de exemplos para treinamento e 20% para teste) |
|COLOR_MODE| RGB | Representa o modo de cor que será executado |
|FRAME_HEIGHT| 32 | Representa o tamanho em altura do frame |
|FRAME_WIDTH| 32 | Representa o tamanho em largura do frame |
|COLLECTED_DATA_PATH| - | Representa o arquivo para salvar/carregar dados coletados |
|PREPARED_DATA_PATH| - | Representa o arquivo para salvar/carregar dados preparados |
|MODEL_NAME| - | Representa o arquivo com o modelo da rede neural a ser utilizado |

### Exportação das Variáveis

Sempre que o arquivo ```.env``` for modificado, é necessário exportar as novas variáveis antes de rodar o projeto pelo seguinte comando no diretório raiz: ```export $(cat .env | xargs)```

## Modos de Execução

Os modos de execução (variável ```TYPE```) podem receber os seguintes valores:

- **COLLECT:** responsável por realizar a coleta de dados do agente.
- **PLAY:** responsável por executar diversas partidas do agente.
- **PREPARE:** responsável por efetuar a preparação dos dados para o treinamento.
- **TRAIN:** responsável por realizar o treinamento das redes neurais.

Os modos descritos acima e a configuração do arquivo ```.env``` serão mais explicados em [Docs](docs/).

## Execução do Projeto

O seguinte comando deve ser executado no diretório raiz do projeto: ```python3 ml-games-course/main.py``` 

## Guia Tutorial

O diretório [Docs](docs/) contém os documentos necessários para o entendimento do projeto e também apresenta um guia para compreender os passos para coletar e preparar os dados com o objetivo treinar redes neurais e testar nos ambientes.
