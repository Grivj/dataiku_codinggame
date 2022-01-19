import copy

from trip import Trip


class C3PO:
    def __init__(self):
        self.trips = []
        self.best_probability = 0

    def explorer(self, trip: Trip):
        if trip.is_arrived() and trip.success_probability > self.best_probability:
            self.best_probability = trip.success_probability
            self.trips.append(trip)
            return

        if trip.success_probability < self.best_probability:
            return

        for neighbor in trip.neighbors:
            try:
                neighbor_trip = copy.deepcopy(trip)
                neighbor_trip.travel(neighbor)
                self.explorer(neighbor_trip)
            except:
                pass
        try:
            trip.refuel()
            self.explorer(trip)
        except:
            pass
