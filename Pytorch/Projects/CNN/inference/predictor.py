import torch
from inference.preprocessing import preprocess_img
from models.transfer_learn import get_model
from PIL import Image

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load Model
model = get_model(num_classes=38)
checkpoint = torch.load(
    "D:\\AI\\Frameworks\\Pytorch\\Projects\\CNN\\outputs\\checkpoint.pth",
    map_location=device
)
model.load_state_dict(checkpoint["model_state"])
model.to(device)
model.eval()

class Predictor:

    def __init__(self,model):
        self.model = model
        self.model.eval()

    def predict(self,image: Image.Image):
        image = preprocess_img(image)
        image = image.to(device)

        with torch.no_grad():
            output = self.model(image)
            pred = torch.argmax(output, dim=1)
        
        return pred.item()