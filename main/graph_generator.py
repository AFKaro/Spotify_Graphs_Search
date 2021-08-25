import networkx as nx
import json_treatment
import matplotlib.pyplot as plt


def create():
    #TODO: falta a beleza
    the_beattles = '3WrFJ7ztbogyGnTHbHJFl2'
    artist_newtwork = json_treatment.treatment(the_beattles, 'The Beattles')

    G = nx.from_pandas_edgelist(artist_newtwork, 'main_artist', 'related_artist')

    plt.figure(figsize=(10, 8))
    nx.draw_shell(G, with_labels=True)

    plt.show(block=False)
    plt.savefig("Graph.png", format="PNG")


# Teste
if __name__ == '__main__':
    create()

