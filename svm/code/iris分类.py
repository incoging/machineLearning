import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model, cross_validation, svm

"""
使用糖尿病病人的数据：
有442个样本；
每个样本10个特征
每个特征都是浮点数，数据都在-0.2~0.2之间
样本的目标都在整数25~346之间
"""

# 定义加载数据集函数
def load_data_regerssion():
    diabetes = datasets.load_diabetes()
    return cross_validation.train_test_split(diabetes.data, diabetes.target, test_size=0.25, random_state=0)
