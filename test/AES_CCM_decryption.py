import json
from base64 import b64decode
from Crypto.Cipher import AES

# We assume that the key was securely shared beforehand
try:
    json_input='''{"nonce": "t5W6Djt7DbiLAGg=", "header": "aGVhZGVy", "ciphertext": "Zw7/kU6V", "tag": "MJ6z0dpxo86Am5+096j8lg=="}'''
    b64 = json.loads(json_input)
    key=b'#\x03\x01v\xddq\xbe1n\x05\xc1\xe1y\x8a+\x8c'
    json_k = [ 'nonce', 'header', 'ciphertext', 'tag' ]
    jv = {k:b64decode(b64[k]) for k in json_k}
    cipher = AES.new(key, AES.MODE_CCM, nonce=jv['nonce'])
    cipher.update(jv['header'])
    plaintext = cipher.decrypt_and_verify(jv['ciphertext'], jv['tag'])
    print("The message was: ",plaintext)
except Exception as e:
    print("Incorrect decryption", e)