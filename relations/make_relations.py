import pandas as pd
from tools import data
from service import request
from domain.artist import Artist
from dataclasses import dataclass
from domain import artist_decode
from settings.filters import Filters

@dataclass
class linking():

    pivot: Artist
    filters: Filters
    __current_relateds = []
    
    def cupid(self):
        self.__current_relateds = self.pivot.__getattribute__("related_artists")
        if not self.__make_data_frame(related_artists=self.__current_relateds):
            return

        while True:
            helpper_related = []
            for artist in self.__current_relateds:
                
                if data.get_data_frame("relations.csv")["artist"].to_list().count(artist.__getattribute__("name")) == 0:

                    related_artists_payload = request.related_artists_payload(artist.__getattribute__("id"))
                    related_artists = artist_decode.get_related_artists(related_artists_payload)
                    artist.__setattr__("related_artists", related_artists)
                    
                    self.pivot = artist
                    
                    if not self.__make_data_frame(related_artists=related_artists):
                        return
                    
                    helpper_related.extend(related_artists)
            if len(helpper_related) > 0 :
                self.__current_relateds = helpper_related


    def __make_data_frame(self, related_artists: list) -> bool:
        for artist in related_artists:
            
            f1 = self.pivot.__getattribute__("followers")
            f2 = artist.__getattribute__("followers")
            pp1 = self.pivot.__getattribute__("popularity")
            pp2 = artist.__getattribute__("popularity")

            mean_arithmetic = (pp1+pp2)/2
            mean_weighted = ((f1*pp1)+(f2*pp2))/(f1+f2)

            if pp2 >= self.filters.__getattribute__("popularity") \
                and f2 >= self.filters.__getattribute__("followers") \
                and mean_weighted >= self.filters.__getattribute__("mean_weighted"):

                if self.filters.__getattribute__("genres") != (None):
                    
                    for g in artist.__getattribute__("genres"):
                        if self.filters.__getattribute__("genres").count(g) > 0:

                            row = {
                                "artist": self.pivot.__getattribute__("name"),
                                "related_artist": artist.__getattribute__("name"),
                                "artist_popularity": pp1,
                                "related_artist_popularity": pp2,
                                "artist_followers": f1,
                                "related_artist_followers": f2,
                                "mean_arithmetic": mean_arithmetic,
                                "mean_weighted": mean_weighted,
                                "artist_genres": self.pivot.__getattribute__("genres"),
                                "related_artist_genres": artist.__getattribute__("genres")
                                }
                            self.__write_data(file_name="relations.csv", row=row)
                            break
                else:

                    row = {
                        "artist": self.pivot.__getattribute__("name"),
                        "related_artist": artist.__getattribute__("name"),
                        "artist_popularity": pp1,
                        "related_artist_popularity": pp2,
                        "artist_followers": f1,
                        "related_artist_followers": f2,
                        "mean_arithmetic": mean_arithmetic,
                        "mean_weighted": mean_weighted,
                        "artist_genres": self.pivot.__getattribute__("genres"),
                        "related_artist_genres": artist.__getattribute__("genres")
                    }
                    self.__write_data(file_name="relations.csv", row=row)
            print(len(data.get_data_frame("relations.csv")["related_artist"].unique()))
            if len(data.get_data_frame("relations.csv")["related_artist"].unique()) == \
                self.filters.__getattribute__("vertex_amount"):
                return False
        return True


    def __write_data(self, file_name:str, row: dict):
        path = "./results/"
        if data.has_file(path, file_name):
            data.write_row(path, file_name, row.values())
        else:
            data_frame = pd.DataFrame(columns=row.keys())
            data_frame = data_frame.append(row, ignore_index=True)
            data.export_to_csv(path, file_name, data_frame)