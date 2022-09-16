''''
This script is an example to sign a message using RSA. To sign a message one needs 
private key. In this example private key needs to be supplied by filepath in args.
Message to sign can be either passed using filepath or a string through args.
If signing is successful then it will print the signature along with success.
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


with open('signature.txt', 'wb') as f:
    f.write(signature)

print("Success")