import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other) -> "Vector":
        if isinstance(other, Vector):
            x = self.x + other.x
            y = self.y + other.y
        else:
            return NotImplemented
        return Vector(x, y)

    def __sub__(self, other):
        if isinstance(other, Vector):
            x = self.x - other.x
            y = self.y - other.y
        else:
            return NotImplemented
        return Vector(x, y)

    def __mul__(self, other):
        if isinstance(other, Vector):
            dot_product = self.x * other.x + self.y * other.y
            return dot_product
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        x1, y1 = start_point
        x2, y2 = end_point
        x = x2 - x1
        y = y2 - y1
        return cls(x, y)

    def get_length(self):
        length = math.sqrt(self.x ** 2 + self.y ** 2)
        return length

    def get_normalized(self):
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other):
        dot = (self.x * other.x) + (self.y * other.y)
        length1 = math.sqrt(self.x ** 2 + self.y ** 2)
        length2 = math.sqrt(other.x ** 2 + other.y ** 2)
        cos_alpha = dot / (length1 * length2)
        angle_in_degrees = math.degrees(math.acos(cos_alpha))
        return round(angle_in_degrees)

    def get_angle(self):
        dot = (self.x * 0) + (self.y * 1)
        length1 = math.sqrt(self.x ** 2 + self.y ** 2)
        length2 = math.sqrt(0 ** 2 + 1 ** 2)
        cos_alpha = dot / (length1 * length2)
        angle = math.degrees(math.acos(cos_alpha))
        return round(angle)

    def rotate(self, degrees: int | float):
        radians = math.radians(degrees)
        x = self.x * math.cos(radians) - self.y * math.sin(radians)
        y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(x, y)
