from flask import request
from flask_restful import Resource, reqparse
# import json
# from base64 import b64encode
# from Crypto.Cipher import AES
# from Crypto.Random import get_random_bytes
from main import app

class Home(Resource):
    
    '''
    If home api successfully returned, then your app is in running status. 
    '''
    def get(self):
        return {"This is Home API of cryptography rest api."},200