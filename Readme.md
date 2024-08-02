# Work with Amazon Rekognition Using Python SDK
## Setup
1. Install `python3` and `pip3`
2. Install required libraries `pip3 install -r ./requirements.txt`
3. Provide AWS credentials and path to image in `.env.example` and `cp .env.example .env`

## Face recognition
`python ./face_recognition.py`

### Output example
```
Faces detected in the image. Number of faces: 5

Face 1:
 - Confidence: 100.00%
 - Image quality:
   - Brightness: 61.47
   - Sharpness: 78.64
 - Emotions:
   - HAPPY: 100.00%
   - ANGRY: 0.00%
   - DISGUSTED: 0.00%
   - FEAR: 0.00%
   - CALM: 0.00%
   - SAD: 0.00%
   - SURPRISED: 0.00%
   - CONFUSED: 0.00%
 - Gender: Male (confidence: 71.14%)
 - Age range: 18 - 22
 - Smile: Yes (confidence: 100.00%)
 - Eyeglasses: No (confidence: 100.00%)
 - Sunglasses: No (confidence: 100.00%)
 - Beard: No (confidence: 76.50%)
 - Mustache: No (confidence: 99.96%)

Face 2:
    ...
```
### You can also try to draw face boxes
`python ./draw_face_boxes.py`

## Safe search
### AI will try to detect:
- Explicit Nudity - Nudity
- Suggestive - Sexual content suggestions
- Violence
- Visually Disturbing - Visually disturbing images
- Rude Gestures
- Drugs
- Tobacco
- Alcohol
- Gambling
- Hate Symbols  
`python ./safe_search.py`

### Output example
```
 Inappropriate content detected in the image. Number of labels: 8
 - Label: Explicit, Confidence: 92.55%
 - Label: Exposed Female Nipple, Confidence: 92.55%
 - Label: Explicit Nudity, Confidence: 92.55%
 - Label: Exposed Female Genitalia, Confidence: 91.60%
 - Label: Exposed Male Genitalia, Confidence: 90.48%
 - Label: Non-Explicit Nudity of Intimate parts and Kissing, Confidence: 83.28%
 - Label: Non-Explicit Nudity, Confidence: 83.28%
 - Label: Exposed Male Nipple, Confidence: 83.28%
```