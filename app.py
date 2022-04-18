from flask import Flask, render_template, request, redirect, flash, url_for
from keras.models import load_model

import os, cv2

import numpy as np

import os
import uuid
import urllib
from PIL import Image
from tensorflow.keras.models import load_model
from flask import Flask , render_template  , request , send_file
from tensorflow.keras.preprocessing.image import load_img , img_to_array

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
chest = load_model(os.path.join(BASE_DIR , 'resnet50.h5'))
ctscan = load_model(os.path.join(BASE_DIR , 'xception.h5'))


ALLOWED_EXT = set(['jpg' , 'jpeg' , 'png' , 'jfif'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXT

classes = ['COVID19','NORMAL','PNEUMONIA','TURBERCULOSIS']
classesct = ['COVID','NON COVID']
# CHEST

def predict(filename , model):
    img = load_img(filename , target_size = (224 , 224))
    img = img_to_array(img)
    img = img.reshape(1 , 224 ,224 ,3)

    img = img.astype('float32')
    img = img/255.0
    result = chest.predict(img)

    dict_result = {}
    for i in range(4):
        dict_result[result[0][i]] = classes[i]

    res = result[0]
    res.sort()
    res = res[::-1]
    prob = res[:4]
    
    prob_result = []
    class_result = []
    for i in range(4):
        prob_result.append((prob[i]*100).round(2))
        class_result.append(dict_result[prob[i]])

    return class_result , prob_result

@app.route('/')
def home():
        return render_template("index.html")

@app.route('/success' , methods = ['GET' , 'POST'])
def success():
    error = ''
    target_img = os.path.join(os.getcwd() , 'static/images')
    if request.method == 'POST':
        if (request.files):
            file = request.files['file']
            if file and allowed_file(file.filename):
                file.save(os.path.join(target_img , file.filename))
                img_path = os.path.join(target_img , file.filename)
                img = file.filename

                class_result , prob_result = predict(img_path , chest)

                predictions = {
                       "class1":class_result[0],
                        "class2":class_result[1],
                        "class3":class_result[2],
                        "class4":class_result[3],
                        "prob1": prob_result[0],
                        "prob2": prob_result[1],
                        "prob3": prob_result[2],
                        "prob4": prob_result[3],
                }

            else:
                error = "Please upload images of jpg , jpeg and png extension only"

            if(len(error) == 0):
                return  render_template('success.html' , img  = img , predictions = predictions)
            else:
                return render_template('index.html' , error = error)

    else:
        return render_template('index.html')

# CT_SCAN

def prediction(filename , model):
    img = load_img(filename , target_size = (299 , 299))
    img = img_to_array(img)
    img = img.reshape(1 , 299 ,299 ,3)

    img = img.astype('float32')
    img = img/255.0
    result = ctscan.predict(img)

    dict_result = {}
    for i in range(2):
        dict_result[result[0][i]] = classesct[i]

    res = result[0]
    res.sort()
    res = res[::-1]
    prob = res[:2]
    
    prob_result = []
    class_result = []
    for i in range(2):
        prob_result.append((prob[i]*100).round(2))
        class_result.append(dict_result[prob[i]])

    return class_result , prob_result


@app.route('/success_ct' , methods = ['GET' , 'POST'])
def uploaded_ct():
    error = ''
    target_img = os.path.join(os.getcwd() , 'static/images/ct')
    if request.method == 'POST':
        if (request.files):
            file = request.files['file']
            if file and allowed_file(file.filename):
                file.save(os.path.join(target_img , file.filename))
                img_path = os.path.join(target_img , file.filename)
                img = file.filename

                class_result , prob_result = prediction(img_path , ctscan)

                predictions = {
                       "class1":class_result[0],
                        "class2":class_result[1],
                        "prob1": prob_result[0],
                        "prob2": prob_result[1],
                }

            else:
                error = "Please upload images of jpg , jpeg and png extension only"

            if(len(error) == 0):
                return  render_template('success_ct.html' , img  = img , predictions = predictions)
            else:
                return render_template('index.html' , error = error)

    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug = True)


