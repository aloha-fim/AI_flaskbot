from flask import Flask, request, render_template, jsonify, Response, Blueprint
from werkzeug.utils import secure_filename
from flask_app.pdf_processor import process_pdf_query

core = Blueprint('core',__name__)

@core.route('/flaskapp', methods=['GET','POST'])
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

@core.route('/test', methods=['GET','POST'])
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


@core.route('/bootstrap', methods=['GET','POST'])
def bootstrap():

    return render_template('index.html')