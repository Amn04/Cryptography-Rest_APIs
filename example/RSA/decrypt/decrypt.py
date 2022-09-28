from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--private_key', type=str, required=True)
parser.add_argument('--cipher_txt', type=str, required=True)
parser.add_argument('--hash_algo', type=str, required=True)
args = parser.parse_args()

isFile = os.path.isfile(args.cipher_txt)
if isFile:
    with open(args.cipher_txt, "rb") as cipher_txt:
        ciphertext=cipher_txt.read()
else:
    print("Invalid file or invalid filepath")
    exit()

with open(args.private_key, "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )

hash_algo=args.hash_algo

plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=eval(hash_algo)),
        algorithm=eval(hash_algo),
        label=None
    )
)
print(plaintext)