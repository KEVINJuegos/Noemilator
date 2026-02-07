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

    def __str__(self):
        return self.name


@dataclass
class Object:
    name: str

    def __str__(self):
        return self.name


@dataclass
class Place:
    name: str

    def __str__(self):
        return self.name
