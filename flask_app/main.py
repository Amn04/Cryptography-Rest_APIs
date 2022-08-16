from flask import Flask
from flask_restful import Api
from flask_cors import CORS
import logging



logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)
api = Api(app)

app.config['JSON_SORT_KEYS'] = False
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app, supports_credentials=True, resources={r"/*": {"origins": ["*", "http://localhost:3000", "http://localhost:3001", "http://localhost:5000"]}})

app.logger.info("Logging is set up.")


    