# Baixar a imagem oficial do PySpark com Jupyter Notebook
FROM jupyter/pyspark-notebook:spark-3.4.1

# Instalar o Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - --version 1.8.4 && \
    export PATH="$HOME/.local/bin:$PATH" && \
    poetry --version

# Adicionar o Poetry ao PATH permanentemente
ENV PATH="/home/jovyan/.local/bin:$PATH"

# Baixar a versão mais recente do driver JDBC do PostgreSQL em um diretório temporário 
RUN wget https://jdbc.postgresql.org/download/postgresql-42.2.20.jar -P /tmp/ 
# Mover o driver JDBC para o diretório correto 
USER root 
RUN mv /tmp/postgresql-42.2.20.jar /usr/local/spark/jars/

# Definir o diretório de trabalho como a pasta padrão do usuário (work directory)
WORKDIR /home/jovyan/work

# Expor a porta padrão do Jupyter Notebook
EXPOSE 8888