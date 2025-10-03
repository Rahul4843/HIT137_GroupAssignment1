# gui.py
"""
The following is the Tkinter GUI (Graphical User Interface) of my HIT137 Assignment 3.

It has two main parts:
Left side: selection of options and input (given by the user).
Right side: The results and the info will appear here.

"""

import tkinter as tk                                                                                      
from tkinter import ttk, scrolledtext, messagebox
from models import createTextGenerator, createImageClassifier
from utils import chooseImageFile, safeRunModel, getOopExplanationText, getModelInfoText

# The whole app window is constructed in this class.

class AppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("HIT137 Assignment 3") # Title of the window
        self.root.geometry("900x600")          #Setting the size and dimensions of the window

        # Loading text and image models
        try:
            self.textWrapper = createTextGenerator()
            self.imageWrapper = createImageClassifier()

        # Displaying an error popup if the models are not loaded properly
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load models: {e}")
            self.textWrapper = None
            self.imageWrapper = None

        # Left Panel 
        left = ttk.Frame(root, padding=10)
        left.pack(side=tk.LEFT, fill=tk.Y)

        # Dropdown menu to choose between text or image inputs
        row = ttk.Frame(left)
        row.pack(fill=tk.X, pady=4)
        ttk.Label(row, text="Input Type:").pack(side=tk.LEFT)
        self.inputType = tk.StringVar(value="text")
        self.inputTypeDropdown = ttk.Combobox(
            row, textvariable=self.inputType, values=["text", "image"],
            state="readonly", width=10
        )
        self.inputTypeDropdown.pack(side=tk.LEFT, padx=4)
        self.inputTypeDropdown.bind("<<ComboboxSelected>>", lambda e: self.onInputTypeChange())

        ttk.Separator(left).pack(fill=tk.X, pady=6)

        # Radio boxes to select the model to be operated.
        ttk.Label(left, text="Select Model:").pack(anchor=tk.W)
        self.outputType = tk.StringVar(value="textModel")
        for text, val in [("Text Model (distilgpt2)", "textModel"), ("Image Model (ViT)", "imageModel")]:
            ttk.Radiobutton(left, text=text, variable=self.outputType, value=val).pack(anchor=tk.W)

        ttk.Separator(left).pack(fill=tk.X, pady=6)

        # Text input box. This can be used to enter text which works only when the input type is text.
        ttk.Label(left, text="Text Input:").pack(anchor=tk.W)
        self.textEntry = scrolledtext.ScrolledText(left, width=40, height=6, wrap=tk.WORD)
        self.textEntry.pack(pady=4)

        # Section for choosing an image file. Input must be image for this to work
        ttk.Label(left, text="Image File:").pack(anchor=tk.W)
        self.imagePathVar = tk.StringVar()
        row = ttk.Frame(left)
        row.pack(fill=tk.X)
        ttk.Entry(row, textvariable=self.imagePathVar, width=30).pack(side=tk.LEFT)
        ttk.Button(row, text="Browse...", command=self.onBrowseImage).pack(side=tk.LEFT, padx=4)

        ttk.Separator(left).pack(fill=tk.X, pady=6)

        #  Button to actually run the selected model
        ttk.Button(left, text="Run Model", command=self.onRunModel).pack(fill=tk.X, pady=4)

        # RIGHT PANEL 
        right = ttk.Frame(root, padding=10)
        right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Output section
        ttk.Label(right, text="Model Output:").pack(anchor=tk.W)
        self.outputBox = scrolledtext.ScrolledText(right, height=8, wrap=tk.WORD)
        self.outputBox.pack(fill=tk.BOTH, expand=True, pady=4)

        # Object-Oriented Programming Explanation
        ttk.Label(right, text="OOP Explanation:").pack(anchor=tk.W)
        self.explainBox = scrolledtext.ScrolledText(right, height=6, wrap=tk.WORD)
        self.explainBox.pack(fill=tk.BOTH, pady=4)
        self.explainBox.insert(tk.END, getOopExplanationText())
        self.explainBox.config(state=tk.DISABLED)

        # info about the models being used
        ttk.Label(right, text="Model Info:").pack(anchor=tk.W)
        self.modelInfoBox = scrolledtext.ScrolledText(right, height=5, wrap=tk.WORD)
        self.modelInfoBox.pack(fill=tk.BOTH)
        if self.textWrapper and self.imageWrapper:
            self.modelInfoBox.insert(tk.END, getModelInfoText(self.textWrapper, self.imageWrapper))
        else:
            self.modelInfoBox.insert(tk.END, "Model info not available.")
        self.modelInfoBox.config(state=tk.DISABLED)

        # ensuring that the correct input is active
        self.onInputTypeChange()

    # Events Handlers. This function runs when the input type such as text or image is changed
    def onInputTypeChange(self):
        if self.inputType.get() == "text":
            self.textEntry.config(state=tk.NORMAL)
        else:
            self.textEntry.config(state=tk.DISABLED)

    # Function which is called when the user clicks "Browse"
    def onBrowseImage(self):
        path = chooseImageFile(self.root)
        if path:
            self.imagePathVar.set(path)

    # Function which is called when the user clicks "Run Model"
    def onRunModel(self):
        self.outputBox.delete("1.0", tk.END)
        use = self.outputType.get()
        inputType = self.inputType.get()

        # Condition if the text model is selected by the user

        if use == "textModel":
            if not self.textWrapper:
                self.outputBox.insert(tk.END, "Text model not loaded.\n")
                return
            if inputType != "text":
                self.outputBox.insert(tk.END, "Input must be text.\n")
                return
            prompt = self.textEntry.get("1.0", tk.END).strip()
            if not prompt:
                self.outputBox.insert(tk.END, "Enter text first.\n")
                return
            out = safeRunModel(self.textWrapper, prompt)

        else:  # condition if the image model is selected
            if not self.imageWrapper:
                self.outputBox.insert(tk.END, "Image model not loaded.\n")
                return
            if inputType != "image":
                self.outputBox.insert(tk.END, "Input must be image.\n")
                return
            path = self.imagePathVar.get().strip()
            if not path:
                self.outputBox.insert(tk.END, "Choose an image.\n")
                return
            out = safeRunModel(self.imageWrapper, path)

        self.outputBox.insert(tk.END, str(out))

    # Function to start the GUI
def runGui():
    root = tk.Tk()
    AppGUI(root)
    root.mainloop()

#This ensures that the GUI is not run when this file has been imported, but rather when directly run.
if __name__ == "__main__":
    runGui()
