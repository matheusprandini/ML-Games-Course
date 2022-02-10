# Docs

Esse diretório tem como principal função guiar o entedimento de utilização do projeto. As docs estão divididas pelos seguintes tópicos:

- **[Agentes](docs/Agentes.md):** apresenta os agentes disponíveis e como funcionam.
- **[Jogos](docs/Jogos.md):** descreve dos ambientes de jogo construídos e explica a forma de interação entre os agentes e tais ambientes.  
- **[Modo-Collect](docs/Modo-Collect.md):** descreve todo o modo de coleta de dados.
- **[Modo-Play](docs/Modo-Play.md):** descreve o modo de execução dos agentes nos ambientes.
- **[Modo-Prepare](docs/Modo-Prepare.md):** descreve todo o modo de preparação de dados a serem utilizados no treinamento das redes neurais.
- **[Modo-Train](docs/Modo-Train.md):** descreve todo o modo de treinamento das redes neurais.

## Guia

Passo a passo para entendimento de todos os módulos do projeto.

### Primeiros Passos

Primeiramente, vamos testar o funcionamento de um agente randômico (**Random**) no jogo _Catch_ por 10 tentativas. Para isso, basta configurar o arquivo ```.env``` da seguinte forma:

```
GAME="Catch"
AGENT="Random"
NUM_TRIES=10
TYPE="PLAY"
```

Exporte as variáveis pelo comando: ```export $(cat .env | xargs)```

E execute o projeto: ```python3 ml-games-course/main.py```

Agora, vamos testar o funcionamento do agente humano (você =D) no jogo _Snake_ por 20 tentativas. Para isso, configure o arquivo ```.env``` do seguinte modo:

```
GAME="Snake"
AGENT="Human"
NUM_TRIES=20
TYPE="PLAY"
```

Exporte as variáveis novamente e execute o projeto.

Por fim, vamos verificar o funcionamento de um agente baseado em uma perceptron de múltiplas camadas treinando-a com dados de 1000 jogos coletados de um supervisor humano para o jogo _Catch_. Configure o arquivo ```.env```` do modo abaixo, exporte as variáveis e rode o projeto:

```
GAME="Catch"
AGENT="NeuralNetwork"
TYPE="TRAIN"
MODEL_MODE="MLP"

BATCH_SIZE=64
LEARNING_RATE=0.1
NUM_EPOCHS=50
SPLIT_FRACTION=0.8

PREPARED_DATA_PATH="ml-games-course/data/prepared_data/catch_grayscale_32x32_1000_games.npy"
MODEL_NAME="ml-games-course/neural_networks/models/test_mlp_catch_grayscale_32x32_1000_games.h5"
```

Assim, um novo modelo ```test_mlp_catch_grayscale_32x32_1000_games.h5``` foi gerado a partir do treinamento. Vamos agora executar o agente baseado em rede neural com esse modelo por 20 partidas. Para isso, basta modificar as variáveis de acordo com o formato abaixo, exportar e rodar o projeto.

```
GAME="Catch"
AGENT="NeuralNetwork"
TYPE="PLAY"
MODEL_MODE="MLP"

COLOR_MODE="GRAYSCALE"
FRAME_HEIGHT=32
FRAME_WIDTH=32
MODEL_NAME="ml-games-course/neural_networks/models/test_mlp_catch_grayscale_32x32_1000_games.h5"
```

Pronto, chegamos ao fim dos primeiros passos no projeto. Esperamos que tenha gostado!
