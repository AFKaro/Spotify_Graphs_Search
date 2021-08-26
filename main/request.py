import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


#TODO: esconder
# client_id = '{client_id}'
# client_secret = '{client_secret}'

client_id = '274ddc712f6d4dc08ee72e1c5d202426'
client_secret = '1527b5dded7e41ef877a9b19d9510c79'


client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get(artist):
    result = sp.artist_related_artists(artist)
    return result


# Teste
if __name__ == '__main__':
    the_beattles = '3WrFJ7ztbogyGnTHbHJFl2'
    print(get(the_beattles))
