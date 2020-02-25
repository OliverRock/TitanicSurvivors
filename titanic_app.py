from flask import Flask
from flask_restful import Api
from titanic_resource import Survivor

#Create flask app
app = Flask(__name__)
api = Api(app)
#Add resource for survivor
api.add_resource(Survivor, '/survivor/')
#Start App
app.run(port=5000)
