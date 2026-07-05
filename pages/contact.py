import streamlit as st

st.set_page_config(
    page_title="Contact",
    page_icon="📞",
    layout="wide"
)

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("📞 Contact Me")

st.write("")

left,right = st.columns([1,1])

with left:

    st.header("Contact Information")

    st.write("📧 Email")
    st.write("patelmanoj40612@gmail.com")

    st.write("📱 Phone")
    st.write("+91 9676125895")

    st.write("📍 Location")
    st.write("Hyderabad, Telangana")

    st.write("")

    st.link_button(
        "🐙 GitHub",
        "https://github.com/manojpatel001",
        use_container_width=True
    )

    st.link_button(
        "💼 LinkedIn",
        "https://www.linkedin.com/in/manoj-kumar-ab829b311/",
        use_container_width=True
    )

with right:

    st.header("Send Message")

    name = st.text_input("Your Name")

    email = st.text_input("Email")

    subject = st.text_input("Subject")

    message = st.text_area("Message")

    if st.button("Send Message",use_container_width=True):

        st.success("Thank you! Your message has been received.")

        st.balloons()

st.write("---")

st.markdown("""
<div class="footer">

Made with ❤️ using Python & Streamlit

<br>

© 2026 Manoj Kumar

</div>
""",unsafe_allow_html=True)