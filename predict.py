import pickle

from flask import Flask
from flask import request
from flask import jsonify


model_file = 'model_C=1.0.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('churn')


@app.route('/predict', methods=['POST'])
def predict():

    # customer = {
    # 'customerid': '8879-zkjof',
    # 'gender': 'female',
    # 'seniorcitizen': 0,
    # 'partner': 'no',
    # 'dependents': 'no',
    # 'tenure': 41,
    # 'phoneservice': 'yes',
    # 'multiplelines': 'no',
    # 'internetservice': 'dsl',
    # 'onlinesecurity': 'yes',
    # 'onlinebackup': 'no',
    # 'deviceprotection': 'yes',
    # 'techsupport': 'yes',
    # 'streamingtv': 'yes',
    # 'streamingmovies': 'yes',
    # 'contract': 'one_year',
    # 'paperlessbilling': 'yes',
    # 'paymentmethod': 'bank_transfer_(automatic)',
    # 'monthlycharges': 79.85,
    # 'totalcharges': 3320.75,
    # }
    
    customer = request.get_json()

    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    churn = y_pred >= 0.5

    result = {
        'churn_probability': float(y_pred),
        'churn': bool(churn)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)