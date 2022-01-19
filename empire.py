from utils import decrypt_json


class Empire:
    def __init__(self, empire_json_path: str):
        self.data = decrypt_json(empire_json_path)
        self.countdown = self.data["countdown"]
        self.bounty_hunters = self._build_hunters_positions(self.data["bounty_hunters"])

    def _build_hunters_positions(self, hunters_list: list[dict]):
        positions = {}
        for hunter in hunters_list:
            planet, day = hunter.values()
            if planet not in positions:
                positions[planet] = []
            positions[planet].append(day)
        return positions
