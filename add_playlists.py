from agematch.models import PlaylistEmocion

# Lista de playlists con sus emociones y géneros correspondientes
playlists = [
    {
        'emocion': 'Feliz',
        'genero': 'Pop',
        'spotify_uri': 'spotify:playlist:37i9dQZF1DXcBWIGoYBM5M'  # Playlist de Spotify Happy Hits
    },
    {
        'emocion': 'Triste',
        'genero': 'Indie',
        'spotify_uri': 'spotify:playlist:37i9dQZF1DX7qK8ma5wgG1'  # Playlist de Spotify Sad Hits
    },
    {
        'emocion': 'Enojado',
        'genero': 'Rock',
        'spotify_uri': 'spotify:playlist:37i9dQZF1DX4WYpdgoIcn6'  # Playlist de Spotify Rock Classics
    },
    {
        'emocion': 'Sorprendido',
        'genero': 'Electronic',
        'spotify_uri': 'spotify:playlist:37i9dQZF1DX4WYpdgoIcn6'  # Playlist de Spotify Electronic Mix
    },
    {
        'emocion': 'Neutral',
        'genero': 'Jazz',
        'spotify_uri': 'spotify:playlist:37i9dQZF1DXbITWG1ZJKYt'  # Playlist de Spotify Jazz Classics
    }
]

# Agregar las playlists a la base de datos
for playlist in playlists:
    try:
        PlaylistEmocion.objects.create(
            emocion=playlist['emocion'],
            genero=playlist['genero'],
            spotify_uri=playlist['spotify_uri']
        )
        print(f"Playlist agregada: {playlist['emocion']}")
    except Exception as e:
        print(f"Error al agregar playlist {playlist['emocion']}: {str(e)}")
