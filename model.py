import torch
import torch.nn as nn
import torch.nn.functional as F
import timm
from torchvision import transforms
from PIL import Image
import json
import os

# Get absolute path to project directory
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

# Load class names
class_names_path = os.path.join(PROJECT_DIR, "class_names.json")
if not os.path.exists(class_names_path):
    raise FileNotFoundError(f"class_names.json not found at {class_names_path}")

with open(class_names_path, "r") as f:
    class_names = json.load(f)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# Load model
model_path = os.path.join(PROJECT_DIR, "efficientnet_plant_best.pth")
if not os.path.exists(model_path):
    raise FileNotFoundError(f"efficientnet_plant_best.pth not found at {model_path}")

try:
    model = timm.create_model("efficientnet_b0", pretrained=False)
    model.classifier = nn.Linear(model.classifier.in_features, len(class_names))
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.to(device)
    model.eval()
    print(f"✅ Model loaded! Total classes: {len(class_names)}")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    raise

# Transform sesuai dengan training (tanpa normalization!)
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

def predict(image: Image.Image):
    input_tensor = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        outputs = model(input_tensor)
        probs = F.softmax(outputs, dim=1)

    # Top 1
    confidence, predicted = torch.max(probs, 1)
    predicted_class = class_names[predicted.item()]
    confidence_score = confidence.item() * 100

    # Top 5
    top5_probs, top5_indices = torch.topk(probs, 5)
    top5 = [
        {
            "class": class_names[idx.item()],
            "confidence": f"{prob.item() * 100:.2f}%"
        }
        for prob, idx in zip(top5_probs[0], top5_indices[0])
    ]

    return {
        "class": predicted_class,
        "confidence": confidence_score,
        "top5": top5
    }