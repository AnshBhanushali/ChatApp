from transformers import pipeline
import spacy
from googletrans import Translator
import openai
import os

# Load NLP models
nlp = spacy.load("en_core_web_sm")
sentiment_analyzer = pipeline("sentiment-analysis")
translator = Translator()

openai.api_key = os.getenv("OPENAI_API_KEY")