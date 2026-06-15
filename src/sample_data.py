import random

from uuid import UUID, uuid4

from models import Position, User

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


COMPANIES = [
    "3M", "Abbott", "Accor", "Accenture", "Adobe", "Adidas", "Airbnb", "Airbus",
    "Allianz", "Alibaba", "Amazon", "American Express", "Apple", "AstraZeneca",
    "AT&T", "Atlassian", "AXA", "Bain & Company", "Banco Santander", "Bank of America",
    "Barclays", "BASF", "Bayer", "BCG", "Bechtel", "Berkshire Hathaway", "BMW",
    "BNP Paribas", "Boeing", "Booz Allen Hamilton", "Bosch", "BP", "Bristol-Myers Squibb",
    "British Airways", "ByteDance", "Carrefour", "Caterpillar", "CBRE", "Chevron",
    "Cisco", "Citibank", "Cloudflare", "Coca-Cola", "Colgate-Palmolive", "Comcast",
    "Compass Group", "CrowdStrike", "CVS Health", "Datadog", "Databricks", "Dell",
    "Deloitte", "Delta Air Lines", "Deutsche Bank", "Deutsche Telekom", "DHL",
    "Disney", "DocuSign", "eBay", "Eli Lilly", "Emirates", "Equinor", "Ericsson",
    "Etsy", "ExxonMobil", "EY", "FedEx", "Fidelity", "Flipkart", "Ford",
    "General Electric", "General Motors", "GlaxoSmithKline", "Goldman Sachs", "Google",
    "Grab", "H&M", "Halliburton", "Hilton", "Honda", "Honeywell", "HP",
    "HSBC", "Huawei", "Hyundai", "IBM", "IKEA", "Infosys", "Intel",
    "Johnson & Johnson", "Jones Lang LaSalle", "JPMorgan Chase", "Kaiser Permanente",
    "Kimberly-Clark", "KPMG", "L'Oréal", "Lidl", "LinkedIn", "Lockheed Martin",
    "Lufthansa", "Maersk", "Marriott", "Mastercard", "Mayo Clinic", "McDonald's",
    "McKinsey", "Medtronic", "Mercedes-Benz", "Merck", "Meta", "Microsoft",
    "Moderna", "Morgan Stanley", "Nestlé", "Netflix", "News Corp", "Nike",
    "Nokia", "Novartis", "Nvidia", "Oliver Wyman", "Oracle", "Orange", "Palantir",
    "Paramount", "PayPal", "Pearson", "PepsiCo", "Pfizer", "Philip Morris",
    "Procter & Gamble", "PwC", "Qualcomm", "Rakuten", "Red Hat", "Roche",
    "Ryanair", "Samsung", "Sanofi", "SAP", "Saudi Aramco", "Schlumberger",
    "Sea Group", "ServiceNow", "Shell", "Shopify", "Siemens", "Singapore Airlines",
    "Slack", "Snowflake", "SoftBank", "Sony", "Spotify", "Splunk", "Starbucks",
    "Stellantis", "Stripe", "T-Mobile", "Tata Consultancy", "Telefónica", "Tesla",
    "Tesco", "Texas Instruments", "TotalEnergies", "Toyota", "Twilio", "Uber",
    "UBS", "Unilever", "Uniqlo", "United Airlines", "UnitedHealth Group", "Universal Music Group",
    "UPS", "Vanguard", "Verizon", "Vinci", "Visa", "VMware", "Volkswagen",
    "Vodafone", "Walmart", "Warner Bros. Discovery", "Wells Fargo", "Wipro",
    "Workday", "Yum! Brands", "Zalando", "Zoom",
]

TITLES = [
    "Account Executive", "Account Manager", "Actuary", "Administrative Director",
    "Associate Consultant", "Backend Engineer", "Brand Manager", "Business Analyst",
    "Business Development Manager", "Chief Executive Officer", "Chief Financial Officer",
    "Chief of Staff", "Chief Operating Officer", "Clinical Research Associate",
    "Compliance Manager", "Compliance Officer", "Content Strategist", "Controller",
    "Credit Analyst", "Data Engineer", "Data Scientist", "DevOps Engineer",
    "Engineering Manager", "Executive Assistant", "Financial Analyst", "Frontend Engineer",
    "Full Stack Engineer", "General Counsel", "Growth Manager", "Head of Product",
    "Healthcare Administrator", "HR Business Partner", "Investment Banker",
    "Legal Counsel", "Logistics Manager", "Management Consultant", "Marketing Manager",
    "Medical Affairs Manager", "ML Engineer", "Office Manager", "Operations Director",
    "Operations Manager", "Paralegal", "People Operations Manager", "Portfolio Manager",
    "Principal Engineer", "Procurement Manager", "Product Designer", "Product Manager",
    "Project Manager", "Public Relations Manager", "QA Engineer", "Recruiter",
    "Regional Sales Manager", "Risk Analyst", "Sales Representative", "Security Engineer",
    "Site Reliability Engineer", "Social Media Manager", "Software Architect",
    "Software Engineer", "Solutions Architect", "Strategy Consultant", "Supply Chain Manager",
    "Talent Acquisition Specialist", "Technical Lead", "Trader", "UX Designer",
    "VP of Engineering", "VP of Sales", "Wealth Manager",
]


def generate_employment_history() -> list[Position]:
    return [
        Position(company=random.choice(COMPANIES), title=random.choice(TITLES))
        for _ in range(random.randint(1, 5))
    ]


def generate_users(count: int) -> list[User]:
    return [
        User(
            id=uuid4(),
            name=f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}",
            employment_history=generate_employment_history(),
        )
        for _ in range(count)
    ]


def generate_connections(users: list[User]) -> list[tuple[UUID, UUID]]:
    user_ids = [u.id for u in users]
    pairs: set[tuple[UUID, UUID]] = set()
    for user_id in user_ids:
        others = random.sample([uid for uid in user_ids if uid != user_id], random.randint(5, 30))
        for other_id in others:
            pairs.add((min(user_id, other_id), max(user_id, other_id)))
    return list(pairs)
