import random

class TrafficSensor:
    def __init__(self, lane_name):
        self.lane_name = lane_name

    def get_vehicle_count(self):
        # Simulates a camera detecting between 0 and 30 cars
        return random.randint(0, 30)