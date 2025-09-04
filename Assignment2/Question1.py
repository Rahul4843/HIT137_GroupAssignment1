# Function for encrypting the text from raw_text.txt 
def EnWord(keyA, keyB):
    newText = ""
    # Opening the raw file for reading.
    with open("raw_text.txt", "r") as file:
        while True:
            char = file.read(1)  # Going through one character at a time
            if not char:
                break
            # Applying the encryption rules
            if 'a' <= char <= 'm':
                newText += chr(ord(char) + keyA * keyB)
            elif 'n' <= char <= 'z':
                newText += chr(ord(char) - (keyA + keyB))
            elif 'A' <= char <= 'M':
                newText += chr(ord(char) - keyA)
            elif 'N' <= char <= 'Z':
                newText += chr(ord(char) + keyB * keyB)
            else:
                newText += char
    # Save the encrypted file
    with open("encrypted_text.txt", "w") as f:
        f.write(newText)
    print("Encryption complete!")

# Asking the user to input the values for the encryption
shift1 = int(input("Enter the value of shift 1: "))
shift2 = int(input("Enter the value of shift 2"))

# Calling the function
EnWord(shift1, shift2)
