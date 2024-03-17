from flask import Flask, request, render_template, jsonify, Response
from werkzeug.utils import secure_filename
from pdf_processor import process_pdf_query

app = Flask(__name__)

@app.route('/flaskapp', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({"error": "No file in the request"}), 400

        file = request.files['file']

        if file.filename == '':
            return jsonify({"error":"No selected file"}), 400

        filename = secure_filename(file.filename)
        file.save(filename)

        question = request.form['question']
        response = process_pdf_query(filename, question)

        return render_template('upload.html', response=response)

    return render_template('upload.html')

@app.route('/test', methods=['GET','POST'])
def test():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({"error": "No file in the request"}), 400

        file = request.files['file']

        if file.filename == '':
            return jsonify({"error":"No selected file"}), 400

        filename = secure_filename(file.filename)
        file.save(filename)

        question = request.form['question']
        response = process_pdf_query(filename, question)

        return render_template('index.html', response=response)

    return render_template('test.html')


@app.route('/bootstrap', methods=['GET','POST'])
def bootstrap():
    response = request.get('http://localhost:5173/message_api/')

    return render_template('index.html', data=response.json())

if __name__ == '__main__':
        app.run(debug=True, port=8081, host='0.0.0.0')

