from torch.utils.data import DataLoader 

def get_loader(dataset, batch_size):
    loader = DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=True,
        num_workers = 4
    )

    return loader