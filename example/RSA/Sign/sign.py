''''
This script is an example script to sign a using RSA. To sign a message one need to use 
private key. In this example private key need to be supplied by filepath in args.
Message to sign can be either passed using filepath or a string through args.
If signing will be succeed then it will print the signature.
'''

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--private_key', type=str, required=True)
parser.add_argument('--msg', type=str, required=True)
args = parser.parse_args()

with open(args.private_key, "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )

isFile = os.path.isfile(args.msg)
if isFile:
    with open(args.msg, "rb") as msg:
        message=msg.read()
else:
    message=bytes(args.msg,'utf-8')


signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

print(message)
print("Signature: ",signature)