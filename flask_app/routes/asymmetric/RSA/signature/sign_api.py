from flask import request
from flask_restful import Resource, reqparse
from flask import send_file
import json
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from main import app
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

class rsa_sign(Resource):

    def get(self):
        '''
        This is a get method API implemented for RSA signing of message. In this API
        data and private key should be passed as files in form data. After successfull
        signing, a success message and signature will be returned. If a error happens 
        API will return internal server error message.
        Algorithm for siganture is fixed.
        '''
        app.logger.info("In rsa_sign class")
        try:
            #Arguments collection
            data=request.files.get("data")
            key = request.files.get("key")

            app.logger.info("Args loaded successful")
        
            private_key = serialization.load_pem_private_key(
                key.read(),
                password=None,
                backend=default_backend()
            )

            app.logger.info("Private key loaded")

            signature = private_key.sign(
                    data.read(),
                    padding.PSS(
                        mgf=padding.MGF1(hashes.SHA256()),
                        salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )

            app.logger.info("Signing successful")

            return {"message":"success",
                    "Signature":str(signature)
            },200
        except Exception as e:
            app.logger.error(f"Error occured - {e}")
            return {"error":"Internal server error"}, 500

        