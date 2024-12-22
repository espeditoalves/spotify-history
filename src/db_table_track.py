import sys
import psycopg2
import json
from typing import Dict, Any
import os
from dotenv import load_dotenv
# Adiciona o diretório 'work' ao path 
sys.path.append('/home/jovyan/work')
# Carregar variáveis de ambiente do arquivo .env
load_dotenv(os.path.join('config', '.env'))

# Configuração da conexão com o banco de dados
db_config = {
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT'),
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD')
}

def create_tracks_table() -> None:
    """
    Cria a tabela 'tracks' no banco de dados PostgreSQL, se ela não existir.

    A tabela contém as colunas:
    - track_URI (chave primária)
    - track_name
    - duration_ms
    - popularity
    - artists (JSONB)
    - main_artist
    - main_artist_URI
    - album_images (JSONB)

    Returns:
        None
    """
    conn = psycopg2.connect(**db_config)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS tracks (
            track_URI VARCHAR PRIMARY KEY,
            track_name VARCHAR NOT NULL,
            duration_ms INTEGER,
            popularity INTEGER,
            artists JSONB,
            main_artist VARCHAR,
            main_artist_URI VARCHAR,
            album_images JSONB
        );
    """)
    conn.commit()
    cur.close()
    conn.close()


def insert_track_data(dados: Dict[str, Any]) -> None:
    """
    Insere dados na tabela 'tracks' no banco de dados PostgreSQL.

    Se a track_URI já existir, a inserção é ignorada.

    Args:
        dados (Dict[str, Any]): Dicionário contendo os dados da faixa, incluindo:
            - track_URI: URI da faixa
            - track_name: Nome da faixa
            - duration_ms: Duração da faixa em milissegundos
            - popularity: Popularidade da faixa
            - artists: Lista de artistas (em formato JSON)
            - main_artist: Nome do artista principal
            - main_artist_URI: URI do artista principal
            - album_images: Imagens do álbum (em formato JSON)

    Returns:
        None
    """
    conn = psycopg2.connect(**db_config)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO tracks (track_URI, track_name, duration_ms, popularity, artists, main_artist, main_artist_URI, album_images)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (track_URI) DO NOTHING;
    """, (dados['track_URI'], dados['track_name'], dados['duration_ms'], dados['popularity'], 
          json.dumps(dados['artists']), dados['main_artist'], dados['main_artist_URI'], 
          json.dumps(dados['album_images'])))
    conn.commit()
    cur.close()
    conn.close()




if __name__ == "__main__":
    create_tracks_table()
    dados = {
        "track_URI": "spotify:teste:teste", 
        "track_name": "Nome da Faixa", 
        "duration_ms": 210000, 
        "popularity": 85, 
        "artists": [{'name': 'Artista 1', 'uri': 'spotify:artist:1'}, {'name': 'Artista 2', 'uri': 'spotify:artist:2'}], 
        "main_artist": "Artista 1", 
        "main_artist_URI": "spotify:artist:1",
        "album_images": [{'url': 'image1.jpg'}, {'url': 'image2.jpg'}]
    }
    insert_track_data(dados)
