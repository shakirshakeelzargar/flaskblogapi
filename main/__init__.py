from flask import Flask
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
application = Flask(__name__,template_folder=os.path.join(dir_path,"templatess"))
from main import routes 