#!/bin/bash

# Instalar o Poetry
curl -sSL https://install.python-poetry.org | python3 - --version 1.8.4

# Baixar o driver JDBC do PostgreSQL
wget https://jdbc.postgresql.org/download/postgresql-42.2.20.jar -P /usr/local/spark/jars/

# Outras configurações adicionais
echo "Customizações aplicadas com sucesso!"