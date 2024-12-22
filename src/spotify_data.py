import spotipy
from typing import Dict, Any

def obter_dados_faixa(
        sp: spotipy.Spotify, 
        track_uri: str) -> Dict[str, Any]:
    """
    Obtém informações detalhadas sobre uma faixa a partir do URI da faixa.

    Args:
        sp (spotipy.Spotify): Cliente autenticado do Spotify.
        track_uri (str): URI da faixa no Spotify.

    Returns:
        Dict[str, Any]: Dicionário contendo as informações da faixa.
        track_URI: URI da faixa

    track_name: Nome da faixa
    duration_ms: Duração da faixa em milissegundos
    popularity: Popularidade da faixa
    artists: Lista de artistas
    main_artist: Nome do artista principal
    main_artist_URI: URI do artista principal
    """
    track_info = sp.track(track_uri)
    dados = {
        "track_URI": track_info['uri'],
        "track_name": track_info['name'],
        "duration_ms": track_info['duration_ms'],
        "popularity": track_info['popularity'],
        "artists": track_info['artists'],
        "main_artist": track_info['artists'][0]['name'],
        "main_artist_URI": track_info['artists'][0]['uri'],
        "album_images":track_info['album']['images']
    }

    return dados

def obter_dados_artista(sp: spotipy.Spotify, artist_uri: str) -> Dict[str, Any]:
    """
    Obtém informações detalhadas sobre um artista a partir do URI do artista.

    Args:
        sp (spotipy.Spotify): Cliente autenticado do Spotify.
        artist_uri (str): URI do artista no Spotify.

    Returns:
        Dict[str, Any]: Dicionário contendo as informações do artista.
        artist_URI: URI do artista

    artist_name: Nome do artista
    followers: Número de seguidores do artista
    popularity: Popularidade do artista
    genres: Gêneros musicais do artista
    artist_images: Imagens do artista
    """
    artist_info = sp.artist(artist_uri)
    dados = {
        "artist_URI": artist_info['uri'],
        "artist_name": artist_info['name'],
        "followers": artist_info['followers']['total'],
        "popularity": artist_info['popularity'],
        "genres": artist_info['genres'],
        "artist_images": artist_info['images']
    }

    return dados
