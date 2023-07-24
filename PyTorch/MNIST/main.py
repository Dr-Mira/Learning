import torch
import torch.nn as nn
from torch.optim import SGD
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
import torchvision
import numpy as np
import matplotlib.pyplot as plt


def main():
    picture, label = torch.load('.\\Data\\processed\\training.pt')

    plt.imshow(picture[0].numpy())
    plt.title(f'This is number {label[0]}')
    plt.show()


if __name__ == '__main__':
    main()
