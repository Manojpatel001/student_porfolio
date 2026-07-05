import streamlit as st

st.set_page_config(
    page_title="Resume",
    page_icon="📄",
    layout="wide"
)

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("📄 Resume")

st.write("")

st.success("Download my latest resume below.")

with open("assets/Resume.pdf","rb") as pdf:

    st.download_button(

        label="⬇ Download Resume",

        data=pdf,

        file_name="Manoj_Kumar_Resume.pdf",

        mime="application/pdf",

        use_container_width=True

    )

st.write("---")

st.header("Resume Highlights")

c1,c2 = st.columns(2)

with c1:

    st.info("""
✔ Python

✔ SQL

✔ Power BI

✔ Excel

✔ Machine Learning

✔ Streamlit
""")

with c2:

    st.success("""
✔ Data Analytics

✔ Dashboard Development

✔ Business Intelligence

✔ GitHub

✔ Team Player

✔ Problem Solving
""")