# Sentiment Text Classifier (Compliments vs Negative Phrases)

A Python script that classifies input text as **Compliments** or **Negative phrases** using a **MachineLearningForKids** hosted API model.

## Classes
- Compliments
- Negative phrases

## Project Structure
```

.
├── app.py
├── requirements.txt
├── .gitignore
├── .env.example
└── data/
├── compliments.txt
└── negative_phrases.txt

````

## Setup

### Install dependencies
```bash
pip install -r requirements.txt
````

### Add API key

Create a file named `.env` (same folder as `app.py`) and add:

```text
MLFK_API_KEY=PASTE_YOUR_KEY_HERE
```

## Run

```bash
python app.py
```

If `python` doesn’t work on Windows:

```bash
py app.py
```

## Example

Input:

* You did an amazing job today

Output:

* Compliments (0.81)

```
::contentReference[oaicite:0]{index=0}
```
