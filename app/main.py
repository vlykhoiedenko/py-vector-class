import math


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x_coordinate = round(x_coordinate, 2)
        self.y_coordinate = round(y_coordinate, 2)

    def __add__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            new_x = self.x_coordinate + other.x_coordinate
            new_y = self.y_coordinate + other.y_coordinate
            return Vector(new_x, new_y)
        return NotImplemented

    def __sub__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            new_x = self.x_coordinate - other.x_coordinate
            new_y = self.y_coordinate - other.y_coordinate
            return Vector(new_x, new_y)
        return NotImplemented

    def __mul__(self, other: int | float | "Vector") -> float | "Vector":
        if isinstance(other, Vector):
            dot_product = (
                self.x_coordinate * other.x_coordinate
                + self.y_coordinate * other.y_coordinate
            )
            return dot_product
        elif isinstance(other, (int, float)):
            return Vector(
                self.x_coordinate * other, self.y_coordinate * other
            )
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple[float, float],
        end_point: tuple[float, float],
    ) -> "Vector":
        x1, y1 = start_point
        x2, y2 = end_point
        new_x = x2 - x1
        new_y = y2 - y1
        return cls(new_x, new_y)

    def get_length(self) -> float:
        return math.sqrt(
            self.x_coordinate ** 2 + self.y_coordinate ** 2
        )

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(
            self.x_coordinate / length,
            self.y_coordinate / length,
        )

    def angle_between(self, other: "Vector") -> int:
        dot = (
            self.x_coordinate * other.x_coordinate
            + self.y_coordinate * other.y_coordinate
        )
        length1 = self.get_length()
        length2 = other.get_length()
        cos_alpha = dot / (length1 * length2)
        angle_in_degrees = math.degrees(math.acos(cos_alpha))
        return round(angle_in_degrees)

    def get_angle(self) -> int:
        dot = self.y_coordinate
        length1 = self.get_length()
        cos_alpha = dot / length1
        angle = math.degrees(math.acos(cos_alpha))
        return round(angle)

    def rotate(self, degrees: int | float) -> "Vector":
        radians = math.radians(degrees)
        new_x = (
            self.x_coordinate * math.cos(radians)
            - self.y_coordinate * math.sin(radians)
        )
        new_y = (
            self.x_coordinate * math.sin(radians)
            + self.y_coordinate * math.cos(radians)
        )
        return Vector(new_x, new_y)
