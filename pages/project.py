import streamlit as st

st.set_page_config(page_title="Projects", page_icon="🚀", layout="wide")

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("🚀 My Projects")

st.write("")

project1, project2 = st.columns(2)

with project1:

    st.image("assets/project1.png")

    st.markdown("""
<div class='card'>

## Blood Donation Management System

### Technologies

✔ React

✔ Spring Boot

✔ MongoDB

✔ Bootstrap

A complete blood donation platform connecting donors, hospitals and receivers.

</div>
""", unsafe_allow_html=True)

    st.link_button(
        "🐙 View GitHub",
        "https://github.com/manojpatel001"
    )

with project2:

    st.image("assets/project1.png")

    st.markdown("""
<div class='card'>

## Student Portfolio

### Technologies

✔ Python

✔ Streamlit

✔ CSS

✔ GitHub

A professional portfolio website built completely using Streamlit.

</div>
""", unsafe_allow_html=True)

    st.link_button(
        "🌐 Live Demo",
        "https://yourwebsite.com"
    )

st.write("---")

st.header("Upcoming Projects")

c1, c2, c3 = st.columns(3)

with c1:

    st.markdown("""
<div class='card'>

### 🤖 AI Chatbot

Python

OpenAI

Streamlit

</div>
""", unsafe_allow_html=True)

with c2:

    st.markdown("""
<div class='card'>

### 📊 Sales Dashboard

Power BI

SQL

Excel

</div>
""", unsafe_allow_html=True)

with c3:

    st.markdown("""
<div class='card'>

### 🧠 Resume Analyzer

Python

NLP

Machine Learning

</div>
""", unsafe_allow_html=True)