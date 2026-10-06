import streamlit as st
from pypdf import PdfReader

# Page configuration
st.set_page_config(
    page_title="LectureRecall",
    page_icon="🎓",
    layout="wide"
)

# Title
st.title("🎓 LectureRecall")
st.subheader("Searchable Lecture Memory")

st.write(
    "Upload your lecture notes and search for important topics quickly."
)

# Store uploaded lectures
if "lectures" not in st.session_state:
    st.session_state.lectures = {}

# Sidebar
st.sidebar.header("📚 Lecture Manager")

uploaded_file = st.sidebar.file_uploader(
    "Upload Lecture PDF",
    type=["pdf"]
)

# Read PDF
if uploaded_file is not None:

    if uploaded_file.name not in st.session_state.lectures:

        reader = PdfReader(uploaded_file)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        st.session_state.lectures[uploaded_file.name] = text

        st.sidebar.success("Lecture uploaded successfully!")

# Search section
st.markdown("---")

st.header("🔍 Search Your Lectures")

query = st.text_input(
    "Ask a question or enter a keyword:",
    placeholder="Example: What is inflation?"
)

# Search
if query:

    found = False

    for lecture_name, lecture_text in st.session_state.lectures.items():

        lines = lecture_text.split("\n")

        results = []

        for line in lines:

            if query.lower() in line.lower():
                results.append(line)

        if results:

            found = True

            st.subheader(f"📖 {lecture_name}")

            for result in results[:10]:
                st.info(result)

    if not found:
        st.warning("No matching information found.")

# Initial message
if not st.session_state.lectures:

    st.info(
        "👈 Upload a lecture PDF from the sidebar to start."
    )

# Footer
st.markdown("---")

st.caption(
    "LectureRecall 🎓 | Search, Recall, and Learn Smarter"
)