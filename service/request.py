from domain.artist import Artist
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import json

__client_id__ = '274ddc712f6d4dc08ee72e1c5d202426'
__client_secret__ = '1527b5dded7e41ef877a9b19d9510c79'

__client_credentials_manager__ = SpotifyClientCredentials(client_id=__client_id__, client_secret=__client_secret__)
__sp__ = spotipy.Spotify(client_credentials_manager=__client_credentials_manager__)


def related_artists_payload(artist_id) -> json:
    """This method find an artist in spotify"""
    return __sp__.artist_related_artists(artist_id=artist_id)

def artist_payload(name:str) -> json:
    """return a json with artist"""
    return __sp__.search(q=name, type="artist", limit=1)
