from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--public_key', type=str, required=True)
parser.add_argument('--msg', type=str, required=True)
parser.add_argument('--signature', type=str, required=True)
args = parser.parse_args()

isFile = os.path.isfile(args.msg)
if isFile:
    with open(args.msg, "rb") as msg:
        message=msg.read()
else:
    message=bytes(args.msg,'utf-8')

isFile = os.path.isfile(args.signature)
if isFile:
    with open(args.signature, "rb") as sign:
        signature=sign.read()
else:
    print("Invalid Signature path")

with open(args.public_key, "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
    )
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Signature verified")
except Exception as e:
    print("Invalid Signature")