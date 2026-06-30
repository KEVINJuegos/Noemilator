# resources.py
from dataclasses import dataclass, field

DAYS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]


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

HUMAN_TYPES = [
    "Profesor(a)",
    "Secretario(a)",
    "Directivo(a)",
    "Seguridad",
    "Otro",
]


@dataclass
class Event:
    id: int
    name: str

    def __str__(self):
        return f"#{self.id} {self.name}"


@dataclass
class ClassGroup:
    name: str

    def __str__(self):
        return self.name


@dataclass
class Place:
    name: str
    type: str = ""
    quantity: int = 0

    def __str__(self):
        return f"{self.name} ({self.type}) x{self.quantity}"


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


# ╔¤═══════¤DASHBOARD¤════════¤╗
@dataclass
class TimeSlot:
    number: int
    start_time: str
    end_time: str


@dataclass
class ScheduleEvent:
    day: str
    slot_number: int
    id: int = 0
    event_ids: list = field(default_factory=list)
    groups: list = field(default_factory=list)
    humans: list = field(default_factory=list)
    places: list = field(default_factory=list)
    objects: list = field(default_factory=list)

    def is_empty(self) -> bool:
        return not (
            self.event_ids or self.groups or self.humans or self.places or self.objects
        )


@dataclass
class Schedule:
    start_day: str = "Lunes"
    end_day: str = "Viernes"
    time_slots: list = field(default_factory=list)

    def get_days(self) -> list:
        if self.start_day not in DAYS or self.end_day not in DAYS:
            return DAYS[:5]
        start_idx = DAYS.index(self.start_day)
        end_idx = DAYS.index(self.end_day)
        if start_idx <= end_idx:
            return DAYS[start_idx : end_idx + 1]
        return DAYS[start_idx:] + DAYS[: end_idx + 1]
