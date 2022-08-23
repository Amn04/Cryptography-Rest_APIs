from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--length', type=int, required=True, help='Length of key')
args = parser.parse_args()

key = get_random_bytes(args.length)
# Save the key to a file
file_out = open("key_file.bin", "wb") # wb = write bytes
file_out.write(key)
file_out.close()
print("Generated Key ",key)