from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--public_key', type=str, required=True)
parser.add_argument('--msg', type=str, required=True)
parser.add_argument('--hash_algo', type=str, required=True)
args = parser.parse_args()

isFile = os.path.isfile(args.msg)
if isFile:
    with open(args.msg, "rb") as msg:
        message=msg.read()
else:
    message=bytes(args.msg,'utf-8')

with open(args.public_key, "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
    )

hash_algo=args.hash_algo

ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=eval(hash_algo)),
        algorithm=eval(hash_algo),
        label=None
    )
)
print("Sucsess")
print(ciphertext)
