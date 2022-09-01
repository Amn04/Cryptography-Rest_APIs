from flask import request
from flask_restful import Resource, reqparse
import json
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from main import app
from Crypto.Util.Padding import pad

class AES_CBC_encrypt(Resource):
    def get(self):
        key_state = False
        app.logger.info("In encryption class")
        
        try:
            #Arguments collection
            data=request.files.get("data")
            key = request.files.get("key")
            
            if data == None or data=="" or data==" ":
                return {"message":"Encryption can be done only if data is provide."}, 201
            else:
                data=data.read()  
                app.logger.info("Data loaded")

            if key == None or key=="" or key==" ":
                key=get_random_bytes(16)     #This will generate 128bit key
                key_state=True
            else:
                key=key.read()

            cipher = AES.new(key, AES.MODE_CBC)
            ct_bytes = cipher.encrypt(pad(data, AES.block_size))
            iv = b64encode(cipher.iv).decode('utf-8')
            ct = b64encode(ct_bytes).decode('utf-8')
            result = {'iv':iv, 'ciphertext':ct}
            print(result)
            if key_state:
                return {'message':'Encryption successful',
                        'result':result,
                        'key_generated':str(key)},200
            else:
                return {'message':'Encryption successful',
                        'result':result},200
        except Exception as e:
            print("Something went wrong ", e)
            app.logger.error(f"Error occured - {e}")
            return {"error":"Internal server error"}, 500