
from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = "https://platform.openai.com/account/api-keys"  # Replace this

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_question = data["question"]

    # Prompt to keep the AI focused on HDL Remote Control
    prompt = f"You are an expert AI assistant helping users understand HDL Remote Control systems. Answer only about AI-powered HDL Remote Control. User asked: {user_question}"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=300
        )
        answer = response["choices"][0]["message"]["content"].strip()
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"answer": f"Error: {str(e)}"})
        
if __name__ == "__main__":
    import os

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)

