import streamlit as st
from PIL import Image

# ---------------- Page Configuration ----------------

st.set_page_config(
    page_title="Manoj Kumar Portfolio",
    page_icon="👨‍💻",
    layout="wide"
)

# ---------------- Load CSS ----------------

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# ---------------- Sidebar ----------------

st.sidebar.title("👨‍💻 Manoj Kumar")

st.sidebar.info("""
Welcome to my Portfolio

📊 Data Analyst

🐍 Python Developer

🤖 AI Enthusiast
""")

st.sidebar.success("Use the navigation menu to explore my portfolio.")

# ---------------- Hero Section ----------------

col1, col2 = st.columns([1,2])

with col1:
    image = Image.open("assets/img1.jpeg")
    st.image(image, width=280)

with col2:

    st.markdown("<h1 class='title'>Manoj Kumar</h1>", unsafe_allow_html=True)

    st.markdown(
        "<h3 class='subtitle'>Data Analyst | Python Developer | Gen AI Enthusiast</h3>",
        unsafe_allow_html=True
    )

    st.write("")

    st.write("""
I am passionate about transforming data into meaningful insights.

Currently learning:

✔ Python

✔ SQL

✔ Power BI

✔ Machine Learning

✔ Deep Learning

✔ Streamlit

✔ Git & GitHub

My goal is to become a professional Data Analyst and AI Engineer.
""")

    c1,c2,c3,c4 = st.columns(4)

    c1.metric("Projects","10+")
    c2.metric("Skills","15+")
    c3.metric("CGPA","9.09")
    c4.metric("Experience","Fresher")

st.write("---")

# ---------------- Buttons ----------------

st.subheader("Quick Links")

b1,b2,b3,b4 = st.columns(4)

with b1:
    st.link_button(
        "🐙 GitHub",
        "https://github.com/manojpatel001"
    )

with b2:
    st.link_button(
        "💼 LinkedIn",
        "https://www.linkedin.com/in/manoj-kumar-ab829b311/"
    )

with b3:
    st.link_button(
        "📧 Email",
        "mailto:patelmanoj40612@gmail.com"
    )

with b4:

    with open("assets/Resume.pdf","rb") as pdf:

        st.download_button(
            "⬇ Download Resume",
            pdf,
            file_name="Resume.pdf",
            mime="application/pdf"
        )

st.write("---")

# ---------------- Skills ----------------

st.header("💻 Technical Skills")

skill1,skill2 = st.columns(2)

with skill1:

    st.write("Python")
    st.progress(90)

    st.write("SQL")
    st.progress(85)

    st.write("Power BI")
    st.progress(80)

    st.write("Excel")
    st.progress(90)

with skill2:

    st.write("Machine Learning")
    st.progress(70)

    st.write("Deep Learning")
    st.progress(60)

    st.write("Streamlit")
    st.progress(85)

    st.write("Git & GitHub")
    st.progress(75)

st.write("---")

# ---------------- Featured Projects ----------------

st.header("🚀 Featured Projects")

project1,project2 = st.columns(2)

with project1:

    st.markdown("""
<div class="card">

<h2>Blood Donation Management System</h2>

Built using

✔ React

✔ Spring Boot

✔ MongoDB

✔ Bootstrap

</div>
""",unsafe_allow_html=True)

with project2:

    st.markdown("""
<div class="card">

<h2>Student Portfolio Website</h2>

Built using

✔ Python

✔ Streamlit

✔ CSS

✔ GitHub

</div>
""",unsafe_allow_html=True)

st.write("---")

# ---------------- About ----------------

st.header("👨 About Me")

st.write("""
I recently completed my B.Tech in Computer Science Engineering.

I enjoy solving business problems using Python, SQL, and Power BI.

Currently, I am building Data Analytics and AI projects to strengthen my portfolio and prepare for software industry roles.
""")

st.write("---")

# ---------------- Footer ----------------

st.markdown("""
<div class="footer">

Made with ❤️ using Python & Streamlit

<br>

© 2026 Manoj Kumar

</div>
""",unsafe_allow_html=True)