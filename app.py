from flask import Flask, render_template, request, jsonify
from src.model.model import rag_chain
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("chatbot.html")

@app.route("/get", methods=["POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    response = rag_chain.invoke({"input": msg})
    print(response["answer"])
    return str(response["answer"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)