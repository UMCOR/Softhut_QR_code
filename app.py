from flask import Flask, render_template
from flask import *
import pyqrcode
from random import randint

app = Flask(__name__)


@app.route('/QR_Code_Generater')
def home():
    return render_template('index.html')


@app.route('/converted', methods=['POST'])
def convert():
    global tex
    tex = request.form['test']
    return render_template('converted.html')


@app.route('/download')
def download():
    qrgen(tex)
    global filename
    filename = "qrcode" + numst + '.png'
    return send_file(filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)


def qrgen(s):
    qr = pyqrcode.create(s)
    global numst
    numst = str(randint(0, 100))
    qr.png("qrcode" + numst + '.png', scale=8)


