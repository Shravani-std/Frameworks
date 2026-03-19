import torch #type:ignore
import torch.nn as nn #type:ignore
import torch.optim as optim #type:ignore

from models.transfer_learn import get_model
from datasets.dataset import get_dataset
from datasets.loader import get_loader
from training.trainer import train_epoch
from datasets.transforms import get_transforms

# device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Using device:", device)

train_transform, val_transform = get_transforms(224)

model = get_model(num_classes=38)   # PlantVillage has 38 classes
model = model.to(device)

# loss function
criterion = nn.CrossEntropyLoss()

# optimizer
optimizer = optim.Adam(
    model.parameters(),
    lr=0.001
)

# dataset
dataset = get_dataset( "D:\\AI\\Frameworks\\Pytorch\\Projects\\CNN\\data\\PlantVillage", train_transform)

# dataloader
train_loader = get_loader(dataset, batch_size=32)

# training loop
def main():
    for epoch in range(30):

        loss = train_epoch(
            model,
            train_loader,
            criterion,
            optimizer,
            device
        )

        print(f"Epoch: {epoch+1}, Loss: {loss:.4f}")
    # save model
    torch.save({
        "epoch": epoch,
        "model_state": model.state_dict(),
        "optimizer_state": optimizer.state_dict()
    }, "outputs/checkpoint.pth")


if __name__ == "__main__":
    main()