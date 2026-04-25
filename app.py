from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from PIL import Image
import io

from model import predict

app = FastAPI(
    title="Plant Disease Detection API",
    description="API untuk deteksi penyakit tanaman menggunakan EfficientNet",
    version="1.0.0"
)



# CORS - allow semua origin (bisa dibatasi nanti)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Plant Disease Detection API is running 🌿"}

@app.post("/predict")
async def predict_disease(file: UploadFile = File(...)):
    # Validasi file
    if not file.content_type.startswith("image/"):
        return JSONResponse(
            status_code=400,
            content={"error": "File harus berupa gambar (jpg/png)"}
        )

    # Baca gambar
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    # Prediksi
    result = predict(image)

    return {
        "predicted_class": result["class"],
        "confidence": f"{result['confidence']:.2f}%",
        "top5": result["top5"]
    }

@app.get("/classes")
def get_classes():
    import json
    with open("class_names.json", "r") as f:
        classes = json.load(f)
    return {"total": len(classes), "classes": classes}