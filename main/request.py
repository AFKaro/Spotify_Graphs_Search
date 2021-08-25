import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


#TODO: esconder
client_id = '{client_id}'
client_secret = '{client_secret}'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get(artist):
    result = sp.artist_related_artists(artist)
    return result


# Teste
if __name__ == '__main__':
    the_beattles = '3WrFJ7ztbogyGnTHbHJFl2'
    print(get(the_beattles))
