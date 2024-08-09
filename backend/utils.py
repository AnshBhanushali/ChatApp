from transformers import pipeline
import spacy
from googletrans import Translator
import openai
import os

# load NLP models
nlp = spacy.load("en_core_web_sm")
sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english", device=0)
translator = Translator()

openai.api_key = os.getenv("OPENAI_API_KEY")

# this functionality will translate all any language
def translate_message(message, target_language='en'):
    translated = translator.translate(message, dest=target_language)
    return translated.text

# this functionality will analyze sentiment of the user for better response
def analyze_sentiment(message):
    sentiment = sentiment_analyzer(message)[0]
    return sentiment['label']

def generate_ai_response(message):
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=message,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )

        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error generating AI response: {str(e)}"


