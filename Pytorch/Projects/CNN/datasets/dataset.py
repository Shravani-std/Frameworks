import os 
from torchvision import datasets

def get_dataset(path, transform):
    dataset = datasets.ImageFolder(
        root=path,
        transform=transform
    )

    return dataset