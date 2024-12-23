import os
import sys
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv 
from typing import Dict, Any

# Adiciona o diretório 'work' ao path 
sys.path.append('/home/jovyan/work')
# Carregar variáveis de ambiente do arquivo .env
load_dotenv(os.path.join('config', '.env'))

# # Configuração da conexão com o banco de dados
# db_config = {
#     'host': os.getenv('DB_HOST'),
#     'port': os.getenv('DB_PORT'),
#     'dbname': os.getenv('DB_NAME'),
#     'user': os.getenv('DB_USER'),
#     'password': os.getenv('DB_PASSWORD')
# }

# def connect_to_db() -> psycopg2.extensions.connection:
#     """
#     Função para conectar ao banco de dados PostgreSQL.
#     Retorna:
#         conn (psycopg2.extensions.connection): Objeto de conexão com o banco de dados.
#     """
#     try:
#         conn = psycopg2.connect(**db_config)
#         print("Conexão com o banco de dados estabelecida com sucesso!")
#         return conn
#     except psycopg2.Error as e:
#         print(f"Erro ao conectar ao banco de dados: {e}")
#         return None

def create_table_all_tracks_registry(
        conn: psycopg2.extensions.connection
        ) -> None:
    """
    Função para criar a tabela necessária no PostgreSQL.

    Args:
        conn (psycopg2.extensions.connection): Objeto de conexão com o banco de dados.

    Retorna:
        None
    """
    create_table_query = """
    CREATE TABLE IF NOT EXISTS all_tracks_registry (
        ts TIMESTAMP,
        platform VARCHAR(255),
        ms_played INT,
        conn_country VARCHAR(10),
        ip_addr VARCHAR(45),
        master_metadata_track_name VARCHAR(255),
        master_metadata_album_artist_name VARCHAR(255),
        master_metadata_album_album_name VARCHAR(255),
        spotify_track_uri VARCHAR(255),
        episode_name VARCHAR(255),
        episode_show_name VARCHAR(255),
        spotify_episode_uri VARCHAR(255),
        reason_start VARCHAR(50),
        reason_end VARCHAR(50),
        shuffle BOOLEAN,
        skipped BOOLEAN,
        offline BOOLEAN,
        offline_timestamp TIMESTAMP,
        incognito_mode BOOLEAN
    );
    """
    try:
        with conn.cursor() as cur:
            cur.execute(create_table_query)
            conn.commit()
            print("Tabela criada com sucesso!")
    except psycopg2.Error as e:
        print(f"Erro ao criar a tabela: {e}")

def insert_data(
        conn: psycopg2.extensions.connection, 
        data: Dict[str, Any],
        your_table_name: str) -> None:
    """
    Insere dados no banco de dados PostgreSQL.

    Args:
        conn (psycopg2.extensions.connection): Objeto de conexão com o banco de dados.
        data (Dict[str, Any]): Dicionário contendo os dados a serem inseridos.

    Retorna:
        None
    """
    with conn.cursor() as cur:
        insert_query = sql.SQL(f"""
            INSERT INTO {your_table_name} (ts, platform, ms_played, conn_country, ip_addr, 
                                         master_metadata_track_name, master_metadata_album_artist_name, 
                                         master_metadata_album_album_name, spotify_track_uri, episode_name, 
                                         episode_show_name, spotify_episode_uri, reason_start, reason_end, 
                                         shuffle, skipped, offline, offline_timestamp, incognito_mode) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, to_timestamp(%s), %s)
        """)
        
        cur.execute(insert_query, (
            data['ts'], data['platform'], data['ms_played'], data['conn_country'], data['ip_addr'], 
            data['master_metadata_track_name'], data['master_metadata_album_artist_name'], 
            data['master_metadata_album_album_name'], data['spotify_track_uri'], data['episode_name'], 
            data['episode_show_name'], data['spotify_episode_uri'], data['reason_start'], data['reason_end'], 
            data['shuffle'], data['skipped'], data['offline'], data['offline_timestamp'], data['incognito_mode']
        ))
        
        conn.commit()
# Exemplo de uso
# if __name__ == "__main__":
#     conn = connect_to_db()
#     if conn:
#         create_table_all_tracks_registry(conn)
#         conn.close()
