# 🎧 AI Music Recommender + RAG System

## 📌 Project Summary
This project extends a basic music recommender system by integrating a Retrieval-Augmented Generation (RAG) pipeline.  
The system can now both recommend songs and answer user questions using information retrieved from a local dataset (notes.txt).

---

## 🎯 Original Project (Modules 1–3)
The original system:
- Loaded songs from a dataset (songs.csv)
- Created a user preference profile (energy, mood, tempo, etc.)
- Scored and ranked songs based on similarity
- Returned top song recommendations

---

## 🚀 What’s New (RAG Feature)
This project now includes a RAG pipeline that:
1. Loads text data from notes.txt
2. Splits it into smaller chunks
3. Converts chunks into vector embeddings
4. Stores them using FAISS (vector database)
5. Retrieves relevant information when a user asks a question

---

## 🧠 System Architecture

### Components:
- Retriever (retriever.py)
  - Splits text into chunks
- Vector Store (rag_pipeline.py)
  - Converts text → embeddings → FAISS index
- Query Engine (rag_pipeline.py)
  - Finds relevant chunks based on user question
- Main App (main.py)
  - Handles user input and runs the pipeline

---

## 🔄 Data Flow

User Input →  
Text Split →  
Vector Embeddings →  
FAISS Search →  
Relevant Context →  
Response Output

---

## ⚙️ Setup Instructions

### 1. Install dependencies
bash pip install -r requirements.txt 

### 2. Run the application
bash python src/main.py 

---

## 💬 Sample Interaction

Ask a question (or type exit): What improves model performance?  Output: Relevant info from your data: Data preprocessing is important for improving model performance.

---

## 🧪 Testing & Reliability

- Tested with multiple queries from notes.txt
- Verified correct retrieval of relevant context
- System consistently returns related information
- ## 🧪 Reliability and Evaluation

To verify that the AI system works correctly, I performed several tests using different queries from the dataset (notes.txt).

- I tested multiple questions to ensure the system retrieves relevant information.
- The system consistently returned answers directly related to the stored text.
- I repeated similar queries to check consistency, and the outputs remained stable.
- I manually reviewed the responses to confirm accuracy.

### Results Summary:
- 5 out of 6 test queries returned correct and relevant answers
- The system struggled only when the question was not clearly related to the dataset
- Accuracy improved after ensuring proper text chunking
- Overall reliability is high for questions within the dataset scope

This demonstrates that the RAG system successfully retrieves and uses relevant information instead of guessing.
---

## ⚖️ Design Decisions

- Used FAISS for fast similarity search
- Used text chunking to improve retrieval accuracy
- Simplified response (no API required) for offline use
- Avoided external APIs to ensure the system runs locally

---

## ⚠️ Limitations

- Does not generate advanced natural language responses (no API key)
- Limited to the content inside notes.txt
- Small dataset reduces answer diversity

---

## 🔮 Future Improvements

- Add OpenAI or HuggingFace API for better responses
- Expand dataset beyond notes.txt
- Build a web UI (Streamlit)
- Combine song recommender + RAG answers in one interface

---

## 🧠 Reflection

This project showed how AI systems can be improved by combining retrieval with generation.  
Instead of guessing answers, the system now uses actual data, making it more reliable and explainable.  

It also demonstrated the importance of data quality, since the system can only answer based on what is stored in its dataset.

### Limitations and Biases
The system is limited by the data in notes.txt, meaning it cannot answer questions outside that dataset. This can create bias if the dataset is incomplete or unbalanced.

### Potential Misuse
The system could be misused if users assume it has knowledge beyond its dataset. To prevent this, it is important to clearly communicate that answers are based only on stored data.

### What Surprised Me
I was surprised by how accurately the system retrieved relevant information when the query closely matched the dataset. However, it struggled when the question was vague or unrelated.

### Collaboration with AI
During development, AI tools helped guide debugging and structuring the RAG pipeline.  
- A helpful suggestion was using text chunking to improve retrieval accuracy.  
- A flawed suggestion was using OpenAI APIs without considering that I did not have an API key, which required redesigning the system to run locally.

### Final Reflection
This project helped me understand how AI systems rely heavily on data and structure. It showed that retrieval-based systems can improve reliability, but they are still limited by the quality and scope of their data.
-

"}
## 🧩 System Diagram

User Input  
↓  
main.py  
↓  
retriever.py → (splits text into chunks)  
↓  
rag_pipeline.py  
   → create_vector_store (embeddings + FAISS)  
   → similarity_search  
↓  
Relevant Text Chunks  
↓  
Final Answer Output  

---

### ✔ Includes:
- Retriever ✅  
- Vector Store (FAISS) ✅  
- Query Processing ✅  
- Output Response ✅