from routes.symmetric.AES.AES_CCM.AES_CCM_decrypt import Aes_decrypt_ccm
from main import app
from flask_restful import Api

from routes.symmetric.AES.AES_CCM.AES_CCM_encrypt import Aes_encrypt_ccm
from routes.home import Home

api = Api(app)

api.add_resource(Home,"/")
api.add_resource(Aes_encrypt_ccm,"/symmetric/encrypt/aes/ccm")
api.add_resource(Aes_decrypt_ccm,"/symmetric/decrypt/aes/ccm")

if __name__ == '__main__':
    app.logger.info("Flask App started successfully")
    app.run(debug=True, port=5000)