import streamlit as st

st.set_page_config(page_title="Skills", page_icon="💻", layout="wide")

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("💻 Technical Skills")

st.write("")

# Programming Languages
st.header("Programming Languages")

c1, c2 = st.columns(2)

with c1:

    st.write("Python")
    st.progress(90)

    st.write("SQL")
    st.progress(85)

    st.write("Java")
    st.progress(70)

    st.write("C")
    st.progress(65)

with c2:

    st.write("HTML")
    st.progress(80)

    st.write("CSS")
    st.progress(75)

    st.write("JavaScript")
    st.progress(60)

    st.write("Git")
    st.progress(75)

st.write("---")

# Libraries

st.header("Python Libraries")

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("""
<div class='card'>

### 🐼 Pandas

✔ Data Cleaning

✔ Data Analysis

</div>
""", unsafe_allow_html=True)

with col2:

    st.markdown("""
<div class='card'>

### 🔢 NumPy

✔ Arrays

✔ Mathematical Operations

</div>
""", unsafe_allow_html=True)

with col3:

    st.markdown("""
<div class='card'>

### 📊 Matplotlib

✔ Charts

✔ Data Visualization

</div>
""", unsafe_allow_html=True)

st.write("---")

# Tools

st.header("Tools & Technologies")

tool1, tool2, tool3, tool4 = st.columns(4)

tool1.metric("Power BI", "⭐⭐⭐⭐")
tool2.metric("Excel", "⭐⭐⭐⭐")
tool3.metric("MySQL", "⭐⭐⭐⭐")
tool4.metric("Streamlit", "⭐⭐⭐⭐⭐")