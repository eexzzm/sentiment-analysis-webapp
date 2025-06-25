from flask import Flask, render_template

app = Flask(__name__, template_folder='../frontend/templates')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predict")
def predict():
    return 'lets predict!'

if __name__ == '__main__':
    app.run(debug=True)