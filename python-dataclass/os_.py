from dataclasses import dataclass
from platform_ import Platform
from proglang import ProgLang


@dataclass(frozen=True)
class OS:
    inception: int
    name: str
    platforms: frozenset[Platform]
    proglangs: frozenset[ProgLang]
