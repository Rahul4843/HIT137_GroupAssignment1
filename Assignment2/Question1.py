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
    # Saving the encrypted file
    with open("encrypted_text.txt", "w") as f:
        f.write(newText)
    print("Encryption complete")

# Function for decrypting the text
def DeWord(keyA, keyB):
    decryptedText = ""
    # Reading both original and encrypted text
    with open("raw_text.txt", "r") as f:
        original = f.read()
    with open("encrypted_text.txt", "r") as f:
        encrypted = f.read()
    for i in range(len(encrypted)):
        orig_char = original[i]
        enc_char = encrypted[i]
        # Applying the decryption rules
        if 'a' <= orig_char <= 'm':
            decryptedText += chr(ord(enc_char) - keyA * keyB)
        elif 'n' <= orig_char <= 'z':
            decryptedText += chr(ord(enc_char) + (keyA + keyB))
        elif 'A' <= orig_char <= 'M':
            decryptedText += chr(ord(enc_char) + keyA)
        elif 'N' <= orig_char <= 'Z':
            decryptedText += chr(ord(enc_char) - keyB * keyB)
        else:
            decryptedText += enc_char
    # Saving the decrypted file
    with open("decrypted_text.txt", "w") as f:
        f.write(decryptedText)
    print("Decryption complete")

def verify_decryption():
    with open("raw_text.txt", "r") as f:
        original = f.read()
    with open("decrypted_text.txt", "r") as f:
        decrypted = f.read()
    # Checking each character from each file
    if original == decrypted:
        print("Decryption successful")
    else:
        print("Decryption failed.")

# Asking the user to input the values
shift1 = int(input("Enter shift 1 value: "))
shift2 = int(input("Enter shift 2 value: "))

# Calling the functions
EnWord(shift1, shift2)
DeWord(shift1, shift2)
verify_decryption()