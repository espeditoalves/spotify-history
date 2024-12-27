SELECT * 
FROM all_tracks_registry
;

SELECT COUNT(*) AS total_registros 
FROM all_tracks_registry;


SELECT count(DISTINCT spotify_track_uri) AS total_distinct_registros
FROM db_myspotify.public.all_tracks_registry;

SELECT
	spotify_track_uri, master_metadata_track_name, count(*)  AS  total_registros
FROM db_myspotify.public.all_tracks_registry
GROUP BY spotify_track_uri, master_metadata_track_name
ORDER BY total_registros DESC;



SELECT count(*)
FROM tracks;

SELECT count(*)
FROM artists ;

DELETE FROM public.tracks
WHERE track_uri='spo:teste:teste';