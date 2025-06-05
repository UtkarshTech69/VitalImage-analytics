# 🧠 VitalImage Analytics - AI-Powered Medical Image Analysis

VitalImage Analytics is an AI-driven Streamlit application that empowers healthcare professionals by providing intelligent insights from medical images using Google’s Generative AI (Gemini 1.5 Flash). This tool assists in identifying anomalies, generating detailed diagnostic reports, and suggesting next steps — all within a secure, private, and easy-to-use interface.

> ⚠️ **Disclaimer**: This tool is intended for educational and research purposes only. It is not a substitute for professional medical diagnosis. Always consult a licensed physician for actual health concerns.

---

## 🚀 Features

- 📤 Upload medical images in `.png`, `.jpg`, or `.jpeg` formats.
- ⚕️ AI-generated diagnostic reports using multimodal image + prompt input.
- 🧪 Analysis follows a structured format:  
  - Detailed Analysis  
  - Finding Reports  
  - Recommendations and Next Steps  
  - Treatment Suggestions
- 🧾 Downloadable analysis report in `.txt` format.
- 🎨 Clean and aesthetic UI with custom glassmorphism effects and branded logo.

---

## 📸 Sample Use Case

A hospital technician uploads a chest X-ray, and the system provides a structured diagnostic report including potential health risks, areas of concern, and recommended follow-up actions—all powered by Google’s cutting-edge generative AI.

---

## 🏗️ Tech Stack

| Technology           | Description                                        |
|----------------------|----------------------------------------------------|
| Python               | Core programming language                          |
| Streamlit            | Web application framework                          |
| Google Generative AI | Gemini 1.5 Flash API for multimodal reasoning      |
| HTML/CSS             | Custom styling for frontend presentation           |
| Base64               | Image encoding for inline display in browser       |

---

## 📁 Project Structure

```
VitalImage-Analytics/
│
├── assets/
│   └── logo.png                  # Custom logo displayed on the app
│
├── .gitignore                    # Ensures sensitive files are not pushed
├── app.py                        # Main Streamlit application
├── api_key.py (ignored)         # API key storage (excluded from GitHub)
├── README.md                     # Project documentation
├── requirements.txt              # List of Python dependencies
```

---

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/VitalImage-Analytics.git
cd VitalImage-Analytics
```

### 2. Create & Activate a Virtual Environment
```bash
python -m venv .venv
# For Windows
.venv\Scripts\activate
# For macOS/Linux
source .venv/bin/activate
```

### 3. Install Required Packages
```bash
pip install -r requirements.txt
```

### 4. Add Your Google Generative AI API Key

Create a file named `api_key.py` in the root directory with the following:

```python
api_key = "YOUR_GOOGLE_API_KEY"
```

> ⚠️ **Important**: Do NOT upload `api_key.py` to GitHub. It is ignored via `.gitignore`.

### 5. Run the App
```bash
streamlit run app.py
```

---

## ✅ Example Output

After uploading a medical image, the system will generate an analysis like:

```
### Detailed Analysis:
The image exhibits signs of...

### Finding Reports:
- Enlarged cardiac silhouette
- Abnormal opacity in the right lung...

### Recommendations and Next Steps:
- Recommend a follow-up chest CT
- Suggest consultation with a cardiologist...

### Treatment Suggestions:
- Depending on CT findings...
```

---

## 🔒 Security Considerations

- No patient-identifiable information is stored.
- All API interactions are local and secured by your API key.
- Sensitive files like `.venv/`, `__pycache__/`, and `api_key.py` are excluded via `.gitignore`.

---

## 📌 Key Learning Outcomes

This project demonstrates:

- Integration of multimodal generative AI into a real-world health-tech use case.
- Clean UI/UX with glassmorphism and Streamlit enhancements.
- Handling of secure keys and best practices in deploying AI projects.
- Structured generation of medical reports suitable for both technical and non-technical stakeholders.

---

## 👨‍💻 About Me

Hi! I'm **Utkarsh Mishra**, a recent graduate in **Artificial Intelligence and Data Science**. I’m passionate about building real-world AI applications that drive impact, especially in healthcare and automation domains.  
🔗 [LinkedIn](https://www.linkedin.com/in/yourprofile) | 🌐 [Portfolio](https://your-portfolio.com)

---

## 🤝 Contributions & Feedback

This is a solo project, but I’m always open to collaborations, feedback, or improvements.  
Feel free to fork this repo or raise issues for enhancements.
