from __future__ import annotations


class Planet:
    def __init__(self, name: str):
        self.name = name

    def __hash__(self):
        return hash(str(self))

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other: Planet):
        if isinstance(other, Planet):
            return self.name == other.name
        if isinstance(other, str):
            return self.name == other
