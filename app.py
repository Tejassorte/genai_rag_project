from flask import Flask, render_template, request, jsonify
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.llms import HuggingFaceHub
import os

# Initialize Flask app
app = Flask(__name__)
UPLOAD_FOLDER = 'documents'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure necessary folders exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs("vectorstore", exist_ok=True)

# Global vector store
vectorstore = None


# ---- PDF Processing ----
def process_pdf(file_path):
    """Loads, splits, and creates vector embeddings from a PDF."""
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    # Split text into manageable chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    chunks = text_splitter.split_documents(documents)

    # Use local, free HuggingFace embeddings
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Create and persist vector store
    vector_db = Chroma.from_documents(chunks, embeddings, persist_directory="vectorstore/")
    vector_db.persist()
    return vector_db


@app.route('/')
def index():
    """Render the frontend."""
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_pdf():
    """Handles PDF upload and processing."""
    if 'pdf' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    pdf = request.files['pdf']
    filename = pdf.filename

    if not filename.lower().endswith('.pdf'):
        return jsonify({"error": "Only PDF files are allowed"}), 400

    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    pdf.save(path)

    try:
        global vectorstore
        vectorstore = process_pdf(path)
        return jsonify({"message": "✅ PDF processed successfully!"})
    except Exception as e:
        return jsonify({"error": f"Failed to process PDF: {e}"}), 500


@app.route('/ask', methods=['POST'])
def ask_question():
    """Handles user question and generates an answer."""
    global vectorstore
    if vectorstore is None:
        return jsonify({"error": "⚠️ No PDF uploaded yet. Please upload first."}), 400

    data = request.get_json()
    question = data.get('question')
    if not question:
        return jsonify({"error": "Please enter a question."}), 400

    try:
        # Retrieve relevant chunks
        docs = vectorstore.similarity_search(question, k=3)
        context = "\n\n".join([doc.page_content for doc in docs])

        # Simple QA logic — rule-based (no paid LLM)
        if not context.strip():
            return jsonify({"answer": "I could not find the answer in the document."})

        answer = f"Based on the document, here's what I found:\n\n{context[:800]}..."
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": f"Error while answering: {e}"}), 500


if __name__ == "__main__":
    app.run(debug=True)
