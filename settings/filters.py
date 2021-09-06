from dataclasses import dataclass

@dataclass
class Filters:

    mean_arithmetic: float = (0,)
    mean_weighted: float = (0,)
    vertex_amount: int = (50)
    popularity: int = (0,)
    followers: int = (0,)
    genres: list = (None)
