import requests
import json

def emotion_detector(text_to_analyze):
    """Runs emotion detection on the text_to_analyze argument and returns

    the raw text attribute of the server response.
    """
    # Define the URL and headers for the Watson NLP Emotion Predict service
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # Format the input JSON payload using the argument variable
    myobj = {"raw_document": {"text": text_to_analyze}}

    # Send the POST request to the API
    response = requests.post(url, json=myobj, headers=headers)

    # Return the text attribute of the response object
    return response.text