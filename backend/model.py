import torch
import torch.nn.functional as F
from torchvision import transforms
import timm
import json
from PIL import Image

# Load class names
with open('class_names.json', 'r') as f:
    class_names = json.load(f)

# Model configuration
MODEL_NAME = 'efficientnet_b0'
NUM_CLASSES = len(class_names)
DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'

# Load model
model = timm.create_model(MODEL_NAME, pretrained=False, num_classes=NUM_CLASSES)
model.load_state_dict(torch.load('efficientnet_plant_best.pth', map_location=DEVICE))
model = model.to(DEVICE)
model.eval()

# Image preprocessing
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

def predict(image: Image.Image) -> dict:
    """
    Predict plant disease from image
    
    Args:
        image: PIL Image object
        
    Returns:
        dict with predicted class, confidence, and top 5 predictions
    """
    # Preprocess image
    input_tensor = transform(image).unsqueeze(0).to(DEVICE)
    
    # Inference
    with torch.no_grad():
        outputs = model(input_tensor)
        probabilities = F.softmax(outputs, dim=1)
        confidence, predicted = torch.max(probabilities, 1)
    
    # Get top 5 predictions
    top5_prob, top5_indices = torch.topk(probabilities[0], 5)
    
    predicted_class = class_names[predicted.item()]
    confidence_score = confidence.item() * 100
    
    top5_predictions = [
        {
            "class": class_names[idx.item()],
            "confidence": f"{prob.item() * 100:.2f}%"
        }
        for prob, idx in zip(top5_prob, top5_indices)
    ]
    
    return {
        "class": predicted_class,
        "confidence": confidence_score,
        "top5": top5_predictions
    }
