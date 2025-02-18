# **Anki Flashcards Generator for Learning Polish**

## **Project Goal**
This project aims to create an AI-powered application that generates Anki flashcards to help Ukrainians learn Polish efficiently. The system will take a user prompt as input, generate Polish vocabulary words grouped by themes, and enrich them with essential details like phonetic transcription, part of speech, translation, example sentences, etymology, and mnemonic aids. The output will be a `.apkg` file compatible with Anki for spaced repetition learning.

## **Technology Stack**
- **Programming Language:** Python
- **AI Model:** OpenAI API (GPT-4 via LangChain)
- **Flashcard Generation:** `genanki`
- **Data Handling:** JSON for structuring generated content
- **Package Management:** `pip` for dependencies

## **Expected Input and Output**
### **Input**
- A **prompt** specifying:
  - The number of words to generate
  - The categories/themes (e.g., "Transport, Food, Technology")
  - The language focus (Polish for Ukrainian learners)

Example input prompt:
```
Generate 10 Polish vocabulary words in 3 categories: Transport, Food, and Technology. Return JSON format.
```

### **Output**
- An `.apkg` file containing Anki flashcards, formatted as per the technical requirements below.
- Each flashcard will include essential language-learning components to enhance retention and comprehension.

## **Technical Requirements for Card Formatting**
### **Front Side (Question)**
- **Word** (Polish word)
- **Phonetic transcription** (IPA format)
- **Part of speech** (noun, verb, adjective, etc.)

### **Back Side (Answer)**
- **Translation** (Ukrainian equivalent)
- **Five example sentences** (with Polish sentence structure)
- **Etymology** (origin and historical development of the word)
- **Mnemonic** (a Ukrainian-language mnemonic to help learners remember the word)

### **Example Flashcard**
#### **Front Side:**
```
samochód  
[samɔxut]  
(noun)
```
#### **Back Side:**
```
samochód  
[samɔxut]  
(noun)  

**Translation:** Автомобіль 🚗  

**Examples:**
1. Mam nowy samochód.
2. Ten samochód jest bardzo szybki.
3. Wczoraj kupiłem używany samochód.
4. Samochód stoi na parkingu.
5. Mój samochód ma uszkodzony silnik.

**Etymology:** From German "Samowagen" meaning "self-moving vehicle."  

**Mnemonic:** "Самохід" — схоже на українське слово, що означає 'саморухоме'!
```

This format ensures comprehensive language learning with AI-generated structured vocabulary and real-world usage examples.

## **Proposed Roadmap for Implementation**
### **Phase 1: Research and Planning (Week 1-2)**
- Define the key learning objectives for Ukrainian learners.
- Gather linguistic resources for Polish vocabulary.
- Investigate OpenAI API capabilities for structured language generation.
- Define JSON schema for AI-generated word details.

### **Phase 2: Development of Core Components (Week 3-5)**
- Implement prompt-based AI vocabulary generation.
- Parse AI responses into structured JSON format.
- Develop Anki flashcard creation using `genanki`.

### **Phase 3: Testing and Refinement (Week 6-7)**
- Validate generated content for accuracy and consistency.
- Test `.apkg` file import and usability in Anki.
- Adjust AI prompts and formatting rules based on feedback.

### **Phase 4: User Interface and Automation (Week 8-9)**
- Develop a simple CLI or web-based UI for user input.
- Automate deck generation and file download.
- Implement error handling and logging.

### **Phase 5: Deployment and Feedback (Week 10+)**
- Release MVP version to test users.
- Gather user feedback for improvements.
- Plan for future features like audio pronunciation support.
