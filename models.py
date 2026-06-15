from dataclasses import dataclass, field


@dataclass
class Position:
    company: str
    title: str


@dataclass
class User:
    name: str
    employment_history: list[Position] = field(default_factory=list)
