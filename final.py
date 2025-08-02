import streamlit as st
from gtts import gTTS
import tempfile
import os

# Topic data structure
topics = {
    "Photosynthesis": {
        "steps": [
            {
                "title": "Step 1: Sunlight Reaches Leaf",
                "text": "Photosynthesis begins when sunlight hits the leaf surface.",
                "image": "images/step1.jpg",
                "video_url": "https://www.youtube.com/embed/eo5XndJaz-Y"
            },
            {
                "title": "Step 2: Chlorophyll Absorbs Light",
                "text": "Chlorophyll in the chloroplast absorbs the sunlight for energy.",
                "image": "images/step2.jpg",
                "video_url": "https://www.youtube.com/embed/eo5XndJaz-Y"
            },
            {
                "title": "Step 3: CO₂ and Water are Taken In",
                "text": "The plant absorbs water from roots and CO₂ from the air.",
                "image": "images/step3.jpg",
                "video_url": "https://www.youtube.com/embed/eo5XndJaz-Y"
            },
            {
                "title": "Step 4: Glucose and Oxygen Released",
                "text": "The plant converts energy into glucose and releases oxygen.",
                "image": "images/step4.jpg",
                "video_url": "https://www.youtube.com/embed/eo5XndJaz-Y"
            }
        ]
    },
    "DNA": {
        "steps": [
            {
                "title": "Step 1: Structure of DNA",
                "text": "DNA is made up of nucleotides arranged in a double helix.",
                "image": "images/dna_step1.jpg",
                "video_url": "https://www.youtube.com/embed/8kK2zwjRV0M"
            },
            {
                "title": "Step 2: Base Pairing",
                "text": "Adenine pairs with Thymine, and Cytosine with Guanine.",
                "image": "images/dna_step2.jpg",
                "video_url": "https://www.youtube.com/embed/8kK2zwjRV0M"
            },
            {
                "title": "Step 3: DNA Replication",
                "text": "DNA makes copies of itself during cell division.",
                "image": "images/dna_step3.jpg",
                "video_url": "https://www.youtube.com/embed/8kK2zwjRV0M"
            },
            {
                "title": "Step 4: Genetic Information",
                "text": "Genes in DNA carry instructions for protein synthesis.",
                "image": "images/dna_step4.jpg",
                "video_url": "https://www.youtube.com/embed/8kK2zwjRV0M"
            }
        ]
    }
}

st.set_page_config(page_title="AI Learning Prototype", layout="centered")
st.title("📚 AI Learning Video-like App")
st.markdown("---")

selected_topic = st.selectbox("🔍 Choose a Concept", list(topics.keys()))

# Reset session state when topic changes
if "step" not in st.session_state or st.session_state.get("topic") != selected_topic:
    st.session_state.step = 0
    st.session_state.topic = selected_topic

# Get the selected topic's data
data = topics[selected_topic]

# Ensure step is in valid range
if st.session_state.step >= len(data["steps"]):
    st.session_state.step = 0

step = data["steps"][st.session_state.step]

# Display content
st.subheader(step["title"])

try:
    st.image(step["image"], use_container_width=True)
except Exception as e:
    st.warning(f"Image not found: {step['image']}")

st.markdown(f"**Narration:** {step['text']}")

# AI Voice Narration
if st.button("🔊 Narrate This Step"):
    tts = gTTS(text=step["text"], lang='en')
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts.save(fp.name)
        st.audio(fp.name)

# Embed YouTube Video
st.markdown("### 🎞️ Explainer Video")
st.video(step["video_url"])

# Navigation buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("⬅️ Previous", disabled=st.session_state.step == 0):
        st.session_state.step -= 1
with col2:
    if st.button("Next ➡️", disabled=st.session_state.step == len(data["steps"])-1):
        st.session_state.step += 1

# Progress Bar (ensure value between 0.0 and 1.0)
progress_value = min((st.session_state.step + 1) / len(data["steps"]), 1.0)
st.progress(progress_value)

st.markdown("---")
st.info("This AI prototype presents educational concepts with images, narration, and video—like a virtual teacher!")
