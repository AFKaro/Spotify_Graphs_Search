from dataclasses import dataclass


@dataclass
class Artist:
    def __init__(
            self,
            name: str,
            artist_id: str,
            related_artists: list,
            genres: list):

        self.__artist_name__ = name
        self.__artist_id__ = artist_id
        self.__related_artists__ = related_artists
        self.__genres__ = genres

