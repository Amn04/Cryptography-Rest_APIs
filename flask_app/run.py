from main import app
from flask_restful import Api

from routes.symmetric.AES.AES_CCM.AES_CCM_encrypt import Aes_encrypt_class
from routes.home import Home

api = Api(app)

api.add_resource(Home,"/")
api.add_resource(Aes_encrypt_class,"/symmetric/encrypt/aes")

if __name__ == '__main__':
    app.logger.info("Flask App started successfully")
    app.run(debug=True, port=5000)