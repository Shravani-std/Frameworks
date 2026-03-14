import torch
from torchvision import transforms

def get_transform():
    transform = transforms.Compose([
        transforms.Resize([224,224]),
        transforms.ToTensor()
    ])

    return transform

def preprocess_img(image):
    transform = get_transform()
    image = transform(image)
    image = image.unsqueeze(0)

    return image