# 🧾 Streamlit Tax Chatbot – Korean Income Tax Law (소득세법 RAG Application)

## 🧠 Overview
This project implements a **Retrieval-Augmented Generation (RAG)** chatbot using **LangChain** and **Streamlit**.  
It provides **context-aware answers** and **legal insights** based on the **South Korean Income Tax Law (소득세법)**.  
By combining **document retrieval**, **few-shot learning templates**, and **conversational history**, the system enhances accuracy, consistency, and reliability in responses.

---

## 🚀 Features
- **LangChain Integration:** Manages prompt orchestration, context retrieval, and model interaction seamlessly.  
- **Streamlit Interface:** Simple and interactive UI for real-time chatbot conversations.  
- **Retrieval-Augmented Generation (RAG):** Combines retrieval-based reasoning with generative modeling for factual responses.  
- **Knowledge Base:** Built around the **Korean Income Tax Law (소득세법)** to provide domain-specific expertise.  
- **Chat History Memory:** Maintains dialogue history for contextually coherent, multi-turn interactions.  
- **Few-Shot Learning Templates:** Improves model reliability through structured example-based prompting.  

---

## 🧰 Tech Stack
- **Language Model Framework:** LangChain  
- **Frontend:** Streamlit  
- **Vector Store:** Chroma / Pinecone  
- **Embedding Model:** OpenAI Embeddings (`text-embedding-3-large`)  
- **Environment Management:** Python-dotenv  
- **Prompt Design:** Few-shot learning templates + conversational memory  

---

## ⚙️ How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/tax-chatbot.git
   cd tax-chatbot

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt

3. **Set environment variables**  
   Create a `.env` file in the project root and add your API key:
   ```bash
   OPENAI_API_KEY=your_openai_api_key

4. **Run the Streamlit app**
   ```bash
   streamlit run chat.py

5. **Open the app in your browser**
   ```bash
   http://localhost:8501

---

## 💡 Example Query
> “연봉 5천만원인 직장인의 소득세는 얼마인가요?”

> 'How much tax for a $50K salary?'

> The chatbot retrieves relevant tax clauses, interprets them contextually, and generates an answer grounded in the South Korean Income Tax Law.

---

## 📊 Future Improvements
- Expand retrieval scope to include enforcement decrees and administrative rulings  
- Add feedback and evaluation loop for model refinement  
- Integrate bilingual support (Korean ↔ English)  
- Containerize the application with Docker for deployment  

---

## 👩‍💻 Author
**Wonha (Leah) Shin**  
📍 [Portfolio](https://leahnote01.github.io/) • [GitHub](https://github.com/leahnote01) • [LinkedIn](https://linkedin.com/in/wshin7)
