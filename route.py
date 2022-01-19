from planet import Planet


class Route:
    """Edges"""

    def __init__(self, origin: str, destination: str, travelTime: int):
        self.origin = Planet(origin)
        self.destination = Planet(destination)
        self.travel_time = travelTime

    def __repr__(self):
        return f"{self.origin}, {self.destination}, {self.travel_time}"
