import imageio.v3 as imageio
import numpy as np
import matplotlib.pyplot as plt

def encrypt_image(image, key):
    encrypted_image = np.bitwise_xor(image, key)
    return encrypted_image

def decrypt_image(encrypted_image, key):
    decrypted_image = np.bitwise_xor(encrypted_image, key)
    return decrypted_image

image_path = 'gajah.jpg'
original_image = imageio.imread(image_path)  


np.random.seed(42)  
key = np.random.randint(0, 256, original_image.shape, dtype=np.uint8)


encrypted_image = encrypt_image(original_image, key)

decrypted_image = decrypt_image(encrypted_image, key)


plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1)
plt.title('Original Image')
plt.imshow(original_image)
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('Encrypted Image')
plt.imshow(encrypted_image)
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('Decrypted Image')
plt.imshow(decrypted_image)
plt.axis('off')

plt.tight_layout()
plt.show()

