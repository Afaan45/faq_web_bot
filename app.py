from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load FAQ data
with open("faq.json", "r", encoding="utf-8") as f:
    faq_data = json.load(f)

def get_bot_response(user_input):
    user_input = user_input.lower()
    for key, value in faq_data.items():
        for phrase in value["synonyms"]:
            if phrase in user_input:
                return value["response"]
    return "🤖 I'm sorry, I don't understand that question."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_input = request.form["msg"]
    response = get_bot_response(user_input)
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)
