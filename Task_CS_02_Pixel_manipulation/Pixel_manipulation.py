from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key):
    # Open the image
    image = Image.open(image_path)
    image_array = np.array(image)

    # Encrypt the image by adding the key to each pixel value
    encrypted_array = (image_array + key) % 255

    # Convert the array back to an image
    encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))

    # Save the encrypted image
    encrypted_image.save(output_path)
    print(f'Encrypted image saved to {output_path}')

def decrypt_image(encrypted_path, output_path, key):

    print('breakpoint')

    # Open the encrypted image
    encrypted_image = Image.open(encrypted_path)
    print(f'breakpoint0')

    encrypted_array = np.array(encrypted_image)
    print(f'breakpoint1')

    # Decrypt the image by subtracting the key from each pixel value
    decrypted_array = (encrypted_array - key) % 256
    print(f'breakpoint2')

    # Convert the array back to an image
    decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))
    print(f'breakpoint3')

    # Save the decrypted image
    decrypted_image.save(output_path)
    print(f'Decrypted image saved to {output_path}')

name = "main"
# Example usage
if name == "main":
    original_image_path = 'C:/Users/moune/OneDrive/Desktop/Python Project/butterflies.jpg'
    encrypted_image_path = 'C:/Users/moune/OneDrive/Desktop/Python Project/butterfliesEnc.jpg'
    decrypted_image_path = 'C:/Users/moune/OneDrive/Desktop/Python Project/butterfliesDec.jpg'
    encryption_key = 123  # Example key

    print('Testing')
    encrypt_image(original_image_path, encrypted_image_path, encryption_key)
    decrypt_image(encrypted_image_path, decrypted_image_path, encryption_key)