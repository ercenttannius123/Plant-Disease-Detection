# 🌿 Plant Disease Detection

AI-powered plant disease detection system using EfficientNet deep learning model with React frontend and FastAPI backend.

![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![React](https://img.shields.io/badge/React-18.2-61dafb)
![License](https://img.shields.io/badge/License-MIT-green)

## ✨ Features

- 🎯 **38 Plant Disease Classes** - Detect diseases across multiple plant types
- 🧠 **EfficientNet-B0 Model** - Pre-trained deep learning model for high accuracy
- 💻 **Modern React UI** - Beautiful, responsive web interface
- 🚀 **FastAPI Backend** - High-performance REST API
- 📊 **Top-5 Predictions** - Shows confidence scores for multiple predictions
- 📥 **Drag & Drop Upload** - User-friendly image upload interface
- 💾 **Export Results** - Download analysis results as text file
- 🎨 **Green Theme** - Professional and ecological color scheme

## 🛠️ Tech Stack

### Frontend
- **React 18.2** - UI library
- **Vite 5.0** - Build tool & dev server
- **Axios** - HTTP client
- **CSS3** - Styling with animations

### Backend
- **FastAPI** - Modern Python web framework
- **PyTorch 2.2** - Deep learning framework
- **TIMM** - EfficientNet model
- **Pillow** - Image processing

## 📋 Prerequisites

- Python 3.8+
- Node.js 16+
- npm 7+
- GPU (optional, CPU works too)

## 🚀 Installation

### 1. Clone Repository
```bash
git clone https://github.com/YOUR_USERNAME/plant-disease-detection.git
cd plant-disease-detection
```

### 2. Backend Setup
```bash
# Install Python dependencies
pip install -r requirements.txt

# Verify model files exist
# - efficientnet_plant_best.pth (model weights)
# - class_names.json (disease labels)
```

### 3. Frontend Setup
```bash
# Install Node dependencies
npm install

# Create environment file
copy .env.example .env.local
# OR manually create .env.local with:
# VITE_API_URL=http://localhost:8000
```

## 🏃 Running the Application

### Terminal 1: Start Backend
```bash
python run_server.py
# OR
python -m uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

Expected output:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
✅ Model loaded! Total classes: 38
INFO:     Application startup complete.
```

### Terminal 2: Start Frontend
```bash
npm run dev
```

Browser will open automatically at `http://localhost:5173`

## 🎯 Usage

1. **Upload Image**
   - Drag & drop plant image OR click to select file
   - Supported formats: JPG, PNG, GIF, WebP

2. **Get Analysis**
   - Click "Analisis Sekarang" button
   - Wait for prediction results

3. **View Results**
   - Top predicted disease with confidence score
   - Top 5 predictions with percentages
   - Confidence visualization bars

4. **Export Results**
   - Click "Download Hasil" to save as text file
   - Click "Analisis Gambar Lain" for new analysis

## 📁 Project Structure

```
plant-disease-detection/
├── backend/
│   ├── app.py                      # FastAPI application
│   ├── model.py                    # Model loading & inference
│   ├── run_server.py               # Server launcher
│   ├── requirements.txt            # Python dependencies
│   ├── efficientnet_plant_best.pth # Model weights
│   └── class_names.json            # Disease labels
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx                 # Main React component
│   │   ├── App.css                 # Base styles
│   │   ├── components.css          # Component styles
│   │   ├── main.jsx                # React entry point
│   │   └── components/
│   │       ├── Header.jsx
│   │       ├── UploadSection.jsx
│   │       ├── ResultsSection.jsx
│   │       ├── ErrorSection.jsx
│   │       └── Footer.jsx
│   ├── index.html
│   ├── vite.config.js
│   ├── package.json
│   └── .env.local
│
├── .gitignore
├── README.md
```

## 🔌 API Endpoints

### GET /
Returns API status
```bash
curl http://localhost:8000/
```
Response:
```json
{
  "message": "Plant Disease Detection API is running 🌿"
}
```

### POST /predict
Upload image and get disease prediction
```bash
curl -X POST -F "file=@plant_image.jpg" http://localhost:8000/predict
```

Request:
- `file` (FormData): Plant image file

Response:
```json
{
  "predicted_class": "Apple___Apple_scab",
  "confidence": "95.43%",
  "top5": [
    {
      "class": "Apple___Apple_scab",
      "confidence": "95.43%"
    },
    {
      "class": "Apple___Black_rot",
      "confidence": "3.21%"
    }
  ]
}
```

## 📊 Supported Plant Diseases (38 Classes)

The model can detect diseases for:
- **Apple**: Apple scab, Black rot, Cedar rust, Healthy
- **Blueberry**: Healthy, Mummy berry
- **Cherry**: Powdery mildew, Healthy
- **Corn**: Cercospora leaf spot, Common rust, Northern leaf blight, Healthy
- **Grape**: Black measles, Esca, Leaf blight, Healthy
- **Orange**: Haunglongbing
- **Peach**: Bacterial spot, Healthy
- **Pepper**: Bacterial spot, Healthy
- **Potato**: Early blight, Late blight, Healthy
- **Raspberry**: Healthy
- **Soybean**: Brown spot, Cankered stem, Frog eye leaf spot, Powdery mildew, Healthy
- **Squash**: Powdery mildew
- **Strawberry**: Angular leaf spot, Healthy
- **Tomato**: Bacterial spot, Early blight, Late blight, Leaf mold, Septoria leaf spot, Spider mites, Target spot, Tomato mosaic virus, Healthy
- **Background**: Images without plants

## 🎨 Features Detail

### Image Recognition
- Input size: 224x224 pixels
- Model: EfficientNet-B0
- Accuracy: ~95% on validation set
- Inference time: ~500ms (CPU)

### UI Components
- **Header**: Title with animated leaf icons
- **UploadSection**: Drag-drop area with file preview
- **ResultsSection**: Diagnosis display with confidence charts
- **ErrorSection**: Error message handling
- **Footer**: App credits

## 🐛 Troubleshooting

### Backend Error: NumPy version incompatibility
```bash
pip install "numpy<2"
```

### Frontend connection error
- Ensure backend is running on `http://localhost:8000`
- Check `.env.local` has correct `VITE_API_URL`
- Restart dev server

### Model loading error
- Verify `efficientnet_plant_best.pth` exists
- Check `class_names.json` is valid JSON
- Ensure PyTorch is properly installed

## 📈 Performance

- **Model Size**: ~100MB
- **CPU Inference**: ~500-1000ms
- **GPU Inference**: ~100-200ms
- **Supported Concurrent Requests**: Depends on system resources

## 🔒 Security Notes

- Change CORS settings for production (`app.py`)
- Add authentication for API endpoints
- Validate file uploads strictly
- Deploy behind reverse proxy (nginx/Apache)


## 🙏 Acknowledgments

- **Dataset**: PlantVillage Dataset
- **Model**: EfficientNet-B0 from timm library
- **Framework**: FastAPI, React, PyTorch


## 🚀 Future Enhancements

- [ ] Mobile app (React Native)
- [ ] Real-time camera analysis
- [ ] Multi-image batch processing
- [ ] Model quantization for mobile
- [ ] User authentication & history
- [ ] Advanced analytics dashboard
- [ ] Multi-language support
- [ ] Treatment recommendations

---

**Happy Disease Detection! 🌿🤖**

Made with ❤️ for Plant Health
