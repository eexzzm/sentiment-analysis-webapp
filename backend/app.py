from flask import Flask, render_template, request, send_file
import pandas as pd
from predict import predict_sentiment
import os
from werkzeug.utils import secure_filename

app = Flask(__name__, template_folder='../frontend/templates')
UPLOAD_FOLDER = os.path.join('uploads') # Absolute upload folder

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    file = request.files['file']
    filename = secure_filename(file.filename) # sanitize filename for safety
    column_name = request.form.get('column_name', '').strip()
    column_name = column_name.lower()
    
    # Handling all excel format
    try:
        if filename.endswith('.csv'):
            df = pd.read_csv(file)
        elif filename.endswith('.xls') or filename.endswith('.xlsx'):
            df = pd.read_excel(file)
        else:
            return 'Unsupported file format', 400
    except Exception as e:
        return f"Failed to read file: {str(e)}", 400
    
    df.columns = df.columns.str.lower()

    if column_name not in df.columns:
        return f"Column '{column_name}' not found in the file", 400
    
    text_list = df[column_name].astype(str).to_list() # Ensures no weird values such NaN
    predictions = predict_sentiment(text_list)
    df['Predicted Sentiment'] = predictions
    
    # Ensure output folder exists
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    
    result_filename = filename.rsplit('.', 1)[0] + '_predicted.csv'
    output_path = os.path.join(UPLOAD_FOLDER, result_filename)
    print(f"Saving prediction to: {output_path}") # DEBUG
    df.to_csv(output_path, index=False)

    return render_template('download.html', result_filename=result_filename)

@app.route('/download/<filename>')
def download_file(filename):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    print(f"donwloading file from: {file_path}")
    return send_file(file_path, as_attachment=True, mimetype='text/csv')

if __name__ == '__main__':
    app.run(debug=True)