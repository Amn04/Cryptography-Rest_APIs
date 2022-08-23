from flask import request
from flask_restful import Resource, reqparse
import json
from base64 import b64decode
from Crypto.Cipher import AES
from main import app

class Aes_decrypt_class(Resource):
    
    def get(self):
        key_state = False
        app.logger.info("Decryption started")
        
        try:
            nonce = request.form.get('nonce')
            header = request.form.get('head')
            cipher_text = request.form.get('text')
            tag = request.form.get('tag')
            key = request.form.get('key')

            cipher = AES.new(key, AES.MODE_CCM, nonce=b64decode(nonce))

            cipher.update(b64decode(header))
            plaintext = cipher.decrypt_and_verify(b64decode(cipher_text), b64decode(tag))

            return {'message':'Decryption successfull',
                    'plain_text': plaintext}, 200
        
        except Exception as e:
            return {'error':'something went wrong'},500