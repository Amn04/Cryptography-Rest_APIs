from flask import request
from flask_restful import Resource, reqparse
import json
from base64 import b64decode
from Crypto.Cipher import AES
from main import app

class Aes_decrypt_ccm(Resource):
    
    def get(self):
        key_state = False
        app.logger.info("Inside decryption class")
        
        try:
            nonce = request.form.get('nonce')
            header = request.form.get('head')
            cipher_text = request.form.get('text')
            tag = request.form.get('tag')
            key = request.files.get('key')

            if nonce == None or nonce=="" or nonce==" ":
                return {'error':'nonce required in ccm'},201
            else:
                nonce=nonce

            if header == None or header=="" or header==" ":
                return {'error':'header required in ccm'},201
            else:
                header=header

            if cipher_text == None or cipher_text=="" or cipher_text==" ":
                return {'error':'cipher_text required in ccm'},201
            else:
                cipher_text=cipher_text

            if tag == None or tag=="" or tag==" ":
                return {'error':'tag required in ccm'},201
            else:
                tag=tag

            if key == None or key=="" or key==" ":
                return {'error':'Key required'},201
            else:
                key=key.read()

            app.logger.info("Args check successfully")
            
            cipher = AES.new(key.read(), AES.MODE_CCM, nonce=b64decode(nonce))
            cipher.update(b64decode(header))
            plaintext = cipher.decrypt_and_verify(b64decode(cipher_text), b64decode(tag))

            app.logger.info("Decrption successful")

            return {'message':'Decryption successful',
                    'plain_text': str(plaintext)}, 200
        
        except Exception as e:
            print(e)
            return {'error':'something went wrong'},500