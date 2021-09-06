from dataclasses import dataclass


@dataclass
class Artist:
    name: str
    id: str
    related_artists: list
    genres: list
    popularity: int
    followers: int

    def __eq__(self, other):
        if isinstance(other, Artist):
            return self.id == other.id
        return False

    def __hash__(self):
        return hash(('name', self.name,
                 'id', self.id))
