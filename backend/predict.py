import os
import joblib
from .preprocessing import clean_text  # Import the cleaning function

MODEL_PATH = os.path.join(os.path.dirname(__file__), '../model/sentiment_pipeline.pkl')

model = joblib.load(MODEL_PATH)


def predict_sentiment(text_list):
    
    # Clean each tweet using the cleaning function
    cleaned_texts = [clean_text(text) for text in text_list]
    # Use the pipeline model to transform + predict
    predictions = model.predict(cleaned_texts)
    
    return predictions
    
