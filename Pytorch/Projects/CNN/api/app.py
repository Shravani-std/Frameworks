import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from fastapi import FastAPI, UploadFile, File
from PIL import Image
import io

from inference.predictor import Predictor, model
from utils.classes import classes

# Create predictor instance
predictor = Predictor(model)

app = FastAPI(
    title="Plant Disease Detection API",
    description="CNN model for plant disease classification",
    version="1.0"
)


@app.get("/")
def home():
    return {"message": "Plant Disease Detection API running"}


@app.post("/predict")
async def predict_img(file: UploadFile = File(...)):

    contents = await file.read()

    image = Image.open(io.BytesIO(contents)).convert("RGB")

    pred = predictor.predict(image)

    label = classes[pred]

    return {
        "prediction": label
    }