# 🧠 Model Card: Music Recommender + RAG System

## 📌 Model Overview
This project combines two components:
1. A Music Recommender System based on user preferences  
2. A Retrieval-Augmented Generation (RAG) system that answers questions using stored text data  

Instead of generating answers from scratch, the RAG system retrieves relevant information from a dataset and uses it to produce responses.

---

## 🎯 Intended Use

This system is designed to:
- Recommend songs based on user preferences (energy, mood, tempo, etc.)
- Answer user questions using stored notes (notes.txt)
- Demonstrate how retrieval-based AI improves accuracy

---

## ⚙️ How It Works

### Recommender System:
- Takes user preferences (e.g., energy, valence)
- Computes similarity between songs and user profile
- Ranks songs and returns top matches

### RAG System:
1. Load text from notes.txt
2. Split into smaller chunks
3. Convert chunks into embeddings
4. Store in FAISS vector database
5. Retrieve relevant chunks based on user query
6. Return matching information as response

---

## 📊 Data

### Sources:
- songs.csv → Song features dataset  
- notes.txt → Text data used for RAG  

### Features Used:
- Energy
- Valence
- Danceability
- Acousticness
- Tempo

---

## 📈 Evaluation

### Recommender:
- Checked if recommended songs match user preferences
- Compared results with expected outcomes

### RAG System:
- Tested multiple queries
- Verified that retrieved text matches the question
- Confirmed consistent outputs for similar queries

---

## ⚠️ Limitations

- RAG system only works with local text data
- No external knowledge beyond notes.txt
- No advanced language generation (no API used)
- Small dataset limits accuracy and variety
- Recommender may oversimplify user preferences

---

## ⚖️ Ethical Considerations

- Recommendations may reflect bias in dataset
- Limited diversity in small datasets
- No personalization beyond defined features
- Users should not rely on system for critical decisions

---

## 🔮 Future Improvements

- Integrate OpenAI or HuggingFace models for better responses
- Expand dataset for more accurate retrieval
- Add user feedback loop to improve recommendations
- Build UI (Streamlit or web app)
- Improve ranking algorithm with machine learning

---

## 🧠 Key Takeaways

This project demonstrates:
- How RAG improves reliability by grounding answers in real data
- The importance of data quality in AI systems
- The trade-off between simplicity vs performance

-