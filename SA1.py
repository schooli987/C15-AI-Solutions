from flask import Flask,render_template

import pytesseract


app = Flask(__name__)

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

@app.route("/", methods=["GET", "POST"])
def index():
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
