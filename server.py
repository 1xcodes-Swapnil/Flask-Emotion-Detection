"""Flask app for detecting emotions in text."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Handles emotion detection for incoming text.
    Returns a formatted response or an error message.
    """
    text_to_analyze = request.args.get('textToAnalyze', '')

    response = emotion_detector(text_to_analyze)

    if response.get('label') is None or response.get('score') is None:
        return "Invalid text! Please try again!"

    label = response['label']
    score = response['score']

    return f"The given text has been identified as {label.split('_')[1]} with a score of {score}."

@app.route("/")
def render_index_page():
    """Renders the index HTML page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
    