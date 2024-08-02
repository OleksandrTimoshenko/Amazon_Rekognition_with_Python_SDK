import boto3
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get environment variables
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_region = os.getenv('AWS_DEFAULT_REGION')
image_path = os.getenv('image_path')

# Initialize Amazon Rekognition client using environment variables
rekognition_client = boto3.client(
    'rekognition',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=aws_region
)

# Function to check for faces in an image and get information about each face
def check_for_faces(image_path):
    # Read the image file
    with open(image_path, 'rb') as image_file:
        image_bytes = image_file.read()

    # Call detect_faces method to detect faces in the image
    response = rekognition_client.detect_faces(
        Image={'Bytes': image_bytes},
        Attributes=['ALL']
    )

    # Check the result
    if len(response['FaceDetails']) > 0:
        print(f"Faces detected in the image. Number of faces: {len(response['FaceDetails'])}")
        for i, face_detail in enumerate(response['FaceDetails']):
            print(f"\nFace {i + 1}:")
            print(f" - Confidence: {face_detail['Confidence']:.2f}%")

            # Image quality
            if 'Quality' in face_detail:
                print(" - Image quality:")
                print(f"   - Brightness: {face_detail['Quality']['Brightness']:.2f}")
                print(f"   - Sharpness: {face_detail['Quality']['Sharpness']:.2f}")

            # Emotions
            if 'Emotions' in face_detail:
                emotions = sorted(face_detail['Emotions'], key=lambda x: x['Confidence'], reverse=True)
                print(" - Emotions:")
                for emotion in emotions:
                    print(f"   - {emotion['Type']}: {emotion['Confidence']:.2f}%")

            # Other attributes
            print(f" - Gender: {face_detail['Gender']['Value']} (confidence: {face_detail['Gender']['Confidence']:.2f}%)")
            print(f" - Age range: {face_detail['AgeRange']['Low']} - {face_detail['AgeRange']['High']}")
            print(f" - Smile: {'Yes' if face_detail['Smile']['Value'] else 'No'} (confidence: {face_detail['Smile']['Confidence']:.2f}%)")
            print(f" - Eyeglasses: {'Yes' if face_detail['Eyeglasses']['Value'] else 'No'} (confidence: {face_detail['Eyeglasses']['Confidence']:.2f}%)")
            print(f" - Sunglasses: {'Yes' if face_detail['Sunglasses']['Value'] else 'No'} (confidence: {face_detail['Sunglasses']['Confidence']:.2f}%)")
            print(f" - Beard: {'Yes' if face_detail['Beard']['Value'] else 'No'} (confidence: {face_detail['Beard']['Confidence']:.2f}%)")
            print(f" - Mustache: {'Yes' if face_detail['Mustache']['Value'] else 'No'} (confidence: {face_detail['Mustache']['Confidence']:.2f}%)")
    else:
        print("No faces detected in the image.")

# Check the image
check_for_faces(image_path)
