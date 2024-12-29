SELECT
	spotify_track_uri, master_metadata_track_name, count(*)  AS  total_registros
FROM db_myspotify.public.all_tracks_registry
GROUP BY spotify_track_uri, master_metadata_track_name
ORDER BY total_registros DESC;