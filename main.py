import random
from dataclasses import dataclass

FIRST_NAMES = [
    "Abena", "Adaeze", "Alejandro", "Alice", "Ama", "Amara", "Amira", "Ananya",
    "Anastasia", "Aoi", "Arjun", "Arman", "Ayana", "Baraka", "Beatriz", "Bogdan",
    "Camila", "Chidi", "Cyrus", "Daehyun", "Darius", "Diego", "Divya", "Dmitri",
    "Elif", "Emeka", "Fang", "Fatima", "Fiona", "Gabriel", "George", "Hana",
    "Hao", "Haruto", "Hyunwoo", "Isabela", "Ivan", "Jabari", "Jelani", "Jie",
    "Jinhee", "Jiyeon", "Jun", "Kamau", "Katarzyna", "Khalid", "Kofi", "Kwame",
    "Larissa", "Layla", "Leila", "Ling", "Lucas", "Lucía", "Makena", "Malia",
    "Mariana", "Mateo", "Mei", "Mikhail", "Minjun", "Nasrin", "Natasha", "Ngozi",
    "Nour", "Omar", "Parisa", "Priya", "Rafael", "Rahul", "Ren", "Reza",
    "Rohan", "Sakura", "Selin", "Seun", "Seungho", "Shirin", "Sneha", "Sofía",
    "Sooyeon", "Sota", "Tariq", "Tendai", "Thiago", "Valentina", "Vikram", "Wei",
    "Xiu", "Youssef", "Yui", "Yuna", "Yuto", "Zofia", "Zuri",
]

LAST_NAMES = [
    "Ahmadi", "Al-Farsi", "Alves", "Asante", "Balogun", "Brown", "Choi", "Chen",
    "Costa", "Diallo", "Dlamini", "Evans", "Ferreira", "Flores", "García", "Gupta",
    "Hassan", "Hernández", "Horvat", "Hosseini", "Huang", "Ito", "Ivanov", "Joshi",
    "Jung", "Kamau", "Kang", "Karimi", "Khalil", "Kim", "King", "Kipchoge",
    "Kobayashi", "Kowalski", "Kumar", "Lee", "Li", "Lim", "Liu", "López",
    "Mansour", "Martínez", "Mehta", "Mensah", "Mokoena", "Molnár", "Moradi", "Mousavi",
    "Mwangi", "Nakamura", "Nasser", "Ndlovu", "Novak", "Nwosu", "Odhiambo", "Okafor",
    "Oliveira", "Owusu", "Park", "Patel", "Pereira", "Petrov", "Popescu", "Qureshi",
    "Rahimi", "Reyes", "Rodríguez", "Sadeghi", "Saleh", "Sánchez", "Santos", "Sato",
    "Sharma", "Silva", "Singh", "Smith", "Sokolova", "Souza", "Suzuki", "Tanaka",
    "Taylor", "Tehrani", "Traore", "Verma", "Walker", "Wang", "Watanabe", "Waweru",
    "Williams", "Wu", "Yamamoto", "Yang", "Yilmaz", "Yoon", "Zhang",
]


@dataclass
class User:
    name: str


def generate_users(count: int) -> list[User]:
    return [
        User(name=f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}")
        for _ in range(count)
    ]


if __name__ == "__main__":
    users = generate_users(1000)
    print(f"Generated {len(users)} users. First 10:\n")
    for user in users[:10]:
        print(f"  {user.name}")
