import streamlit as st

st.set_page_config(
    page_title="Certifications",
    page_icon="🏆",
    layout="wide"
)

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("🏆 Certifications")

st.write("")

c1,c2,c3 = st.columns(3)

with c1:

    st.markdown("""
<div class="card">

# 🐍 Python Programming

Completed Python Programming Course

⭐ Beginner to Intermediate

</div>
""",unsafe_allow_html=True)

with c2:

    st.markdown("""
<div class="card">

# 🗄 SQL

Database Management

MySQL

SQL Server

</div>
""",unsafe_allow_html=True)

with c3:

    st.markdown("""
<div class="card">

# 📊 Power BI

Dashboard Development

Data Visualization

</div>
""",unsafe_allow_html=True)

st.write("")

c4,c5,c6 = st.columns(3)

with c4:

    st.markdown("""
<div class="card">

# 🤖 Machine Learning

Regression

Classification

Prediction

</div>
""",unsafe_allow_html=True)

with c5:

    st.markdown("""
<div class="card">

# 💻 Streamlit

Interactive Python Web Apps

Portfolio Development

</div>
""",unsafe_allow_html=True)

with c6:

    st.markdown("""
<div class="card">

# ☁ Git & GitHub

Version Control

Collaboration

</div>
""",unsafe_allow_html=True)