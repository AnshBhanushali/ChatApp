from transformers import pipeline
import spacy
from googletrans import Translator
import openai
import os

# load NLP models
nlp = spacy.load("en_core_web_sm")
sentiment_analyzer = pipeline("sentiment-analysis")
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


