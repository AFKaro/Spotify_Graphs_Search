from spotipy.oauth2 import SpotifyClientCredentials
#from artist import artist
import spotipy
import json

__client_id__ = '274ddc712f6d4dc08ee72e1c5d202426'
__client_secret__ = '1527b5dded7e41ef877a9b19d9510c79'

__client_credentials_manager__ = SpotifyClientCredentials(client_id=__client_id__, client_secret=__client_secret__)
__sp__ = spotipy.Spotify(client_credentials_manager=__client_credentials_manager__)


def get_related_artists(artist):
    """This method find an artist in spotifi"""
    return __sp__.artist_related_artists(artist)

