import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: 'Vector') -> 'Vector':
        if isinstance(other, Vector):
            x = self.x + other.x
            y = self.y + other.y
            return Vector(x, y)
        return NotImplemented

    def __sub__(self, other: 'Vector') -> 'Vector':
        if isinstance(other, Vector):
            x = self.x - other.x
            y = self.y - other.y
            return Vector(x, y)
        return NotImplemented

    def __mul__(self, other: int | float | 'Vector') -> float | 'Vector':
        if isinstance(other, Vector):
            dot_product = self.x * other.x + self.y * other.y
            return dot_product
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple[float, float],
        end_point: tuple[float, float]
    ) -> 'Vector':
        x1, y1 = start_point
        x2, y2 = end_point
        x = x2 - x1
        y = y2 - y1
        return cls(x, y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> 'Vector':
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: 'Vector') -> int:
        dot = (self.x * other.x) + (self.y * other.y)
        length1 = self.get_length()
        length2 = other.get_length()
        cos_alpha = dot / (length1 * length2)
        angle_in_degrees = math.degrees(math.acos(cos_alpha))
        return round(angle_in_degrees)

    def get_angle(self) -> int:
        dot = self.y  # (self.x * 0) + (self.y * 1) = self.y
        length1 = self.get_length()
        cos_alpha = dot / length1
        angle = math.degrees(math.acos(cos_alpha))
        return round(angle)

    def rotate(self, degrees: int | float) -> 'Vector':
        radians = math.radians(degrees)
        x = self.x * math.cos(radians) - self.y * math.sin(radians)
        y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(x, y)
