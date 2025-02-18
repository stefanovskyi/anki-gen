from pydantic import BaseModel

class GenerateFlashcardsRequest(BaseModel):
    prompt: str
    target_language: str = "Polish"
    native_language: str = "Ukrainian"
    num_words: int = 10

class GenerateFlashcardsResponse(BaseModel):
    deck_path: str
    num_cards: int 