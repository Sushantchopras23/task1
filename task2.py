from PIL import Image
import random

def encrypt_image(image_path, output_path, key):
    img = Image.open(image_path)
    pixels = img.load()

    width, height = img.size
    random.seed(key)

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # Simple encryption by adding a random value to each color channel
            pixels[x, y] = ((r + random.randint(0, 255)) % 256,
                            (g + random.randint(0, 255)) % 256,
                            (b + random.randint(0, 255)) % 256)
    img.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(image_path, output_path, key):
    img = Image.open(image_path)
    pixels = img.load()

    width, height = img.size
    random.seed(key)

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # Reverse the encryption by subtracting the random value
            pixels[x, y] = ((r - random.randint(0, 255)) % 256,
                            (g - random.randint(0, 255)) % 256,
                            (b - random.randint(0, 255)) % 256)
    img.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

# Get user input
mode = input("Enter mode (encrypt/decrypt): ").strip().lower()
image_path = input("Enter path to the image: ").strip()
output_path = input("Enter output path for the processed image: ").strip()
key = input("Enter a key (integer) for encryption/decryption: ").strip()

try:
    key = int(key)
    if mode == 'encrypt':
        encrypt_image(image_path, output_path, key)
    elif mode == 'decrypt':
        decrypt_image(image_path, output_path, key)
    else:
        print("Invalid mode. Use 'encrypt' or 'decrypt'.")
except ValueError:
    print("Invalid key. Please enter an integer.")
