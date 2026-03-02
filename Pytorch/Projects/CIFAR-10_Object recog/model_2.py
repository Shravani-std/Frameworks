import torch
import torch.nn as nn
import torchvision.models as models
import torch #type:ignore
import torch.nn as nn #type:ignore
from torch.utils.data import DataLoader #type:ignore
from torchvision import datasets, transforms #type:ignore
import torchvision.models as models #type:ignore

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
transform = transforms.ToTensor()

training_data = datasets.CIFAR10(
    root="./data",
    train=True,
    download=True,
    transform=transform
)

test_data = datasets.CIFAR10(
    root="./data",
    train=False,
    download=True,
    transform=transform
)

train_dataloader = DataLoader(training_data, batch_size=64, shuffle=True)
test_dataloader = DataLoader(test_data, batch_size=64)


class VGG_CIFAR(nn.Module):
    def __init__(self):
        super().__init__()
        
        vgg = models.vgg16(weights=None)

        self.features = vgg.features
        self.avgpool = nn.AdaptiveAvgPool2d((1,1))
        self.classifier = nn.Linear(512, 10)

    def forward(self, x):
        x = self.features(x)
        x = self.avgpool(x)
        x = torch.flatten(x, 1)   # Correct flatten
        x = self.classifier(x)
        return x

model = VGG_CIFAR().to(device)

optimizer = torch.optim.Adam(model.parameters(), lr=0.0003)
loss_fn = nn.CrossEntropyLoss()