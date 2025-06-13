import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="AIzaSyB6x_RY1HtmIbfk6RPRUAUcxVzlH-9EpaM")  # Keep your API key

# Function to generate resume content
def generate_resume(content, style, tone):
    prompt = f"Generate a {style} resume in a {tone} tone using these details:\n{content}"
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    return response.text

# Function to save text file
def save_text_file(text, filename):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(text)
        return True
    except Exception as e:
        st.error(f"❌ Failed to save text file: {e}")
        return False

# Streamlit UI
st.title("🧠 AI Resume Generator")

with st.form("resume_form"):
    st.subheader("Enter Your Details")
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    summary = st.text_area("Career Objective / Summary")
    skills = st.text_area("Skills (comma-separated)")
    education = st.text_area("Education Details")
    experience = st.text_area("Work Experience")
    projects = st.text_area("Projects / Certifications")

    style = st.selectbox("Resume Style", ["Professional", "Modern", "Creative"])
    tone = st.radio("Tone", ["Formal", "Confident", "Friendly"])

    submitted = st.form_submit_button("Generate Resume")

if submitted:
    user_input = f"""
Name: {name}
Email: {email}
Phone: {phone}
Summary: {summary}
Skills: {skills}
Education: {education}
Experience: {experience}
Projects: {projects}
"""
    output = generate_resume(user_input, style, tone)
    st.success("✅ Resume generated!")
    st.text_area("📝 Generated Resume", value=output, height=400)

    # Save as .txt file
    if save_text_file(output, "generated_resume.txt"):
        with open("generated_resume.txt", "rb") as f:
            st.download_button(
                label="📄 Download as TXT",
                data=f.read(),
                file_name="resume.txt",
                mime="text/plain"
            )
