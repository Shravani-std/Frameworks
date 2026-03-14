import torch.nn as nn # type:ignore
from torchvision.models import resnet18, ResNet18_Weights # type:ignore



def get_model(num_classes):

    model = resnet18(weights=ResNet18_Weights.DEFAULT)

    for params in model.parameters():
        params.requires_grad = False
    
    in_features = model.fc.in_features

    model.fc = nn.Linear(in_features, num_classes)

    return model