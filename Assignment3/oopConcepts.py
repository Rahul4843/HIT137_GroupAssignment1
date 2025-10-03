# oopConcepts.py
"""
used Object Oriented programming concepts
- inheritance
- encapsulation (private attributes)
- polymorphism (same method name used across subclasses)
- method overriding
- decorators (multiple decorators)
"""

import time
from functools import wraps

#  Using decorators which logs when a function starts and ends
def simpleLog(func):
    """Decorator: Prints messages before and after the function runs."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling {func.__name__}")  # Before the function run
        result = func(*args, **kwargs)
        print(f"[LOG] Finished {func.__name__}") # After the function ends
        return result
    return wrapper

# Function to track how long a fucntion takes to run
def timeIt(func):
    """Prints how long the function takes to run."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()                      # Start the timer
        result = func(*args, **kwargs)
        end = time.time()                        # Start the timer
        print(f"[TIME] {func.__name__} took {end - start:.3f}s")
        return result
    return wrapper

# Base Class
class ModelWrapper:
    """base class for both the text and image model wrappers demonstrating encapsulation and polymorphism."""
    def __init__(self, modelName: str):
        # encapsulated attribute (private)
        self._modelName = modelName

    def getModelName(self):
        return self._modelName

    def getModelInfo(self):
        """Polymorphic method: subclasses should override this."""
        return f"Generic model: {self._modelName}"

    def processInput(self, inputData):
        """Polymorphic placeholder - should be overridden by subclasses."""
        raise NotImplementedError("processInput must be overridden by subclass")


# Subclass for text model. This overrides base methods
class TextModelWrapper(ModelWrapper):
    def __init__(self, modelName: str, generator):
        super().__init__(modelName)  # Calling the constructor from the base class
        self._generator = generator  # Hugging Face pipeline for text generation

    def getModelInfo(self):
        """Overriding the base method to return info about the text model."""
        return f"Text model wrapper for {self._modelName}"

    @simpleLog  # Logs when this function starts and ends
    @timeIt     # Measures how long it takes
    
    def processInput(self, inputData: str):
        """Generates text using the provided hugging face text generator pipeline."""
        output = self._generator(inputData, max_new_tokens=60)
        # pipeline returns a list
        if isinstance(output, list) and "generated_text" in output[0]:
            return output[0]["generated_text"]
        # converting to string as older versions may return different structure
        return str(output)


# Subclass for image model. It overrides base methods
class ImageModelWrapper(ModelWrapper):
    def __init__(self, modelName: str, classifier):
        super().__init__(modelName)
        self._classifier = classifier

    def getModelInfo(self):
        """Overriding base method to show the information about the image model."""
        return f"Image classification model wrapper: {self._modelName}"

    @simpleLog
    @timeIt
    def processInput(self, imagePath: str):
        """
       function that takes the path to an image file, and returns classification results.
        The classifier is expected to be a transformers pipeline for image-classification.
        """
        results = self._classifier(imagePath, top_k=3)
        return results
