from distutils.log import info
from deepface import DeepFace
from flask  import Flask,request
from flask_restful import Api , Resource
import os ,cv2

request_served = 0
app = Flask(__name__)
api = Api(app)
UPLOAD_PATH = "/uploads"
app.config['UPLOAD_PATH'] = os.path.join(app.instance_path,"uploads")
os.makedirs(app.config["UPLOAD_PATH"], exist_ok=True)

class help(Resource):
#todo : add more information about the api here on this route
    def get(self):
        info = "Test"
        return info


class status(Resource):
    def get(self):
        try:
            return {'data' : f"Running : Served {request_served} since last downtime"}
        except:
            return {'data' :  "API offline"}
#endpoint for facial emotion recognition
class emotions(Resource):
    def post(self):
    #getting image from the request sent by the client
        image =  request.files['image']  

    #saving the image locally on the server 
        image.save(os.path.join(app.config['UPLOAD_PATH'] , image.filename))

    #performing analysis on emotions
        img = cv2.imread(f"{app.config['UPLOAD_PATH']}"+f'/{image.filename}')
        result =  DeepFace.analyze(img ,actions=["emotion"])
    
    #deleting the image because there is no need to store the image on the server
        os.remove(f"{app.config['UPLOAD_PATH']}"+f'/{image.filename}')

    #returning the data after analysis
        return result
api.add_resource(help , "/")
api.add_resource(status, "/status")
api.add_resource(emotions, "/analyze")