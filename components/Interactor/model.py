# model.py
from dataclasses import dataclass
from dataclasses import asdict
from typing import Optional

# plain old python objects
# data classes for mapping imperatively
@dataclass#(frozen=True)
class OrmLabs:
    id: int
    user_cookie: str
    name: str
    note: Optional[str]
    level: int
    active: bool
    updated: str

    def to_dict(self):
        return asdict(self)


@dataclass
class Movie:
    title: str
    overview: str
    runtime: float
    original_language: str
    budget: str
    release_date: str
    vote_count: float
    vote_average: float
    