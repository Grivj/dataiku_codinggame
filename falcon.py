from route import Route
from utils import decrypt_json


class Falcon:
    def __init__(self, falcon_json_path: str):
        self.data = decrypt_json(falcon_json_path)
        self.autonomy = self.data["autonomy"]
        self.routes = self._build_routes(self.data["routes"])

    def _build_routes(self, routes_json: dict[list]) -> dict:
        routes = {}
        for route in routes_json:
            route = Route(**route)
            if route.origin not in routes:
                routes[route.origin] = {}
            routes[route.origin][route.destination] = route.travel_time
        return routes
