
# Sentiment Analysis App

This project is a simple **sentiment analysis** application using Hugging Face Transformers. It works both in the **terminal** and through a **web interface** with Streamlit.

---

## Setup

1. Clone or download the repository:
```bash
git clone <repo-link>
cd sentiment-analysis-app-main
## Create and activate a virtual environment:

python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate   # Mac/Linux

Install required libraries:
pip install transformers torch streamlit

## Usage
Terminal Mode
python app.py

Enter text to analyze and see the sentiment
Type q to quit

##Web Interface (Streamlit)
streamlit run app.py


A browser window will open with the web interface

Enter text and click Analyze
