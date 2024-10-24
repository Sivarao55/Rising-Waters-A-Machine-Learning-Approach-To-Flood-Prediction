from flask import Flask, request, render_template
import pickle


# Load your model
#from joblib import load

#model = load('floodpredicition.pkl')

model = pickle.load(open('floodpredicition.pkl', 'rb'))
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract and convert the input data
    temp = float(request.form['temp'])
    humd = float(request.form['humidity'])
    cloud_cover = float(request.form['cloud_cover'])
    annual = float(request.form['annual'])
    jan_feb = float(request.form['jan_feb'])
    mar_may = float(request.form['mar_may'])
    jun_sep = float(request.form['jun_sep'])
    oct_dec = float(request.form['oct_dec'])
    avg_june = float(request.form['avg_june'])
    sub = float(request.form['sub'])

    # Prepare the input for the model
    x = [[temp, humd, cloud_cover, annual, jan_feb, mar_may, jun_sep, oct_dec, avg_june, sub]]
    
    # Make a prediction
    y = model.predict(x)[0]
    if y == 1:
        pred = "Warning: Flood can occur in your area. Please take necessary precautions"

    else:
        pred = "No flood is expected, but please remain alert and vigilant.!"

    #return render_template('predict.html', Prediction=pred)


    
    # Render the prediction result
    return render_template('predict.html', Prediction=pred)

if __name__ == '_main_':
    app.run(debug=True)