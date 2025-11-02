# 🧠 GenAI RAG PDF Assistant

> 📚 **Chat with your PDFs — Powered by Flask, LangChain, and AI**

GenAI RAG PDF Assistant is a **Retrieval-Augmented Generation (RAG)** web application that lets users **upload PDF files** and **ask AI-driven questions** about their content.
It uses embeddings and vector search to find relevant information — delivering precise and context-based answers.

---

## ✨ Key Highlights

✅ **Upload & Process PDFs** – Supports any document type in `.pdf` format
✅ **Retrieval-Augmented Generation (RAG)** – AI searches within your PDF, not the internet
✅ **Context-Aware Answers** – Powered by **LangChain + OpenAI/HuggingFace**
✅ **Local Vector Store** – Uses **ChromaDB** to store and retrieve embeddings
✅ **Interactive UI** – Simple, clean, and responsive frontend
✅ **Runs Locally** – Full control over your data; no cloud dependencies

---

## 🧰 Tech Stack

| Layer                  | Technology                       |
| ---------------------- | -------------------------------- |
| **Backend**            | Flask (Python)                   |
| **AI / LLM**           | LangChain + OpenAI / HuggingFace |
| **Vector Store**       | Chroma                           |
| **Frontend**           | HTML5, CSS3, JavaScript          |
| **Environment Config** | dotenv (`.env`)                  |

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/genai_rag_project.git
cd genai_rag_project
```

### 2️⃣ Create and Activate a Virtual Environment

#### 🪟 On Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### 🐧 On macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add API Key (if using OpenAI)

Create a file named `.env` in the project root:

```
OPENAI_API_KEY=your_api_key_here
```

Get your key from 👉 [OpenAI Platform](https://platform.openai.com/)

---

## ▶️ Running the App

```bash
python app.py
```

Then open your browser and visit:
👉 **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

Upload a PDF → ask a question → and watch the AI respond. 🤖💬

---

## 📁 Folder Structure

```
genai_rag_project/
│
├── app.py                  # Flask backend
├── .env                    # API key
├── requirements.txt         # Dependencies
├── .gitignore              # Ignore config
│
├── templates/
│   └── index.html          # Frontend (UI)
│
├── static/
│   └── style.css           # CSS Styling
│
├── documents/              # Uploaded PDFs
└── vectorstore/            # Chroma vector DB
```

---

## 🧠 How It Works

1. User uploads a **PDF**.
2. The system extracts and splits text into small chunks.
3. Each chunk is **embedded** into a vector using **OpenAI / HuggingFace embeddings**.
4. The vectors are stored in **ChromaDB**.
5. When a question is asked, the app retrieves the **most relevant text chunks**.
6. The AI generates a precise answer from the retrieved content.

---

## 🧩 Example Commands

Rebuild your vector store:

```bash
rm -rf vectorstore/
python app.py
```

Deactivate virtual environment:

```bash
deactivate
```

Push to GitHub:

```bash
git add .
git commit -m "Add project and README"
git push -u origin main
```

---

## 🪄 Sample Questions You Can Ask

Once your PDF is uploaded, try:

* “Summarize the document in 3 lines.”
* “What is the main idea discussed on page 2?”
* “List all key points about the topic.”
* “Who are the authors mentioned?”
* “Explain the process described in section 3.”

---

## 📸 (Optional) Screenshot Placeholder

You can include a screenshot of your app’s UI:

```
![App Screenshot](./static/preview.png)
```

---

## 👨‍💻 Author

**Tejas Sorte**
🎓 Student Development Faculty Trainee
📍 India
💼 [GitHub](https://github.com/Tejassorte) • [LinkedIn](https://www.linkedin.com/notifications/?filter=all)

---

## 🪪 License

This project is open-source and licensed under the **MIT License** — free to use and modify.

---

⭐ **If you find this project useful, give it a star on GitHub!**



