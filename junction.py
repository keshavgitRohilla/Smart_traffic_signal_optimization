
# Note the dot (.) - this is a relative import for files in the same folder
from .traffic_light import TrafficLight
from .sensor import TrafficSensor

class Junction:
    def __init__(self, name):
        self.name = name
        # We create a dictionary of 4 directions
        self.lanes = ["North", "South", "East", "West"]
        self.signals = {d: TrafficLight(d) for d in self.lanes}
        self.sensors = {d: TrafficSensor(d) for d in self.lanes}