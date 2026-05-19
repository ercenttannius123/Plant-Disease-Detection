import torch
import torch.nn.functional as F
from torchvision import transforms
import timm
import json
from PIL import Image
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CLASS_NAMES_PATH = BASE_DIR / 'class_names.json'
MODEL_PATH = BASE_DIR / 'efficientnet_plant_best.pth'

# Load class names
with open(CLASS_NAMES_PATH, 'r', encoding='utf-8') as f:
    class_names = json.load(f)

# Model configuration
MODEL_NAME  = 'efficientnet_b0'
NUM_CLASSES = len(class_names)
DEVICE      = 'cuda' if torch.cuda.is_available() else 'cpu'

# Load model
model = timm.create_model(MODEL_NAME, pretrained=False, num_classes=NUM_CLASSES)
model.load_state_dict(torch.load(MODEL_PATH, map_location=DEVICE))
model = model.to(DEVICE)
model.eval()

# ✅ Sama persis dengan val_transforms di training — TANPA Normalize
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

def predict(image: Image.Image) -> dict:
    image        = image.convert('RGB')
    input_tensor = transform(image).unsqueeze(0).to(DEVICE)
    with torch.no_grad():
        outputs       = model(input_tensor)
        probabilities = F.softmax(outputs, dim=1)
        confidence, predicted = torch.max(probabilities, 1)

    top5_prob, top5_indices = torch.topk(probabilities[0], 5)

    predicted_class  = class_names[predicted.item()]
    confidence_score = confidence.item() * 100

    top5_predictions = [
        {
            "class":      class_names[idx.item()],
            "confidence": f"{prob.item() * 100:.2f}%"
        }
        for prob, idx in zip(top5_prob, top5_indices)
    ]

    return {
        "class":      predicted_class,
        "confidence": confidence_score,
        "top5":       top5_predictions
    }
