from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import os
from models.api_models import GenerateFlashcardsRequest, GenerateFlashcardsResponse
from core.flashcard_generator import FlashcardGenerator
from core.anki_exporter import AnkiExporter

app = FastAPI(
    title="Polish Flashcards Generator API",
    description="API for generating Anki flashcards for language learning",
    version="1.0.0"
)

@app.post("/generate-flashcards", response_model=GenerateFlashcardsResponse)
async def generate_flashcards(request: GenerateFlashcardsRequest):
    try:
        # Initialize components
        generator = FlashcardGenerator()
        exporter = AnkiExporter()
        
        # Prepare the prompt
        prompt = {
            "num_words": request.num_words,
            "categories": [request.prompt],  # Using the prompt as a category
            "target_language": request.target_language,
            "native_language": request.native_language
        }
        
        # Generate flashcards
        flashcards = generator.generate(prompt)
        
        # Export to Anki deck
        deck_path = exporter.export_to_apkg(flashcards)
        
        return GenerateFlashcardsResponse(
            deck_path=deck_path,
            num_cards=len(flashcards)
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/download/{filename}")
async def download_deck(filename: str):
    file_path = filename  # Adjust path based on where decks are saved
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Deck file not found")
    return FileResponse(file_path, filename=filename) 