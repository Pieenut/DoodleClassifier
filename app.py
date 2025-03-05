import base64
import numpy as np
import io
from PIL import Image
import tensorflow as tf
from tensorflow import keras
from keras import models
from keras.models import Sequential, load_model
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

classes = ['star', 'house', 'umbrella', 't-shirt', 'windmill', 'shoe', 'duck', 'popsicle', 'airplane', 'piano']

def get_model():
    global model
    model = tf.keras.models.load_model("keras.h5")
    print("Model Loaded")
    
def preprocess_img(image, target_size, inv):
    image = image.convert("L")
    image = image.resize(target_size)
    if inv==True :
        image=np.invert(image)
    image = tf.keras.utils.img_to_array(image)
    image = np.expand_dims(image, axis=0)
    return image    

print("loading model...")
get_model()

@app.route('/')
def index():
	return render_template("index.html")
    

@app.route("/predict-image/", methods = ["GET","POST"])
def predict_img():
    message = request.get_json(force=True)
    encoded = message["image"]
    decoded = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(decoded))
    processed_img = preprocess_img(image, target_size=(28,28), inv=False)
    pred = model.predict(processed_img)
    idx = np.argmax(np.array(pred[0]))
    response = {
            'predictionImg' : str(classes[idx-1])
    }
    return jsonify(response)

@app.route("/predict-drawing/", methods = ["GET","POST"])
def predict_draw():
    message = request.get_json(force=True)
    encoded = message["image"]
    decoded = base64.b64decode(encoded)
    image = Image.open(io.BytesIO(decoded))
    processed_img = preprocess_img(image, target_size=(28,28), inv=True)
    pred = model.predict(processed_img)
    idx = np.argmax(np.array(pred[0]))
    response = {
            'predictionDraw' : str(classes[idx-1])
    }
    return jsonify(response)