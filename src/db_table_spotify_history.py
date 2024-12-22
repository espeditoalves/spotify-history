import sys
import psycopg2
# Adiciona o diretório 'work' ao path 
sys.path.append('/home/jovyan/work')
import src.conect_sql as conect_sql

def connect_to_db() -> psycopg2.extensions.connection:
    """
    Função para conectar ao banco de dados PostgreSQL.

    Retorna:
        conn (psycopg2.extensions.connection): Objeto de conexão com o banco de dados.
    """
    try:
        conn = psycopg2.connect(**conect_sql.db_config)
        print("Conexão com o banco de dados estabelecida com sucesso!")
        return conn
    except psycopg2.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def create_table_all_tracks_registry(conn: psycopg2.extensions.connection) -> None:
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

# Exemplo de uso
if __name__ == "__main__":
    conn = connect_to_db()
    if conn:
        create_table_all_tracks_registry(conn)
        conn.close()
