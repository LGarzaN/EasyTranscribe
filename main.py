from flask import Flask, render_template, request, redirect, url_for, jsonify
from word import word
import os
import gpt as g


app = Flask(__name__)

query = ""
msg = "Loading..."

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=["POST", "GET"])
def index():
    global query
    if request.method == "POST":
        uploaded_file = request.files['file']

        filename = uploaded_file.filename
        file_extension = os.path.splitext(filename)[1].lower()

        if file_extension == '.docx':
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
            uploaded_file.save(file_path)

            query = word(file_path)

            return redirect(url_for("chat"))

    return render_template("index.html")

@app.route("/chat", methods=["GET", "POST"])
def chat():
    global query, msg
    g.start()
    summary = "Loading..."
    if request.method == "POST":
        data = request.json.get("message")  # Access the message from the request
        summary = g.normal(data)
        
        return jsonify(response=summary)
    
    else:
        return render_template("Chat.html")
    
@app.route("/send_dict", methods=["GET"])
def send_dict():
    global query
    summary = g.normal(query)
    frequentWords = g.frequentWords(query)
    ideas = g.keyIdeas(query)

    dic = {
        "summary": summary,
        "words": frequentWords,
        "ideas": ideas
    }
    return jsonify(dic)


if __name__ == "__main__":
    app.run()