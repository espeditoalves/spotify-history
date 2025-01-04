
- [1. Spotify Project](#1-spotify-project)
  - [1.1. Construção do Ambiente Exploratório](#11-construção-do-ambiente-exploratório)
    - [1.1.1. Dockerfile e Docker Compose](#111-dockerfile-e-docker-compose)
    - [1.1.2. Passo a Passo](#112-passo-a-passo)
  - [1.2. Configurando o Poetry](#12-configurando-o-poetry)
  - [1.3. Passo a Passo para Obter o Token do Jupyter e Usar no VSCode](#13-passo-a-passo-para-obter-o-token-do-jupyter-e-usar-no-vscode)
    - [1.3.1. Use o link e token](#131-use-o-link-e-token)
  - [1.4. Estrutura do Projeto](#14-estrutura-do-projeto)
- [2. Entendimento da Estrutura](#2-entendimento-da-estrutura)
- [3. DASHBOARD](#3-dashboard)

# 1. Spotify Project

Este projeto tem o objetivo de realizar uma analise de dados do **SPOTIFY** utilizando ferramentas como `python`, `pyspark`, `SQL` e `PowerBI`, para desenvolver o projeto, extraí meus dados do Spotify através do link https://www.spotify.com/br-pt/account/privacy/. Após acessar a opção "Baixe seus dados", selecionei "Histórico ampliado de streamings".

O processo de solicitação dos dados pode levar até 30 dias para ser concluído, e os dados são enviados por e-mail no formato JSON (JavaScript Object Notation).

Com a intenção de criar uma prática de análise de dados utilizando Banco de Dados e SQL, decidi armazenar os dados obtidos em um banco de dados do PostgreSQL.

Para isso, configurei um ambiente de análise e serviço PostgreSQL utilizando um container do Docker, conforme descrito no arquivo [docker-compose.yml](../../docker-compose.yml).

A inspiração inicial desse projeto veio do artigo [Análise de Dados do Spotify](https://medium.com/@fellipe_ao/an%C3%A1lise-de-dados-do-spotify-7c106387477b), que oferece uma visão de analise dos dados da plataforma .

Escolhi utilizar meu próprios dados para interpretar mais de perto os resultados que estarei obtendo.

> Referências

- Fellipe Ao. (2020). Análise de Dados do Spotify. Medium. [Link](https://medium.com/@fellipe_ao/an%C3%A1lise-de-dados-do-spotify-7c106387477b)

## 1.1. Construção do Ambiente Exploratório

### 1.1.1. Dockerfile e Docker Compose

### 1.1.2. Passo a Passo

1. **Iniciar o Docker Compose:** `docker-compose up`
2. **Verificar os containers em execução:** `docker ps`
3. **Acessar o bash do container:** `docker exec -it <container> bash`

    ```bash
    # Após pegar o nome do container com docker ps
    docker exec -it spotify-history-ambiente_spotify-1 bash
    ```

4. **Iniciar os container\serviços já existentes definidos no arquivo `docker-compose.yml`:** `docker-compose start`
5. **Para todos os containers\serviços já definidos no arquivo `docker-compose.yml`:** `docker-compose stop`

Para mais comandos acessar: 

## 1.2. Configurando o Poetry

1. **Instalar dependências com Poetry:** `poetry install`
2. **Configurar o Kernel do Jupyter:** ```python -m ipykernel install --user --name=<container> --display-name "Python (nome_que_desejar)"```

    ```bash
    # Use esse para uma organização melhor
    python -m ipykernel install --user --name=spotify-history-ambiente_spotify-1 --display-name "venv_spotify"
    ```

## 1.3. Passo a Passo para Obter o Token do Jupyter e Usar no VSCode

### 1.3.1. Use o link e token

- Use o link com token completo fornecido pelo docker, basta copiar o link com o token (**`http://127.0.0.1:9090/lab/?token=abc123def456`**) e colar na caixa `Existent Jupyter Server`.

- Clique em `Select Kernel` > `Select Another Kernel` > `Existent Jupyter Server`.

- O link comentado é o mesmo link utilizado para acessar o jupyter notebook via navegador

- Pode ser acesso também com os comandos:
  
    ```bash
    docker-compose logs <service_name>
    docker-compose logs
    docker logs <container_id>
    ```

## 1.4. Estrutura do Projeto

```bash
.
├── config                      
│   ├── main.yaml                   # Main configuration file
│   ├── model                       # Configurations for training model
│   │   ├── model1.yaml             # First variation of parameters to train model
│   │   └── model2.yaml             # Second variation of parameters to train model
│   └── process                     # Configurations for processing data
│       ├── process1.yaml           # First variation of parameters to process data
│       └── process2.yaml           # Second variation of parameters to process data
├── data            
│   ├── final                       # data after training the model
│   ├── processed                   # data after processing
│   └── raw                         # raw data
├── docs                            # documentation for your project
├── .gitignore                      # ignore files that cannot commit to Git
├── Makefile                        # store useful commands to set up the environment
├── models                          # store models
├── notebooks                       # store notebooks
│   ├── exploration
│   │   └── .gitkeep
│   ├── modeling
│   │   └── .gitkeep
│   ├── preprocessing
│   │   └── .gitkeep
│   └── reporting
│       └── .gitkeep
├── output                          # store outputs
│   ├── figures
│   │   └── .gitkeep
│   ├── predictions
│   │   └── .gitkeep
│   └── reports
│       └── .gitkeep
├── .pre-commit-config.yaml         # configurations for pre-commit
├── pyproject.toml                  # dependencies for poetry
├── README.md                       # describe your project
├── src                             # store source code
│   ├── __init__.py                 # make src a Python module 
│   ├── process.py                  # process data before training model
│   ├── train_model.py              # train model
│   └── utils.py                    # store helper functions
└── tests                           # store tests
    ├── __init__.py                 # make tests a Python module 
    ├── test_process.py             # test functions for process.py
    └── test_train_model.py         # test functions for train_model.py
```

# 2. Entendimento da Estrutura

Para entendimento do projeto:

- Foi utilizado a arquitetura do docker para construir meu ambiente exploratório
- Fou utilizada a pasta **`src`** para salvar meus cripts utilizados nos notebooks do projeto
- Ultilizei a pasta `notebook\0_db_tabelas` para salvar os notebooks com as funções de criar, puxar e inserir dados no banco de dados **`POSTGRESQL`**.
- Fou utilizado a pasta `01_exploration` para salvar as principais explorações que fiz nos dados.
- Foi utilizado a pasta `output` para salvar todas as saídas e extrações dos dados e meus arquivos de DASHBOARD do Power BI
- Foi utilizado a pasta `Script_sql` para salvar meus scripts testes e de análise de dados desenvolvidos em SQL.
- Na pasta `Conf` foi salvo um arquivo env, somente na minha maquina pessoal com os dados de acesso para o **spotify** e meu **PostgreSQL**.

# 3. DASHBOARD

- Link para acessar o Dashboard desenvolvido: [link](https://espeditoalves.github.io/Resume_website/portifolio-spotify_dashboard.html)
