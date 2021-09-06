from service import request
from domain import artist_decode 
from relations.make_relations import linking
from tools import graph_generator
from tools import data
from settings.filters import Filters
from settings.configurations import config


if __name__ == "__main__":
    
    filters = Filters(
        mean_arithmetic = 0,
        mean_weighted = 50,
        vertex_amount = 300,
        popularity = 50,
        followers = 1000,
        genres = None #["rock", "metal", "blues"]
    )

    csv_name = "relations.csv"
    pivot = "The Beatles"

    #Pick a color palette — Blues8, Reds8, Purples8, Oranges8, Viridis8
    color = "Purples8"

    configuration = config(
        pivot=pivot, 
        csv_name=csv_name, 
        color_base=color, filters=filters)
    
    payload = request.artist_payload(configuration.__getattribute__("pivot"))
    artist = artist_decode.get_artist(payload)

    related_artists_payload = request.related_artists_payload(artist.__getattribute__("id"))

    related_artists = artist_decode.get_related_artists(related_artists_payload)
    artist.__setattr__("related_artists", related_artists)

    linking(artist, filters).cupid()

    graph_generator.create(data.get_data_frame(configuration.__getattribute__("csv_name")))