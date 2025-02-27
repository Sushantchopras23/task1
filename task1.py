def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == 'encrypt' else -shift
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift_amount) % 26 + base)
        else:
            result += char
    return result

# Get user input
mode = input("Do you want to encrypt or decrypt? (enter 'encrypt' or 'decrypt'): ").strip().lower()
if mode not in ['encrypt', 'decrypt']:
    print("Invalid mode. Please enter 'encrypt' or 'decrypt'.")
    exit()

text = input("Enter your message: ").strip()
try:
    shift = int(input("Enter the shift value (integer): ").strip())
except ValueError:
    print("Invalid shift value. Please enter an integer.")
    exit()

# Perform encryption or decryption
result = caesar_cipher(text, shift, mode)
print(f"Result: {result}")
