import os
import sys
from dotenv import load_dotenv 
sys.path.append('/home/jovyan/work')

# Carregar variáveis de ambiente do arquivo .env na pasta config 
load_dotenv(os.path.join('config', '.env'))
db_config = {
    'host': os.getenv('DB_HOST'), 
    'port': os.getenv('DB_PORT'), 
    'dbname': os.getenv('DB_NAME'), 
    'user': os.getenv('DB_USER'), 
    'password': os.getenv('DB_PASSWORD')
}