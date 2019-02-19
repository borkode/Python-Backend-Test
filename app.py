from flask import Flask
import os
dirname = (os.path.dirname(os.path.abspath(__file__)))
app = Flask(__name__)
@app.route('background_process_test')
def background_process_test():
    print ("Hello")
    return "nothing"