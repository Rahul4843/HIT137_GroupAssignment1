# models.py
"""
 text generation done using open-ai-community/gpt2-medium.

 image classification is from google/vit-base-patch16-224.

Both models are pipelines, which utilize Hugging face transformers to avoid manual download
"""

from transformers import pipeline
from oopConcepts import TextModelWrapper, ImageModelWrapper

# Names of the models being used
TEXT_MODEL_ID = "openai-community/gpt2-medium"    # model for generating text
IMAGE_MODEL_ID = "google/vit-base-patch16-224"    # model for classifying images

# Function to set up the text generator
def createTextGenerator():
    """
    setting up a text generation model using gpt2-medium.
    """
    try:
        pipe = pipeline("text-generation", model="openai-community/gpt2-medium")    
        wrapper = TextModelWrapper(TEXT_MODEL_ID, pipe)
        return wrapper
    except Exception as e:  
        print("Error creating text generator. Please make sure 'transformers' and 'torch' are installed.")
        print("Exception:", e)
        raise

# Function to set up the image generator 
def createImageClassifier():
    """
    Making an image-classification pipeline.
    The pipeline accepts either a PIL image or a path to an image file.
    """
    try:
        pipe = pipeline("image-classification", model="google/vit-base-patch16-224")
        wrapper = ImageModelWrapper(IMAGE_MODEL_ID, pipe)
        return wrapper
    except Exception as e:
        print("Error creating image classifier. Please check environment and required libraries.")
        print("Exception:", e)
        raise