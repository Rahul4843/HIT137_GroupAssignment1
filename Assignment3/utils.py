# utils.py
"""
Functions for utility helpers used in the project:
file selection such as selecting image from the computer
running safe wrappers
Showing basic explanations of OOP
"""

import os
from tkinter import filedialog  # Opening file picker window

# Image Picker Function
def chooseImageFile(parentWindow=None):
    """This opens a file picker so the user can select an image file. 
    It returns the path to the image, or None if they cancel or pick something invalid."""

    # File types that the picker will allow. Only images are allowed
    filetypes = [("Image files", ".jpg *.jpeg *.png *.bmp"), ("All files", ".*")]
    path = filedialog.askopenfilename(parent=parentWindow, title="Select an image", filetypes=filetypes)
    if not path:
        return None
    if not os.path.exists(path):
        return None
    return path

# Safe Running Models
def safeRunModel(modelWrapper, inputData):
    """
    Calls modelWrapper.processInput within try/except and this returns either result or error string.
    Makes code in GUI easier because error management is centralized.
    """
    try:
        return modelWrapper.processInput(inputData)
    except Exception as e:
        return f"Error running model: {e}"

def getOopExplanationText():
    
# Returning a string explaining OOP concepts used in this project.
    text = (
        "OOP explanations:\n"
        "- Inheritance: ModelWrapper is the base class;  It has two kinds of inheritance: TextModelWrapper and ImageModelWrapper which inherit from it.\n"
        "- Encapsulation: model name and pipeline objects are held as private attributes (e.g. modelName)..\n"
        "Polymorphism: processInput is implemented in both the subclasses, GUI invokes the same method in all wrappers.\n"
        "Method overriding: In order to give a given behavior, subclasses implement getModelInfo and processInput.\n"
        "Decorators: simpleLog and timeIt wrap model calls to show logs and timings.\n"
    )
    return text

def getModelInfoText(textWrapper, imageWrapper):
    """Returns brief info about the selected models for the GUI."""
    return (
        f"Text model: {textWrapper.getModelName()}\n{ textWrapper.getModelInfo() }\n\n"
        f"Image model: {imageWrapper.getModelName()}\n{ imageWrapper.getModelInfo() }\n"
    )