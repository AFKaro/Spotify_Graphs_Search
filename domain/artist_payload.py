import json
from pprint import pprint


def make_artist(payload: json):
    """"""

    for element in payload:
        [element.pop(k) for k in ['external_urls', 'followers', 'genres', 'href', 'images', 'popularity', 'uri', 'type']]

        #element['main_artist'] = artist_name
        element['related_artist'] = element['name']

        # TODO: loop de service utilizando o id dos artistas relacionados
        [element.pop(k) for k in['id', 'name']]

        pprint(element)
