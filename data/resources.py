# resources.py
from dataclasses import dataclass


@dataclass
class ClassGroup:
    name: str

    def __str__(self):
        return self.name


@dataclass
class Human:
    name: str
    type: str = "Profesor(a)"

    def __str__(self):
        return f"{self.name} ({self.type})"


@dataclass
class Object:
    name: str
    quantity: int = 0

    def __str__(self):
        return f"{self.name} x{self.quantity}"


@dataclass
class Place:
    name: str

    def __str__(self):
        return self.name
