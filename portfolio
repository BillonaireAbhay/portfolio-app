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
with tabs[0]:
    st.header("🎬 Project Demo Videos")
    video_dir = "assets/videos"
    if os.path.exists(video_dir):
        video_files = sorted([f for f in os.listdir(video_dir) if f.endswith(".mp4")])

        for idx, video in enumerate(video_files):
            st.markdown(f"## 🎯 Project {idx + 1}")
            col1, col2 = st.columns([1, 2])
            with col1:
                st.markdown("""<p style='color:gray;'>Short description about the project goes here. Explain what it does and any tech stack used.</p>""", unsafe_allow_html=True)
            with col2:
                st.video(os.path.join(video_dir, video))

            if idx % 2 == 1:
                try:
                    lottie = load_lottie("assets/animation.json")
                    st_lottie(lottie, speed=1, width=700)
                except:
                    pass
            st.markdown("---")
    else:
        st.warning("Video folder not found. Please ensure 'assets/videos' exists.")

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
<center style='color:#444;'>Made with ❤️ by <strong>[Your Name]</strong></center>
""", unsafe_allow_html=True)
