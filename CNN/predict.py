import torch
import torch.nn as nn
from torchvision.models import mobilenet_v2
from torchvision import transforms
from PIL import Image

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

checkpoint = torch.load("rail_defect_model.pth", map_location=device)
classes = checkpoint["classes"]

model = mobilenet_v2()
model.classifier[1] = nn.Linear(model.last_channel, len(classes))
model.load_state_dict(checkpoint["model_state"])
model = model.to(device)
model.eval()

transform = transforms.Compose([
    transforms.CenterCrop((640,220)),
    transforms.Resize((256,256)),
    transforms.ToTensor(),
    transforms.Normalize([0.485,0.456,0.406],
                         [0.229,0.224,0.225])
])

img_path = r"D:\IMAGE_processing\TRAIN_TRACK\img_2.png"

image = Image.open(img_path).convert("RGB")
image = transform(image).unsqueeze(0).to(device)

with torch.no_grad():
    output = model(image)
    prob = torch.softmax(output, dim=1)
    pred = torch.argmax(prob,1)

label = classes[pred.item()]
confidence = prob[0][pred].item()

if label == "defect":
    print(f"DEFECT DETECTED ({confidence:.2f})")
else:
    print(f"RAIL NORMAL ({confidence:.2f})")