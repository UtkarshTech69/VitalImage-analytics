# import necessary libraries
import streamlit as st
import google.generativeai as genai
from pathlib import Path
from api_key import api_key
import base64

# configure the Google Generative AI API
genai.configure(api_key=api_key)

# set up the model
generation_config = {
    "temperature": 0.4,
    "top_p": 1,
    "top_k": 32,
    "max_output_tokens": 4096,
}

# apply safety settings
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

# System prompt for the model
system_prompt = """
As a highly skilled medical practitioner specializing in image analysis, you are tasked with examining medical images for a renowned hospital. Your expertise is crucial in identifying any anomalies or health issues that may be present in the images.

Your responsibilities include:

1. Detailed Analysis: thoroughly analyze each image, focusing on identifying any abnormal findings
2. Finding Reports: Document all observed anomalies or signs of disease. Clearly articulate these findings in a structured report format.
3. Recommendations and Next Steps: Based on you analysis, suggest potential next steps including further tests or treatments as applicable.
4. Treatment suggestions: If applicable, provide recommend possible treatment options or interventions based on the findings.

Important Notes:

1. Scope of response: Only respond if the image pertains to human health issues. 
2. clarity and precision: In case where the image quality impedes clear analysis, note that certain aspects are 'Unable to be determined based on the provided image.'
3. Desclaimer: Accompany your analysis with the disclaimer: "Consult with a Doctor before making any decisions in long-term health issues. This analysis is not a substitute for professional medical advice or treatment."

Your insights are invaluable in guiding clinical decisions. please proceed with the analysis, adhering to the structured approach outlined above.

Please provide me an output response with these four headings with long explanation: Detailed Analysis, Finding Reports, Recommendations and Next Steps, and Treatment Suggestions.
"""

# Model setup
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    safety_settings=safety_settings,
)

# Set Streamlit page config
st.set_page_config(
    page_title="VitalImage Analytics",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom CSS styling
st.markdown("""
<style>
    body {
        background-color: #fdf6e3;
    }
    .stButton>button {
        background-color: #a1887f;
        color: white;
        border: None;
        padding: 0.5em 2em;
        border-radius: 8px;
    }
    .stButton>button:hover {
        background-color: #8d6e63;
    }
    .glass-image-container {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
        padding: 15px;
        margin-bottom: 20px;
        text-align: center;
    }
    .glass-image-container img {
        max-width: 100%;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    }
</style>
""", unsafe_allow_html=True)

# Show logo on the left
st.image("assets/logo.png", width=60)

# Title and subheader
st.title("⚕️ VitalImage 🔍 Analytics 🧠📊")
st.subheader("An intelligent assistant to help identify patterns and insights from medical images.")

# File uploader
upload_file = st.file_uploader("📤 Upload the medical image for analysis", type=["png", "jpg", "jpeg"])

# Submit button
submit_button = st.button("🧪 Generate the Analysis")

# Analysis generation logic
if submit_button and upload_file is not None:
    image_bytes = upload_file.getvalue()
    mime = upload_file.type
    encoded = base64.b64encode(image_bytes).decode()

    # Display uploaded image in glass morphism style
    st.markdown(f"""
    <div class="glass-image-container">
        <img src="data:{mime};base64,{encoded}" alt="Uploaded Image" />
        <p style="margin-top: 10px; color: #555;">🖼️ Uploaded Medical Image</p>
    </div>
    """, unsafe_allow_html=True)

    # Call Gemini model with image + prompt
    image_parts = [{"mime_type": mime, "data": image_bytes}]
    prompt_parts = [image_parts[0], system_prompt]
    response = model.generate_content(prompt_parts)

    # Display analysis with minimal clean style
    st.markdown("### 📝 Analysis Report:")
    with st.container():
        st.markdown("""
        <div style="
            background: rgba(255, 255, 255, 0.8);
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.05);
            font-family: 'Segoe UI', sans-serif;
        ">
        """, unsafe_allow_html=True)

        st.markdown(response.text, unsafe_allow_html=False)

        st.markdown("</div>", unsafe_allow_html=True)

    # Download button
    st.download_button(
        label="📥 Download Report",
        data=response.text,
        file_name="vitalimage_analysis_report.txt",
        mime="text/plain"
    )
