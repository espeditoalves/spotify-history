
- [1. Spotify Project](#1-spotify-project)
  - [1.1. Construção do Ambiente Exploratório](#11-construção-do-ambiente-exploratório)
    - [1.1.1. Dockerfile e Docker Compose](#111-dockerfile-e-docker-compose)
    - [Passo a Passo](#passo-a-passo)
  - [1.2. Configurando o Poetry](#12-configurando-o-poetry)
  - [1.3. Passo a Passo para Obter o Token do Jupyter e Usar no VSCode](#13-passo-a-passo-para-obter-o-token-do-jupyter-e-usar-no-vscode)
    - [1.3.1. Use o link e token](#131-use-o-link-e-token)
  - [1.4. Estrutura do Projeto](#14-estrutura-do-projeto)

# 1. Spotify Project

TEXTO

## 1.1. Construção do Ambiente Exploratório

### 1.1.1. Dockerfile e Docker Compose

### Passo a Passo

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