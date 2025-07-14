# Sentiment Analysis Web App
A prototype Flask web application for performing sentiment analysis on uploaded CSV data.

# About The Project
This project delivers a functional web application built with Flask that performs sentiment analysis. It allows users to upload a CSV file containing textual data, specify the column to be analyzed, and then receive predictions on the sentiment of each text entry. The core functionality leverages a Machine Learning model (specifically, a Multinomial Naive Bayes classifier trained on TF-IDF features) to classify sentiment, demonstrating a complete pipeline from data input to model inference and result output within a web environment.

# Features
- **CSV Upload**: Easily upload .csv or Excel files (.xlsx, .xls) containing your textual data.
- **Column Selection**: Specify which text column from your uploaded CSV should be used for sentiment prediction.
- **Machine Learning Powered Sentiment Prediction**: Utilizes a pre-trained Machine Learning model to classify the sentiment of the text.
- **Downloadable Results**: Receive a downloadable CSV file that includes your original data along with a new column containing the predicted sentiment labels.

# Getting started
To get a local copy up and running, follow these simple steps.

## Prerequisites
Ensure you have the following installed on your system:
- Python 3.10 or higher
- pip

## Instalation
- Clone the repository
```
https://github.com/eexzzm/sentiment-analysis-webapp
cd sentiment-analysis-webapp
```

- Create and activate a Python virtual environment
```
python -m venv venv
# For Windows:
.\venv\Scripts\activate
# For macOS/Linux:
source venv/bin/activate
```

- Install dependencies:
```
pip install -r backend/requirements.txt
```

- Run the flask application:
```
# Set the FLASK_APP environment variable (replace 'app.py' with your main Flask app file if different)
# For Windows PowerShell:
$env:FLASK_APP="app.py"
# For macOS/Linux Bash/Zsh:
export FLASK_APP=app.py

# Run the Flask development server
flask run
```