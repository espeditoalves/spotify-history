
- [1. Projeto Spotify](#1-projeto-spotify)
- [2. Estrutura](#2-estrutura)
  - [2.1. Conjunto de Dados](#21-conjunto-de-dados)
  - [2.2. Ambiente Exploratório com Docker Compose](#22-ambiente-exploratório-com-docker-compose)
    - [2.2.1. Iniciando o container e customizando](#221-iniciando-o-container-e-customizando)
    - [2.2.2. Parar o container do jeito que está:](#222-parar-o-container-do-jeito-que-está)
    - [2.2.3. Configurando o Poetry](#223-configurando-o-poetry)
      - [2.2.3.1. pyproject.toml Não definido:](#2231-pyprojecttoml-não-definido)
      - [2.2.3.2. pyproject.toml já definido:](#2232-pyprojecttoml-já-definido)
    - [2.2.4. Passo a Passo para Obter o Token do Jupyter e Usar no VSCode](#224-passo-a-passo-para-obter-o-token-do-jupyter-e-usar-no-vscode)
      - [2.2.4.1. Use o link e token](#2241-use-o-link-e-token)
  - [3. Dashboard](#3-dashboard)
  - [4. Considerações Finais](#4-considerações-finais)

# 1. Projeto Spotify

Este projeto tem como objetivo realizar uma análise de dados do **Spotify**, utilizando ferramentas como `Python`, `PySpark`, `SQL`, `DBeaver` e `Power BI`.

O projeto foi desenvolvido com os meus próprios dados do Spotify. Esses dados, no formato JSON, foram manipulados e [salvos](./notebooks/00_db_tabelas/) em um banco de dados `PostgreSQL`. A partir do banco de dados, foi criado um link com o `Power BI `para o desenvolvimento de um `dashboard` para análise e visualização dos dados.

Além disso, foi estabelecida uma conexão com o banco de dados via `Pandas` e `PySpark` para o desenvolvimento de um notebook com uma [Análise Exploratória de Dados (EDA)](./notebooks/01_exploration/01_EDA_Spotify_User_1.ipynb), permitindo a visualização e exploração detalhada dos dados.

O projeto também conta com uma API do Spotify para a coleta de informações adicionais, que podem ser utilizadas para novas explorações e insights sobre meus gostos musicais.

# 2. Estrutura

Para melhor entendimento do projeto:

- Utilizei a arquitetura do **Docker** para construir meu ambiente exploratório.
- A pasta **`src`** foi utilizada para salvar os scripts usados nos notebooks do projeto.
- Utilizei a pasta **`notebook\00_db_tabelas`** para armazenar os notebooks com as funções de criar, puxar e inserir dados no banco de dados **PostgreSQL**.
- A pasta **`01_exploration`** foi usada para salvar as principais explorações realizadas nos dados.
- A pasta **`output`** foi utilizada para salvar todas as saídas e extrações dos dados, bem como meus arquivos de **dashboard** do Power BI.
- A pasta **`Script_sql`** foi usada para salvar meus scripts de testes e de análise de dados desenvolvidos em SQL.
- Na pasta **`Conf`** foi salvo um arquivo **.env** (somente na minha máquina pessoal) com os dados de acesso ao **Spotify** e ao **PostgreSQL**.


## 2.1. Conjunto de Dados

Para desenvolver o projeto, extraí meus dados do Spotify através deste [link](https://www.spotify.com/br-pt/account/privacy/). Após acessar a opção **"Baixe seus dados"**, selecionei **"Histórico ampliado de streamings"**.

O processo de solicitação dos dados pode levar até 30 dias para ser concluído, e os dados são enviados por e-mail no formato JSON (JavaScript Object Notation).

Com a intenção de criar uma prática de análise de dados utilizando banco de dados e SQL, decidi armazenar os dados obtidos em um banco de dados PostgreSQL.

Para isso, configurei um ambiente de análise e serviço PostgreSQL utilizando um container do Docker, conforme descrito no arquivo [docker-compose.yml](../../docker-compose.yml).

A inspiração inicial desse projeto veio do artigo [Análise de Dados do Spotify](https://medium.com/@fellipe_ao/an%C3%A1lise-de-dados-do-spotify-7c106387477b), que oferece uma visão de análise dos dados da plataforma.

Escolhi utilizar meus próprios dados para interpretar mais de perto os resultados que estarei obtendo.

> Referências
> - Fellipe Ao. (2020). Análise de Dados do Spotify. Medium. [Link](https://medium.com/@fellipe_ao/an%C3%A1lise-de-dados-do-spotify-7c106387477b)
 

## 2.2. Ambiente Exploratório com Docker Compose

Para o passo a passo a seguir é necessário ter na nessa pasta os arquivos  [docker-compose.yml](docker-compose.yml) e o arquivo [customizations.sh](/scripts/customizations.sh).

- `docker-compose.yml`: Baixa e gerencia os serviços e imagens
- `customizations.sh`: Realiza as principais customizações, como por exemplo a instalação do poetry, e instalação do **driver JDBC do PostgreSQL**.
  
### 2.2.1. Iniciando o container e customizando

1. **Iniciar o Docker Compose:** 
    ```bash
    docker-compose up
    ```
2. **Verificar os containers em execução:**
    ```bash
    docker ps
    ```
3. **Acessar o bash do container:** 
    ```bash
    # Após pegar o nome do container com docker ps
    #`docker exec -it <container_name(definido no docker-compose)> bash`
    docker exec -it pyspark_spotify_custom bash
    ```
4. **Instalar as customizações:** 
    ```bash
    sh customizations.sh
    ```
5. **Definir caminho para o poetry funcionar na sessão atual:**
    ```bash
    export PATH="$HOME/.local/bin:$PATH"
    ```
    Em seguida é necessário definir caminho para o poetry funcionar de forma permanente. Execute o seguinte comando no terminal do seu container para adicionar a linha `export PATH="$HOME/.local/bin:$PATH"` ao final do arquivo **`.bashrc`**:

    ```bash
    # Definir caminho para o poetry funcionar de forma permanente:
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> /home/jovyan/.bashrc
    ```
   - O `echo` escreve a linha desejada no terminal.
   - O `>>` adiciona (em vez de sobrescrever) o conteúdo ao final do arquivo.

Após adicionar a linha ao **.bashrc**, toda vez que o container for iniciado e uma sessão do Bash for aberta, a variável **PATH** será configurada automaticamente.

O arquivo **.bashrc** é um script de configuração executado automaticamente sempre que uma nova sessão do Bash é iniciada para o usuário. Ele contém configurações e variáveis de ambiente específicas do usuário. Adicionar o comando ao .bashrc garante que as alterações persistam entre as sessões, sem que você precise reconfigurar manualmente.

### 2.2.2. Parar o container do jeito que está:
1. **Parar todos os containers\serviços já definidos no arquivo `docker-compose.yml`:** `docker-compose stop`

2. **Iniciar os container\serviços já existentes definidos no arquivo `docker-compose.yml`:** `docker-compose start`

### 2.2.3. Configurando o Poetry

#### 2.2.3.1. pyproject.toml Não definido:
Caso o arquivo **`pyproject.toml`** não esteja definido, siga os passos:
1. **Iniciar o poetry:** `poetry init`
2. **Necessário instalar:** `poetry add ipykernel`
3. **Instalar dependências com Poetry:** `poetry install --no-root`, esse comando dessativa o empacotamento do projeto.

#### 2.2.3.2. pyproject.toml já definido:
vá direto para o comando

1. **Instalar dependências com Poetry:** `poetry install --no-root`, esse comando dessativa o empacotamento do projeto.
Em meus projetos geralmente já inicio com as principais  no arquivo **`pyproject.toml`**:
- python = "^3.10"
- ipykernel = "^6.28.0"

2. **Configurar o Kernel do Jupyter:** ```python -m ipykernel install --user --name=<container> --display-name "Python (nome_que_desejar)"```

    ```bash
    # Use esse para uma organização melhor
    python -m ipykernel install --user --name=ambiente_exploratorio --display-name "minha_venv"
    ```

### 2.2.4. Passo a Passo para Obter o Token do Jupyter e Usar no VSCode

#### 2.2.4.1. Use o link e token

- Use o link com token completo fornecido pelo docker, basta copiar o link com o token (**`http://127.0.0.1:9090/lab/?token=abc123def456`**) e colar na caixa `Existent Jupyter Server`.

- Clique em `Select Kernel` > `Select Another Kernel` > `Existent Jupyter Server`.

- O link comentado é o mesmo link utilizado para acessar o jupyter notebook via navegador

- Pode ser acesso também com os comandos:
  
    ```bash
    docker-compose logs <service_name>
    docker-compose logs
    docker logs <container_id>
    ```



## 3. Dashboard  

A análise desenvolvida pode ser explorada por meio do dashboard interativo disponível no link abaixo:  

🔗 [Acessar o Dashboard](https://app.powerbi.com/view?r=eyJrIjoiOWIyNzBhY2ItY2UwYy00NDY0LWE4MDItNGIwMGQxNGUxMWM1IiwidCI6ImFlMzhlYzZiLWY3YjEtNDJjMS1hZWM0LWEwYTNmMzgwYzRkZCJ9)  

O dashboard foi estruturado para oferecer uma experiência intuitiva, permitindo a visualização detalhada dos principais indicadores. Ele inclui funcionalidades interativas para filtrar dados, analisar tendências e extrair insights estratégicos de forma dinâmica.  

---

## 4. Considerações Finais  

A conclusão desta análise representa um passo significativo na exploração dos dados e na geração de insights valiosos. O objetivo foi transformar dados brutos em informações acessíveis e acionáveis.

Agradeço por dedicar seu tempo para revisar este projeto. Caso tenha sugestões de melhorias, insights adicionais ou ideias para futuras análises, ficarei imensamente grato pelo seu feedback. A colaboração e o aprimoramento contínuo são essenciais para a evolução dos projetos de análise de dados.  

📩 **Contato para sugestões, dúvidas ou colaborações:**  

- ✉️ **E-mail:** [espeditoalves123@hotmail.com](mailto:espeditoalves123@hotmail.com)  
- 🔗 **LinkedIn:** [Espedito Ferreira Alves](https://www.linkedin.com/in/espedito-ferreira-alves/)  



