import gradio as gr
from transformers import pipeline

classifier = pipeline("sentiment-analysis")

def analyze(text):
    result = classifier(text)[0]
    return f"Sentiment: {result['label']}", f"Confidence: {result['score']:.2f}"

iface = gr.Interface(
    fn=analyze,
    inputs="text",
    outputs=["text", "text"],
    title="Sentiment Analysis App",
    description="Enter any text to see its sentiment prediction!"
)

iface.launch()
