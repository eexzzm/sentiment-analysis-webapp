import os
import joblib
from preprocessing import clean_text  # Import the cleaning function

MODEL_PATH = os.path.join(os.path.dirname(__file__), '../model/sentiment_pipeline.pkl')

model = joblib.load(MODEL_PATH)


def predict_sentiment(text_list):
    
    # Clean each tweet using the cleaning function
    cleaned_texts = [clean_text(text) for text in text_list]
    # Use the pipeline model to transform + predict
    predictions = model.predict(cleaned_texts)
    
    return predictions


# for prediction testing with hardcoded text  
# if __name__ == '__main__':
#     test_data = [
#         "Anies sangat bijak menjawab semuanya dengan tenang.",
#         "Pak Ahok itu kasar banget ngomongnya.",
#         "Wkwkwk ngaco banget ini debat 😅"
#     ]

#     preds = predict_sentiment(test_data)
#     for text, label in zip(test_data, preds):
#         print(f"{text} → Sentimen: {'Positif' if label == 1 else 'Negatif'}")