from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            features = [float(x) for x in request.form.values()]
            final_input = np.array([features])
            prediction = model.predict(final_input)[0]
            return render_template('index.html', prediction_text=f'Estimated House Price: ${prediction:.2f}')
        except:
            return render_template('index.html', prediction_text='Please enter valid inputs.')

if __name__ == "__main__":
    app.run(debug=True)
