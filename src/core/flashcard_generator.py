from typing import List, Dict
from models.flashcard import Flashcard
from core.openai_client import OpenAIClient
from templates.prompts import FLASHCARD_GENERATION_PROMPT

class FlashcardGenerator:
    def __init__(self):
        self.openai_client = OpenAIClient()
    
    def generate(self, prompt: Dict) -> List[Flashcard]:
        # Format the prompt using template
        formatted_prompt = FLASHCARD_GENERATION_PROMPT.format(**prompt)
        
        # Get response from OpenAI
        response = self.openai_client.generate_flashcards(formatted_prompt)
        
        # Parse response into Flashcard objects
        flashcards = self._parse_response(response)
        
        return flashcards
    
    def _parse_response(self, response: dict) -> List[Flashcard]:
        flashcards = []
        for card_data in response["flashcards"]:
            flashcard = Flashcard.from_dict(card_data)
            flashcards.append(flashcard)
        return flashcards 