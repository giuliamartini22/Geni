from dataclasses import dataclass

@dataclass

class Arco:
    c1: int
    c2: int
    gen1: str
    gen2: str
    corr: float

    def __hash__(self):
        return hash(self.c1)

    def __str__(self):
        return f"Arco({self.c1}, {self.c2} - {self.gen1}, {self.gen2} - {self.corr})"

