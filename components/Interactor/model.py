# model.py
from dataclasses import dataclass
from datetime import datetime

# plain old python objects
# data classes for mapping imperatively
@dataclass(frozen=True)
class OrmLabs:
    name: str
    note: str
    level: int
    active: bool
    updated: datetime

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
    