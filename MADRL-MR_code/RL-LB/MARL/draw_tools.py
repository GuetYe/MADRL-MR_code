# @Project : Experiment-code 
# @File    : draw_tools.py
# @IDE     : PyCharm 
# @Author  : hhw
# @Date    : 2022/10/14 22:50 
# @Describe:
# @Update  :
import os
import datetime  # 注意要输入这个模块
from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

from utils import save_experimental_data, load_experimental_data
import config

mkdir_time = datetime.datetime.strftime(datetime.datetime.now(), '%Y_%m_%d')  # 这里是文件夹引用时间
figure_save_path = './results/' + mkdir_time + '/reward'  # 指定图片保存路径，给文件夹赋予名字
figure_save_w = './results/' + mkdir_time + '/reward_w'  # 指定图片保存路径，给文件夹赋予名字
graph_save_path = './results/' + mkdir_time + '/graph_3'  # 指定图片保存路径，给文件夹赋予名字
graph_save_e = './results/' + mkdir_time + '/graph_e'  # 指定图片保存路径，给文件夹赋予名字
graph_save_g = './results/' + mkdir_time + '/graph_g'  # 指定图片保存路径，给文件夹赋予名字
# exp_data_save_path = './results/' + mkdir_time + '/compare_exp'  # 指定图片保存路径，给文件夹赋予名字
save_path = './results/' + mkdir_time  # 指定图片保存路径，给文件夹赋予名字


def draw_episode_reward_all(ep_avg_reward, save_name):
    """
    画图：每回合的奖励
    :param ep_avg_reward:
    :return:
    """
    time = datetime.datetime.strftime(datetime.datetime.now(), '%Y_%m_%d_%H_%M_%S')
    # 保存数据
    if not os.path.exists(figure_save_w):
        os.makedirs(figure_save_w)  # 如果不存在目录save_path，则创建
    save_experimental_data(ep_avg_reward, figure_save_w, save_name + time)
    # 画图
    mkfile_time = "picture_" + time  # 这里是文件引用时间
    plt.figure(1)
    plt.plot(ep_avg_reward, label='Mutil_agents')
    plt.legend(loc='best')
    plt.ylabel('Moving average ep reward')
    plt.xlabel('Episode')
    plt.title("Reward")
    if not os.path.exists(figure_save_path):
        os.makedirs(figure_save_path)  # 如果不存在目录figure_save_path，则创建
    plt.grid()
    plt.savefig(os.path.join(figure_save_path, mkfile_time), dpi=400)
    plt.show()


def draw_multicast_tree(nodes, edges):
    """
    画组播树
    :param nodes:
    :param edges:
    :return:
    """
    time = datetime.datetime.strftime(datetime.datetime.now(), '%Y_%m_%d_%H_%M_%S')

    mkfile_time = "graph_" + time  # 这里是文件引用时间
    graph = nx.Graph()
    graph.add_nodes_from(nodes)  # 添加节点2，3
    graph.add_edges_from(edges)

    # pos = nx.spectral_layout(graph)
    nx.draw(graph, with_labels=True, node_size=200)  # 在这里添加属性，添加颜色和大小
    if not os.path.exists(graph_save_path):
        os.makedirs(graph_save_path)  # 如果不存在目录figure_save_path，则创建
    plt.savefig(os.path.join(graph_save_path, mkfile_time), dpi=400)
    plt.show()


def draw_compare_exp(exp_data, label_name, pic_color):
    """
    画对比实验图
    :param exp_data:
    :param label_name:
    :return:
    """
    # 画图
    mkfile_time = "compare_" + datetime.datetime.strftime(datetime.datetime.now(), '%Y_%m_%d_%H_%M_%S')  # 这里是文件引用时间
    plt.figure(2)
    pic_color = pic_color
    for i in range(len(exp_data)):
        plt.plot(exp_data[i], label=label_name[i], linestyle='-', color=pic_color[i])
    plt.legend(loc='best')
    plt.ylabel('Moving average ep reward')
    plt.xlabel('Episode')
    plt.title("Reward")
    if not os.path.exists(config.COMPARE_EXP):
        os.makedirs(config.COMPARE_EXP)  # 如果不存在目录figure_save_path，则创建
    plt.grid()
    plt.savefig(os.path.join(config.COMPARE_EXP, mkfile_time), dpi=400)
    plt.show()


def draw_compare_exp_plus(exp_data, label_name, pic_color, marker, linestyle, xyt_label):
    """
    画图对比实验plus
    :param exp_data:
    :param label_name:
    :param pic_color:
    :param marker:
    :param linestyle:
    :param xyt_label:
    :return:
    """
    # 画图
    mkfile_time = "compare_" + datetime.datetime.strftime(datetime.datetime.now(), '%Y_%m_%d_%H_%M_%S')  # 这里是文件引用时间
    plt.figure(3)
    pic_color = pic_color
    for i in range(len(exp_data)):
        plt.plot(exp_data[i], label=label_name[i], marker=marker, linestyle=linestyle, color=pic_color[i])
    plt.legend(loc='best')
    plt.xlabel(xyt_label[0])
    plt.ylabel(xyt_label[1])
    plt.title(xyt_label[2])
    if not os.path.exists(config.COMPARE_EXP):
        os.makedirs(config.COMPARE_EXP)  # 如果不存在目录figure_save_path，则创建
    plt.grid()
    plt.savefig(os.path.join(config.COMPARE_EXP, mkfile_time), dpi=400)
    plt.show()


def draw_compare_exp_bar(exp_bar_data, bar_label, bar_color, xyt_label):
    """"""
    mkfile_time = "compare_" + datetime.datetime.strftime(datetime.datetime.now(), '%Y_%m_%d_%H_%M_%S')  # 这里是文件引用时间
    size = 12
    x = np.arange(size)

    # 有a/b两种类型的数据，n设置为2
    total_width, n = 0.8, len(exp_bar_data)
    # 每种类型的柱状图宽度
    width = total_width / n

    list1 = exp_bar_data[0]
    list2 = exp_bar_data[1]
    list3 = exp_bar_data[2]
    list4 = exp_bar_data[3]

    # 重新设置x轴的坐标
    x = x - (total_width - width) / n
    # print(x)
    plt.rcParams['font.serif'] = ['Times New Roman']
    # 画柱状图
    plt.bar(x, list1, width=width, label=bar_label[0], color=bar_color[0])
    plt.bar(x + width, list2, width=width, label=bar_label[1], color=bar_color[1])
    plt.bar(x + 2*width, list3, width=width, label=bar_label[2], color=bar_color[2])
    plt.bar(x + 3*width, list4, width=width, label=bar_label[3], color=bar_color[3])
    plt.xticks(np.arange(size), ('1:00', '3:00', '5:00', '7:00', '9:00', '11:00', '13:00',
                                 '15:00', '17:00', '19:00', '21:00', '23:00'))
    # 显示图例
    plt.legend(loc='best')
    plt.xlabel("time")
    plt.ylabel(xyt_label[1])
    plt.title(xyt_label[2])
    plt.savefig(os.path.join(config.COMPARE_EXP, mkfile_time), dpi=400)
    # 显示柱状图
    plt.show()


def draw_tree_len(tree_len, save_name):
    """

    :param tree_len:
    :param save_name:
    :return:
    """
    time = datetime.datetime.strftime(datetime.datetime.now(), '%Y_%m_%d_%H_%M_%S')
    # 保存数据
    if not os.path.exists(save_path):
        os.makedirs(save_path)  # 如果不存在目录save_path，则创建
    save_experimental_data(tree_len, save_path, save_name + time)

    # 画图
    mkfile_time = "picture_" + time  # 这里是文件引用时间
    plt.figure(1)
    plt.plot(tree_len, label='Mutil_agents')
    plt.legend(loc='best')
    plt.ylabel('tree length')
    plt.xlabel('epoch')
    plt.title("tree length")
    if not os.path.exists(save_path):
        os.makedirs(save_path)  # 如果不存在目录figure_save_path，则创建
    plt.grid()
    plt.savefig(os.path.join(save_path, mkfile_time), dpi=400)
    plt.show()


