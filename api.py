from fastapi import FastAPI, File, UploadFile
from model_definition import SegmentationModel
import tensorflow as tf
import json

# Initialize FastAPI app
app = FastAPI()

# Load the model
model = SegmentationModel()
model.load_weights('cancer_weights.h5')

@app.post("/")
async def predict(file: UploadFile = File(...)):
    # Read and decode the image
    image_data = await file.read()
    image = tf.image.decode_image(image_data, channels=3)
    image = tf.cast(image, tf.float32) / 255.0
    image = tf.image.resize(image, [256, 256])
    image = tf.expand_dims(image, 0)
    
    # Make prediction
    prediction = model(image)
    
    # Convert to JSON serializable format
    prediction_list = prediction.numpy().tolist()
    
    return {"prediction": json.dumps(prediction_list)}