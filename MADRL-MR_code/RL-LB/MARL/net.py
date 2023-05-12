# @Project : Experiment-code 
# @File    : net.py
# @IDE     : PyCharm 
# @Author  : hhw
# @Date    : 2022/11/24 21:03 
# @Describe:
# @Update  :
import numpy
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import config
from utils import combine_state


class Actor(nn.Module):
    def __init__(self):
        super(Actor, self).__init__()
        self.conv1 = nn.Conv2d(config.STATE_NUM, 32, kernel_size=1)
        self.fc1 = nn.Linear(32*14, 32)
        self.fc2 = nn.Linear(32, 16)
        self.action_head = nn.Linear(16, config.ACTION_NUM)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = x.view(-1, 32*14)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        action_prob = F.softmax(self.action_head(x), dim=1)
        return action_prob


class Critic(nn.Module):
    def __init__(self):
        super(Critic, self).__init__()
        self.conv1 = nn.Conv2d(config.STATE_NUM, 32, kernel_size=1)
        self.fc1 = nn.Linear(32 * 14, 32)
        self.fc2 = nn.Linear(32, 16)
        self.state_value = nn.Linear(16, 1)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = x.view(-1, 32 * 14)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        value = self.state_value(x)
        return value


