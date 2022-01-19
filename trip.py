from empire import Empire
from falcon import Falcon
from planet import Planet


class Trip:
    def __init__(self, falcon: Falcon, empire: Empire, start: Planet, end: Planet):
        self.path = [start]

        self.routes = falcon.routes
        self.autonomy = falcon.autonomy
        self.tank = falcon.autonomy
        self.bounty_hunters = empire.bounty_hunters
        self.countdown = empire.countdown
        self.start = start
        self.end = end
        self.day = 0
        self.days_with_hunters = 0

    @property
    def neighbors(self):
        return (
            self.routes[self.current_planet]
            if self.current_planet in self.routes
            else []
        )

    @property
    def current_planet(self):
        return self.path[-1]

    def are_hunters_here(self) -> bool:
        if self.current_planet in self.bounty_hunters:
            return self.day in self.bounty_hunters[self.current_planet]
        return False

    def is_tank_empty(self) -> bool:
        return self.tank == 0

    def is_out_of_time(self, travel_time: int = 0) -> bool:
        return self.day + travel_time > self.countdown

    def is_arrived(self) -> bool:
        return self.current_planet == self.end

    def refuel(self) -> None:
        if self.is_out_of_time():
            raise ValueError("Out of time to refuel! Mission failed.")
        if self.is_arrived():
            raise ValueError("Already arrived!")
        if not self.neighbors:
            raise ValueError("Dead end, no need to refuel there.")
        self.tank = self.autonomy
        self.day += 1
        self.path.append(self.current_planet)
        self.days_with_hunters += self.are_hunters_here()

    def travel(self, destination: Planet) -> None:
        if destination not in self.neighbors:
            raise ValueError("This destination is not a neighbor planet.")
        if self.is_arrived():
            raise ValueError("Already arrived!")
        distance = self.neighbors[destination]
        if self.is_out_of_time(distance):
            raise ValueError("Out of time to travel! Mission failed.")
        if distance > self.tank:
            raise ValueError(
                "The tank is not filled enough to travel to the destination."
            )
        self.path.append(destination)
        self.tank -= distance
        self.day += distance
        self.days_with_hunters += self.are_hunters_here()

    @property
    def success_probability(self) -> float:
        p = sum((9 ** i) / (10 ** (i + 1)) for i in range(self.days_with_hunters))
        return 1 - p
