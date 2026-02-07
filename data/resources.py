# resources.py
from dataclasses import dataclass


HUMAN_TYPES = [
    "Profesor(a)",
    "Secretario(a)",
    "Directivo(a)",
    "Seguridad",
    "Otro",
]

PLACE_TYPES = [
    "Aula",
    "Lab. Física",
    "Lab. Química",
    "Lab. Biología",
    "Lab. Informática",
    "Área de Deportes",
    "Sala de Reuniones",
    "Otro",
]


@dataclass
class ClassGroup:
    name: str

    def __str__(self):
        return self.name


@dataclass
class Human:
    name: str
    type: str = ""
    quantity: int = 0

    def __str__(self):
        return f"{self.name} ({self.type}) x{self.quantity}"


@dataclass
class Object:
    name: str
    quantity: int = 0

    def __str__(self):
        return f"{self.name} x{self.quantity}"


@dataclass
class Place:
    name: str
    type: str = ""
    quantity: int = 0

    def __str__(self):
        return f"{self.name} ({self.type}) x{self.quantity}"
