import streamlit as st
from data import questions_answers
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Questions list
questions = list(questions_answers.keys())

# Vectorizer
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(questions)

# Streamlit UI
st.title("🎓 College AI Chatbot")

st.write("Ask your college-related questions")

user_input = st.text_input("Enter your question")

if user_input:
    
    # Convert user question into vector
    user_vector = vectorizer.transform([user_input])
    
    # Similarity check
    similarity = cosine_similarity(user_vector, X)
    
    index = similarity.argmax()
    
    answer = questions_answers[questions[index]]
    
    st.success(answer)