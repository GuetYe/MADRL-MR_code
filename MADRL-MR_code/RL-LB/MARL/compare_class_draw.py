# @Project : Experiment-code
# @File    : compare_class_draw.py
# @IDE     : PyCharm
# @Author  : hhw
# @Date    : 2022/12/27 18:57
# @Describe:
# @Update  :
import random

import numpy as np

from draw_tools import draw_compare_exp, draw_compare_exp_plus, draw_compare_exp_bar
from utils import load_experimental_data, save_experimental_data, max_min_normalize, compute_ratio



path = "D:/Users/Projects/PycharmProjects/experiment-code/"
exp_data = []
exp_bar_data = []

# 1、颜色
# 'royalblue', 'limegreen', 'deeppink', 'darkorange'
# 'red', 'royalblue'
# 'red', 'limegreen',
pic_color = ['red', 'royalblue', 'limegreen', 'darkorange']

# 2、标签名
# "single_agent", "two_agents", "three_agents", "four_agents", "MARL-MR", "DuelingDQN"
# "Using transfer learning", "Without Using transfer learning"
# "MADRL-MR" "kmb_bw", "kmb_delay", "kmb_loss"
label_name = ["MADRL-MR", "KMB_bw", "KMB_delay", "KMB_loss"]

# 3、坐标轴和图标题名
# 'average throughput', 'throughput'
# 'average delay', 'delay'
# 'average loss', 'loss'
# 'average bw', 'bandwidth'
# 'average length', 'length'
# 'average distance', 'distance'
xyt_label = ['traffic', 'average distance', 'distance']

# 4、点形状和线形状
marker = '*'
line_style = '-'

# 5、 数据路径
path1 = 'RL-LB/MARL/compare_exp/compare_marl_and_kmb/distance/bar_KMB_distance.pkl'
path2 = 'RL-LB/MARL/compare_exp/compare_marl_and_kmb/distance/bar_MARL_distance.pkl'


# ------------------------------------------------------------------------------------#
# 解析分数据
kmb_data = load_experimental_data(path + path1)
kmb_bw, kmb_delay, kmb_loss = kmb_data[0], kmb_data[1], kmb_data[2]

marl_data = load_experimental_data(path + path2)
# ------------------------------------------------------------------------------------#

exp_data.append(np.array(marl_data))
exp_data.append(np.array(kmb_bw))
exp_data.append(np.array(kmb_delay))
exp_data.append(np.array(kmb_loss))

draw_compare_exp_bar(exp_data, label_name, pic_color, xyt_label)

