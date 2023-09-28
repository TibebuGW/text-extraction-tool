from datetime import datetime
from dataclasses import dataclass, field

class MenuItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price