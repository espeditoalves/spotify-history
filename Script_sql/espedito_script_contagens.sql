/*-------------------------------------*/
/*--- CONTAGEM DE REGISTROS EM COMUM ---*/
/*-------------------------------------*/

-- Contagem distinta
SELECT COUNT(*) AS registros_comuns
FROM (
	SELECT DISTINCT spotify_track_uri 
	FROM db_myspotify.public.all_tracks_registry
) AS A
JOIN db_myspotify.public.tracks AS B  
	ON A.spotify_track_uri = B.track_uri;

/* EU PODERIA FAZER ASSIM TAMBÉM */
SELECT count(*) AS registros_comuns
FROM (SELECT DISTINCT spotify_track_uri FROM db_myspotify.public.all_tracks_registry) AS A
LEFT JOIN db_myspotify.public.tracks AS B 
	ON A.spotify_track_uri = B.track_uri
WHERE B.track_uri IS NOT NULL;

/*-------------------------------------*/
/* Contar quantos registros do 
all_tracks_registry não estão no tracks */
/*-------------------------------------*/
SELECT count(*) AS registros_nao_no_track
FROM (SELECT DISTINCT spotify_track_uri FROM db_myspotify.public.all_tracks_registry) AS A
LEFT JOIN db_myspotify.public.tracks AS B 
	ON A.spotify_track_uri = B.track_uri
WHERE B.track_uri IS NULL;


