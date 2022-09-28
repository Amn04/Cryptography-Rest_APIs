import json
from base64 import b64decode
import os
from Crypto.Cipher import AES

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--nonce', type=str, required=True)
parser.add_argument('--header', type=str, required=True)
parser.add_argument('--text', type=str, required=True)
parser.add_argument('--tag', type=str, required=True)
parser.add_argument('--key', type=str, required=True)
args = parser.parse_args()

try:
    isFile = os.path.isfile(args.key)
    if isFile:
        with open(args.key, "rb") as k:
            key=k.read()
    else:
        print("Invalid file or filepath of key")
        exit()

    cipher = AES.new(key, AES.MODE_CCM, nonce=b64decode(args.nonce))
    cipher.update(b64decode(args.header))
    plaintext = cipher.decrypt_and_verify(b64decode(args.text), b64decode(args.tag))
    print("The message was: ",plaintext)

except Exception as e:
    print("Incorrect decryption", e)