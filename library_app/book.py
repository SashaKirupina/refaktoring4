from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    year: str
    genre: str
    id: int
    taken: bool = False
