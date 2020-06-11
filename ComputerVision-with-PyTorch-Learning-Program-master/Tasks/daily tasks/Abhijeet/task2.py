import torch.nn as nn
import torch.nn.functional as F


class Network(nn.Module):
    def __init__(self):
        super(Network, self).__init__()
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.Output = nn.Linear(84, 10)

    def forward(self, x):
        x= self.fc1(x)
        x = F.Sigmoid(x)
        x=self.fc2(x)
        x = F.Sigmoid(x)
        x = self.fc3(x)
        return x


net = Network()
print(net)