from deepface import DeepFace
from flask import Flask,request
import os ,cv2

api = Flask(__name__)
UPLOAD_PATH = "/uploads"
api.config['UPLOAD_PATH'] = os.path.join(api.instance_path,"uploads")
os.makedirs(api.config["UPLOAD_PATH"], exist_ok=True)


#todo : add more information about the api here on this route
@api.route("/")
def info():
    info = "Test"
    return info

#endpoint for facial emotion recognition
@api.route("/emotions" , methods=["POST"])
def emotions():
    #getting image from the request sent by the client
    image =  request.files['image']  

    #saving the image locally on the server 
    image.save(os.path.join(api.config['UPLOAD_PATH'] , image.filename))

    #performing analysis on emotions
    img = cv2.imread(f"{api.config['UPLOAD_PATH']}"+f'/{image.filename}')
    result =  DeepFace.analyze(img ,actions=["emotion"])
    
    #deleting the image because there is no need to store the image on the server
    os.remove(f"{api.config['UPLOAD_PATH']}"+f'/{image.filename}')

    #returning the data after analysis
    return result

api.run(host = "localhost" , debug=True, threaded=True)