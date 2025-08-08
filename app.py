from flask import Flask, request, render_template_string
import pickle

# Load the trained model and vectorizer
with open("model.pkl", "rb") as f:
    model = pickle.load(f)
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>TruePoint</title>
    <link href="https://fonts.googleapis.com/css2?family=Nunito&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Nunito', sans-serif;
            background: #f7f0ff;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            background: #fff;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 600px;
            text-align: center;
        }
        h1 {
            color: #7a42f4;
            margin-bottom: 20px;
            font-size: 32px;
        }
        textarea {
            width: 100%;
            height: 150px;
            padding: 15px;
            border: 2px solid #e0d9f8;
            border-radius: 10px;
            font-size: 16px;
            background: #faf7ff;
            resize: none;
        }
        button {
            margin-top: 20px;
            padding: 12px 24px;
            font-size: 16px;
            background: #a98ef8;
            color: white;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            transition: background 0.3s;
        }
        button:hover {
            background: #8c71d8;
        }
        #result {
            margin-top: 25px;
            font-size: 18px;
            font-weight: bold;
            color: #333;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📰 TruePoint</h1>
        <form method="POST" action="/">
            <textarea name="text" placeholder="Paste news content here..."></textarea><br>
            <button type="submit">Check News</button>
        </form>
        {% if prediction %}
        <div id="result">
            Prediction: {{ prediction }} <br>
            Confidence: {{ confidence }}%
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("text", "")
        if not text.strip():
            return render_template_string(HTML_PAGE, prediction="No input", confidence="0")
        X = vectorizer.transform([text])
        pred = model.predict(X)[0]
        prob = model.predict_proba(X)[0][pred]
        label = "Real" if pred == 1 else "Fake"
        return render_template_string(HTML_PAGE, prediction=label, confidence=round(float(prob) * 100, 2))
    return render_template_string(HTML_PAGE)

if __name__ == "__main__":
    app.run(debug=True)
