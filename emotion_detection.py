import json
import requests


def emotion_detector(text_to_analyze):
    """Analyzes text using Watson NLP, extracts specific emotion scores,

    and identifies the dominant emotion.
    """
    # API Setup
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    myobj = {"raw_document": {"text": text_to_analyze}}

    # Send request to the Watson NLP service
    response = requests.post(url, json=myobj, headers=headers)

    # Convert the raw text response into a Python dictionary
    formatted_response = json.loads(response.text)

    # Navigate the Watson NLP JSON structure to extract the emotion scores dictionary
    # Watson's structure: response -> 'emotionPredictions' (list) -> 1st element -> 'emotion' (dict)
    emotions = formatted_response["emotionPredictions"][0]["emotion"]

    # Extract individual scores
    anger_score = emotions["anger"]
    disgust_score = emotions["disgust"]
    fear_score = emotions["fear"]
    joy_score = emotions["joy"]
    sadness_score = emotions["sadness"]

    # Logic to find the dominant emotion (the key with the maximum value)
    dominant_emotion = max(emotions, key=emotions.get)

    # Construct the final formatted output dictionary
    output = {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
        "dominant_emotion": dominant_emotion,
    }

    return output