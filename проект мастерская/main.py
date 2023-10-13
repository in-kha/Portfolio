import catboost as cb
import pandas as pd


from flask import Flask, jsonify, request

# Load the model
model = cb.CatBoostClassifier()
model.load_model("catboost_model.cbm")

# Init the app
app = Flask("default")


# Setup prediction endpoint
@app.route("/predict", methods=["POST"])
def predict():
    # Get the provided JSON
    x = request.get_json()
    # Perform a prediction
    preds = model.predict_proba(pd.DataFrame(x, index=[0]))[0, 1]
    # Output json with prediction
    result = {"default_proba": preds}
    return jsonify(result)


if __name__ == "__main__":
    # Run the app on local host and port 8989
    app.run(debug=True, host='127.0.0.1', port=8989)
