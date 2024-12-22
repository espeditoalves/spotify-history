import psycopg2
import json
from typing import Dict, Any
import os
from dotenv import load_dotenv

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

def create_artists_table() -> None:
    """
    Cria a tabela 'artists' no banco de dados PostgreSQL, se ela não existir.

    A tabela contém as colunas:
    - artist_URI (chave primária)
    - artist_name
    - followers
    - popularity
    - genres (JSONB)
    - artist_images (JSONB)

    Returns:
        None
    """
    conn = psycopg2.connect(**db_config)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS artists (
            artist_URI VARCHAR PRIMARY KEY,
            artist_name VARCHAR NOT NULL,
            followers INTEGER,
            popularity INTEGER,
            genres JSONB,
            artist_images JSONB
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

def insert_artist_data(dados: Dict[str, Any]) -> None:
    """
    Insere dados na tabela 'artists' no banco de dados PostgreSQL.

    Se a artist_URI já existir, a inserção é ignorada.

    Args:
        dados (Dict[str, Any]): Dicionário contendo os dados do artista, incluindo:
            - artist_URI: URI do artista
            - artist_name: Nome do artista
            - followers: Número de seguidores
            - popularity: Popularidade do artista
            - genres: Gêneros musicais (em formato JSON)
            - artist_images: Imagens do artista (em formato JSON)

    Returns:
        None
    """
    conn = psycopg2.connect(**db_config)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO artists (artist_URI, artist_name, followers, popularity, genres, artist_images)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON CONFLICT (artist_URI) DO NOTHING;
    """, (dados['artist_URI'], dados['artist_name'], dados['followers'], dados['popularity'], 
          json.dumps(dados['genres']), json.dumps(dados['artist_images'])))
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    create_artists_table()
    # Exemplo de inserção de dados
    dados_artista = {
        "artist_URI": "spotify:artist:teste",
        "artist_name": "Nome do Artista",
        "followers": 50000,
        "popularity": 85,
        "genres": ["genre1", "genre2"],
        "artist_images": [{'url': 'image1.jpg'}, {'url': 'image2.jpg'}]
    }
    insert_artist_data(dados_artista)