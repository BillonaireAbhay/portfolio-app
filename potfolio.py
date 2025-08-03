import streamlit as st
import os
from PIL import Image
from streamlit_lottie import st_lottie
import json

st.set_page_config(page_title="My AI/ML Portfolio", layout="wide")

# ---------- Load Animation ----------
def load_lottie(filepath):
    with open(filepath, "r") as f:
        return json.load(f)

# ---------- Background Styling ----------
def add_bg():
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(to right, #e0eafc, #cfdef3);
        }
        .title-wrapper {
            text-align: center;
            padding: 30px 0;
        }
        .stVideo {
            border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.15);
        }
        </style>
    """, unsafe_allow_html=True)

add_bg()

# ---------- Header ----------
st.markdown("""
<div class='title-wrapper'>
    <h1 style='font-size: 3rem;'>🚀 My AI/ML Project Portfolio</h1>
    <h4>Welcome! Explore my best <span style='color:#6c63ff'>project demos</span>, <span style='color:#6c63ff'>certificates</span>, and <span style='color:#6c63ff'>visual highlights</span>.</h4>
</div>
""", unsafe_allow_html=True)

# ---------- Tabs ----------
tabs = st.tabs(["🎥 Project Videos", "📸 Project Images", "📜 Certificates"])

# ---------- Project Videos Tab ----------
# ---------- Project Videos Tab ----------


# ----------- Custom CSS Styling -----------
st.markdown("""
<style>
.project-card {
    background-color: #f9f9f9;
    padding: 1.5rem;
    border-radius: 15px;
    margin-bottom: 25px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.08);
    transition: transform 0.3s ease;
}
.project-card:hover {
    transform: scale(1.02);
}
.project-title {
    font-size: 24px;
    font-weight: bold;
    color: #1f77b4;
}
.tech-badge {
    background-color: #e0f7fa;
    color: #00796b;
    padding: 4px 10px;
    margin: 2px;
    border-radius: 5px;
    font-size: 12px;
    display: inline-block;
}
</style>
""", unsafe_allow_html=True)

# ----------- Header Section with Lottie -----------

with tabs[0]:
    st.markdown("<h1 style='text-align:center;'>🚀 AI/ML Project Showcase</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:gray;'>Beautifully presented demos of my top projects in AI, Data Science & Automation.</p>", unsafe_allow_html=True)

    try:
        st_lottie(load_lottie("assets/animations/banner.json"), height=200)
    except:
        st.info("Banner animation missing...")

    video_dir = "assets/videos"
    if os.path.exists(video_dir):
        video_files = sorted([f for f in os.listdir(video_dir) if f.endswith(".mp4")])
        
        for idx, video in enumerate(video_files):
            with st.container():
                st.markdown('<div class="project-card">', unsafe_allow_html=True)
                
                col1, col2 = st.columns([1, 2])
                with col1:
                    st.markdown(f"<div class='project-title'>🎯 Project {idx + 1}</div>", unsafe_allow_html=True)
                    st.markdown("""
                        <p>This is a short description of the project.<br>
                        It tackles a real-world problem using Automataion by Gen Ai.<br><br>
                        <b>🔧 Tech Stack:</b><br>
                        <span class='tech-badge'>Python</span>
                        <span class='tech-badge'>Streamlit</span>
                        <span class='tech-badge'>TensorFlow</span>
                        <span class='tech-badge'>Pandas</span>
                        <span class='tech-badge'>N8N</span>
                        <span class='tech-badge'>Api</span>
                         <span class='tech-badge'>openAi</span>
                        </p>
                    """, unsafe_allow_html=True)
                    
                    st.link_button("🔗 GitHub", url="https://github.com/your_project", use_container_width=True)
                    st.link_button("🌐 Live Demo", url="https://yourliveproject.com", use_container_width=True)

                    # Add Lottie inside each block (optional)
                    try:
                        st_lottie(load_lottie("assets/animations/animation.json"), height=150, key=f"anim{idx}")
                    except:
                        pass

                with col2:
                    st.video(os.path.join(video_dir, video))

                st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.error("Video folder not found. Please ensure 'assets/videos' exists.")



# ---------- Project Images Tab ----------
with tabs[1]:
    st.header("🧠 AI/ML Project Snapshots")
    image_dir = "assets/images"
    if os.path.exists(image_dir):
        image_files = sorted([f for f in os.listdir(image_dir) if f.lower().endswith((".png", ".jpg", ".jpeg"))])

        for i in range(0, len(image_files), 2):
            col1, col2 = st.columns(2)
            with col1:
                if i < len(image_files):
                    img = Image.open(os.path.join(image_dir, image_files[i]))
                    st.image(img, caption=f"Project Image {i + 1}", use_column_width=True)
            with col2:
                if i+1 < len(image_files):
                    img = Image.open(os.path.join(image_dir, image_files[i+1]))
                    st.image(img, caption=f"Project Image {i + 2}", use_column_width=True)

        st.success("These visuals highlight key moments of my AI/ML work.")
    else:
        st.warning("Image folder not found. Please ensure 'assets/images' exists.")

# ---------- Certificates Tab ----------
with tabs[2]:
    st.header("📜 Certifications")
    cert_dir = "assets/certificates"
    if os.path.exists(cert_dir):
        cert_files = sorted([f for f in os.listdir(cert_dir) if f.lower().endswith((".png", ".jpg", ".jpeg", ".pdf"))])

        for cert in cert_files:
            col1, col2 = st.columns([3, 1])
            with col1:
                if cert.endswith(".pdf"):
                    st.markdown(f"[📄 {cert}](assets/certificates/{cert})", unsafe_allow_html=True)
                else:
                    image = Image.open(os.path.join(cert_dir, cert))
                    st.image(image, caption=cert, use_column_width=True)
            with col2:
                with open(os.path.join(cert_dir, cert), "rb") as file:
                    st.download_button(label="📥 Download", data=file.read(), file_name=cert)
            st.markdown("---")
    else:
        st.warning("Certificate folder not found. Please ensure 'assets/certificates' exists.")

# ---------- Footer ----------
st.markdown("---")
st.markdown("""
<center style='color:#444;'>Made with ❤️ by <strong>[Abhay Singh Rana]</strong></center>
""", unsafe_allow_html=True)
