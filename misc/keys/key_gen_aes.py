from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(32)

# Save the key to a file
file_out = open("key_file.bin", "wb") # wb = write bytes
file_out.write(key)
file_out.close()