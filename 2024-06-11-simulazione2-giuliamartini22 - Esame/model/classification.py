from dataclasses import dataclass

@dataclass
class Classification:
    GeneID: str
    Localization: str

    def __hash__(self):
        return hash(self.GeneID)

    def __str__(self):
        return f"{self.GeneID} - {self.Localization}"