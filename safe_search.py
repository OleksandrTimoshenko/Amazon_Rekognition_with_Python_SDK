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

# Function to check for inappropriate content in an image
def check_for_moderation_labels(image_path):
    # Read the image file
    with open(image_path, 'rb') as image_file:
        image_bytes = image_file.read()

    # Call detect_moderation_labels method to detect inappropriate content in the image
    response = rekognition_client.detect_moderation_labels(
        Image={'Bytes': image_bytes}
    )

    # Check the result
    if len(response['ModerationLabels']) > 0:
        print(f"Inappropriate content detected in the image. Number of labels: {len(response['ModerationLabels'])}")
        for label in response['ModerationLabels']:
            print(f" - Label: {label['Name']}, Confidence: {label['Confidence']:.2f}%")
    else:
        print("No inappropriate content detected in the image.")

# Check the image for inappropriate content
check_for_moderation_labels(image_path)