from dataclasses import dataclass, field
from uuid import UUID


@dataclass
class Position:
    company: str
    title: str


@dataclass
class User:
    id: UUID
    name: str
    employment_history: list[Position] = field(default_factory=list)
