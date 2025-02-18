from dataclasses import dataclass
from typing import List

@dataclass
class Flashcard:
    word: str
    phonetic: str
    part_of_speech: str
    translation: str
    examples: List[str]
    etymology: str
    mnemonic: str
    
    def to_dict(self):
        return {
            "word": self.word,
            "phonetic": self.phonetic,
            "part_of_speech": self.part_of_speech,
            "translation": self.translation,
            "examples": self.examples,
            "etymology": self.etymology,
            "mnemonic": self.mnemonic
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data) 