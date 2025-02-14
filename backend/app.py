from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import docx
import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from models import db, Upload
from openai import OpenAI

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///uploads.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


OPENAI_API_KEY = "YOUR API KEY HERE"
client = OpenAI(api_key=OPENAI_API_KEY)

db.init_app(app)

ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def read_file(file_path):
    text = ""
    if file_path.endswith('.doc') or file_path.endswith('.docx'):
        doc = docx.Document(file_path)
        for para in doc.paragraphs:
            text += para.text
    elif file_path.endswith('.pdf'):
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text()
    return text


def get_resume_feedback(resume_text):

    prompt = f"Evaluate the following resume and provide suggestions for improvement:\n\n{resume_text}"
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "developer", "content": "You are a resume review expert."},
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return completion.choices[0].message.content


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'resume' not in request.files or 'jobDescription' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    resume = request.files['resume']
    job_description = request.files['jobDescription']

    if resume.filename == '' or job_description.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if resume and allowed_file(resume.filename) and job_description and allowed_file(job_description.filename):
        resume_filename = secure_filename(resume.filename)
        job_description_filename = secure_filename(job_description.filename)
        resume_path = os.path.join(app.config['UPLOAD_FOLDER'], resume_filename)
        job_description_path = os.path.join(app.config['UPLOAD_FOLDER'], job_description_filename)
        resume.save(resume_path)
        job_description.save(job_description_path)

        resume_text = read_file(resume_path)
        job_description_text = read_file(job_description_path)

        vectorizer = TfidfVectorizer().fit_transform([resume_text, job_description_text])
        vectors = vectorizer.toarray()
        cosine_sim = cosine_similarity(vectors)
        score = cosine_sim[0][1] * 100

        suggestions = get_resume_feedback(resume_text)

        return jsonify({'score': score, 'suggestions': suggestions})

    return jsonify({'error': 'File type not allowed'}), 400

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    with app.app_context():
        db.create_all()
    app.run(debug=True)