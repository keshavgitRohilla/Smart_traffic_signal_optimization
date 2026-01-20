class TrafficLight:
    def __init__(self, direction):
        self.direction = direction
        self.color = "RED"

    def set_color(self, new_color):
        self.color = new_color
        return f"[{self.direction}] Signal is now {self.color}"