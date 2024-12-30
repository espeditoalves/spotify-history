SELECT
	spotify_track_uri, master_metadata_track_name, count(*)  AS  total_registros
FROM db_myspotify.public.all_tracks_registry
GROUP BY spotify_track_uri, master_metadata_track_name
ORDER BY total_registros DESC;


SELECT * 
FROM db_myspotify.public.all_tracks_registry
WHERE DATE(ts) = '2019-12-07';

SELECT count(*)
FROM db_myspotify.public.all_tracks_registry
WHERE DATE(ts) = '2019-12-07';

SELECT * 
FROM db_myspotify.public.all_tracks_registry
WHERE DATE(ts) = '2019-06-17';

-- Total de horas dia
SELECT 
    DATE_TRUNC('day', ts) AS dia,
    ROUND(SUM(ms_played) / 3.6e+6, 2) AS total_horas
FROM 
    db_myspotify.public.all_tracks_registry
GROUP BY 
    DATE_TRUNC('day', ts)
ORDER BY 
    total_horas DESC;

-- Total de horas MÊS
SELECT 
    DATE_TRUNC('month', ts) AS mes,
    ROUND(SUM(ms_played) / 3.6e+6, 2) AS total_horas
FROM 
    db_myspotify.public.all_tracks_registry
GROUP BY 
    mes
ORDER BY 
    total_horas DESC



