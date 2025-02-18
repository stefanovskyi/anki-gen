import os
from core.flashcard_generator import FlashcardGenerator
from core.anki_exporter import AnkiExporter
from models.flashcard import Flashcard
from config.settings import Settings

def main():
    # Initialize settings
    settings = Settings()
    
    # Create flashcard generator
    generator = FlashcardGenerator()
    
    # Example prompt
    prompt = {
        "num_words": 10,
        "categories": ["Transport", "Food", "Technology"],
        "target_language": "Polish",
        "native_language": "Ukrainian"
    }
    
    # Generate flashcards
    flashcards = generator.generate(prompt)
    
    # Export to Anki deck
    exporter = AnkiExporter()
    deck_path = exporter.export_to_apkg(flashcards)
    
    print(f"Deck generated successfully at: {deck_path}")

if __name__ == "__main__":
    main() 