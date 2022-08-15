import json
from base64 import b64decode
from Crypto.Cipher import AES

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--nonce', type=str, required=True)
parser.add_argument('--header', type=str, required=True)
parser.add_argument('--text', type=str, required=True)
parser.add_argument('--tag', type=str, required=True)
args = parser.parse_args()

try:
    json_input=f'''{{"nonce": {args.nonce}, "header": {args.header}, "ciphertext": {args.text}, "tag": {args.text}}}'''
    key=b'P\xb31eZ"8\x15Mj\xf3\xceU\xb8\xe0\xa2'
    json_k = [ 'nonce', 'header', 'ciphertext', 'tag' ]

    cipher = AES.new(key, AES.MODE_CCM, nonce=b64decode(args.nonce))
    cipher.update(b64decode(args.header))
    plaintext = cipher.decrypt_and_verify(b64decode(args.text), b64decode(args.tag))
    print("The message was: ",plaintext)
except Exception as e:
    print("Incorrect decryption", e)