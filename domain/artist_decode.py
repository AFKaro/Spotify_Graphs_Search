import json
from domain.artist import Artist


def get_artist(payload:json) -> Artist:
    """Return a domain artist"""
    payload = payload["artists"]["items"][0]

    return __make_artist__(payload=payload)


def get_related_artists(payload:json) -> list:
    artists = []
    for artist in payload["artists"]: 
        artists.append(__make_artist__(artist))

    return artists


def __make_artist__(payload: json) -> Artist:
    """"""
    artist = Artist(
        name = payload["name"],
        id = payload["id"],
        related_artists = [],
        genres = payload["genres"],
        popularity = payload["popularity"],
        followers = payload["followers"]["total"]
        )
    return artist

