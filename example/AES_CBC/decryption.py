import json
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--iv', type=str, required=True)
parser.add_argument('--text', type=str, required=True)
args = parser.parse_args()

try:
    key=b'\xeb\x8c\x99\xb0\x8e./\xd9A+G:\xa45\xafY'
    iv = b64decode(args.iv)
    ct = b64decode(args.text)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    print("The message was: ", pt)
except Exception as e:
    print("Incorrect decryption ", e)