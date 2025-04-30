# app.py

import os
import numpy as np
from flask import Flask, render_template, request
import tensorflow as tf 
from werkzeug.utils import secure_filename
from PIL import Image
import io

app = Flask(__name__)

# Load pre-trained model (ensure this is in the same directory as app.py)
model = tf.keras.models.load_model('cat_dog_classifier.keras')

# Allowed file extensions for uploading
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def prepare_image(image):
    img = Image.open(image)
    img = img.resize((32, 32))  # Resize image to match model input
    img = np.array(img) / 255.0   # Normalize the image
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    return img

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join('static/uploaded_images', filename)
        file.save(filepath)
        
        # Prepare the image
        image = prepare_image(filepath)
        
        # Predict the class (Cat or Dog)
        result = model.predict(image)
        pred_prob = result.item()  # Get the probability
        
        # Classify as Dog or Cat based on the probability
        if pred_prob > 0.5:
            label = 'Dog'
            accuracy = round(pred_prob * 100, 2)
        else:
            label = 'Cat'
            accuracy = round((1 - pred_prob) * 100, 2)
        
        return render_template('index.html', label=label, accuracy=accuracy, image_path=filepath)
    
    return "Invalid file format. Please upload an image."

# if __name__ == '__main__':
#     app.run(debug=True)
