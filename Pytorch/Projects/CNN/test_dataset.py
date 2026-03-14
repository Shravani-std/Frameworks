from datasets.dataset import get_dataset
from datasets.transforms import get_transforms

transforms = get_transforms(224)
dataset = get_dataset( "D:\\AI\\Frameworks\\Pytorch\\Projects\\CNN\\data\\PlantVillage", transforms)

print("Total images:", len(dataset))
print("\n")
print("\nClasses:", dataset.classes)

import torch

import torch

print("Torch:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())
print("CUDA version:", torch.version.cuda)
print("GPU:", torch.cuda.get_device_name(0))

import torch

print("Torch:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())
print("CUDA version:", torch.version.cuda)

if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0))