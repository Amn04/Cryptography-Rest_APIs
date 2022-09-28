import json
from base64 import b64encode
import os
from Crypto.Cipher import AES
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--data', type=str, required=True)
parser.add_argument('--key', type=str, required=True)
args = parser.parse_args()

try:

    header = b"header"
    data = bytes(args.data,'utf-8')
    isFile = os.path.isfile(args.key)
    if isFile:
        with open(args.key, "rb") as k:
            key=k.read()
    else:
        print("Invalid file or filepath of key")
        exit()

    print(key)
    cipher = AES.new(key, AES.MODE_CCM)
    cipher.update(header)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    json_k = [ 'nonce', 'header', 'ciphertext', 'tag' ]
    json_v = [ b64encode(x).decode('utf-8') for x in (cipher.nonce, header, ciphertext, tag)]
    result = json.dumps(dict(zip(json_k, json_v)))
    print(result)

except Exception as e:
    print("Internal error ",e)