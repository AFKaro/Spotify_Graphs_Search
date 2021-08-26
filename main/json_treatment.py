import pandas as pd
import request
from pprint import pprint


def treatment(artist_id, artist_name):
    json = request.get(artist_id)['artists']
    for element in json:
        [element.pop(k) for k in ['external_urls', 'followers', 'genres', 'href', 'images', 'popularity', 'uri', 'type']]

        element['main_artist'] = artist_name
        element['related_artist'] = element['name']

        # TODO: loop de service utilizando o id dos artistas relacionados
        [element.pop(k) for k in['id', 'name']]

        pprint(element)

    df = pd.DataFrame(json)
    return df


#Teste
if __name__ == '__main__':
    the_beattles_id = '3WrFJ7ztbogyGnTHbHJFl2'
    treatment(the_beattles_id, 'The Beattles')


