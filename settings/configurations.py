from settings.filters import Filters
from dataclasses import dataclass


@dataclass
class config:

    pivot: str
    csv_name: str
    color_base: str
    filters: Filters