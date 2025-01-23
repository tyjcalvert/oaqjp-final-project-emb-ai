import requests, json

def emotion_detector(text_to_analyse):
    try:
        url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
        headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
        myobj = { "raw_document": { "text": text_to_analyse } }
        response = requests.post(url, json = myobj, headers = headers)

        if response.status_code == 400:
            obj = {
                "anger": None, 
                "disgust": None, 
                "fear": None, 
                "joy": None, 
                "sadness": None, 
                "dominant_emotion": None
            }

            return obj

        formatted_response = json.loads(response.text)

        emotion_data = formatted_response['emotionPredictions'][0]['emotion']
        emotion_data['dominant_emotion'] = max(emotion_data, key=emotion_data.get)

        return emotion_data
    except Exception as err:
        return { "error": str(err) }
        
