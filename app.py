# app.py

from transformers import pipeline

# Sentiment analysis pipeline
classifier = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    result = classifier(text)[0]
    label = result['label']
    score = result['score']
    return label, score

def main():
    print("Welcome to sentiment analysis app!")
    while True:
        text = input("\nEnter text to analyze: (type 'q' to quit): ")
        if text.lower() == 'q':
            print("Bye!")
            break
        label, score = analyze_sentiment(text)
        print(f"Sentiment: {label} | Confident Score: {score:.2f}")

if __name__ == "__main__":
    main()
