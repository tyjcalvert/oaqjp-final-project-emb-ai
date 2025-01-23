"""
server.py

This module starts a Flask application that performs
emotion detection on user-supplied text.
"""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    """
    Analyze user input text for emotions and return the results.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    emo_data = emotion_detector(text_to_analyze)
    anger = emo_data['anger']
    disgust = emo_data['disgust']
    fear = emo_data['fear']
    joy = emo_data['joy']
    sadness = emo_data['sadness']
    dominant_emotion = emo_data['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    response = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': "
        f"{fear}, 'joy': {joy}, and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
     )

    return response

@app.route("/")
def index():
    """
    Render the home page.
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
