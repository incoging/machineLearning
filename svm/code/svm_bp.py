# coding=utf-8
import numpy as np
import pickle

class SVM:
    def __init__(self, data_set, labels, C, toler, kernel_option):
        # 训练特征、标签
        self.train_x = data_set
        self.train_y = labels
        # 惩罚参数
        self.C = C
        # 迭代终止条件之一
        self.toler = toler
        # 训练样本的个数
        self.n_samples = np.shape(data_set)[0]
        # 拉格朗日乘子
        self.alphas = np.mat(np.zeros((self.n_samples, 1)))
        self.b = 0
        self.error_tmp = np.mat(np.zeros((self.n_samples, 2)))
        self.kernel_opt = kernel_option
        self.kernel_mat = calc_kernel(self.train_x, self.kernel_opt)
        pass
    pass


def calc_kernel(train_x, kernel_option):
    """计算核函数的矩阵

    :param train_x: train_x(mat): 训练样本的特征值
    :param kernel_option: kernel_option(tuple): 核函数的类型以及参数
    :return: kernel_matrix(mat): 样本的核函数值
    """
    m = np.shape(train_x)[0]
    # 初始化样本之间的核函数值
    kernel_matrix = np.mat(np.zeros((m, m)))
    for i in range(m):
        kernel_matrix[:, i] = cal_kernel_value(train_x, train_x[i, :], kernel_option)
    return kernel_matrix


def cal_kernel_value(train_x, train_x_i, kernel_option):
    """样本之间的核函数值

    :param train_x: 训练样本
    :param train_x_i: 第i个训练样本
    :param kernel_option: 核函数的类型以及参数
    :return: kernel_value: 样本之间的核函数值
    """
    # 核函数的类型，分为rbf和其他
    kernel_type = kernel_option[0]
    # 样本的个数
    m = np.shape(train_x)[0]

    kernel_value = np.mat(np.zeros((m, 1)))

    if kernel_type == "rbf":
        sigma = kernel_option[1]
        sigma = 1.0 if sigma == 0 else sigma
        for i in range(m):
            diff = train_x[i, :] - train_x_i
            kernel_value[i] = np.exp(diff * diff.T / (-2.0 * sigma ** 2))
    else:
        kernel_value = train_x * train_x_i.T
    return kernel_value


def SVM_train(train_x, train_y, toler, max_iter, kernel_option = ("rbf", 0.431029)):
    """

    :param train_x:  训练数据的特征
    :param train_y: 训练数据的标签
    :param toler:  惩罚系数
    :param max_iter: 迭代的终止条件之一
    :param kernel_option: 核函数的类型及其参数
    :return: SVM模型
    """
    # 初始化SVM分类器
    svm = SVM(train_x, train_y, C, toler, kernel_option)

    # 开始训练
    entire_set = True
    alpha_pairs_changed = 0
    iteration = 0

    while(iteration < max_iter) and ((alpha_pairs_changed > 0) or entire_set):
        print("iterration: ", iteration)
        alpha_pairs_changed = 0

        if entire_set:
            # 对所有的样本
            for x in range(svm.n_samples):
                alpha_pairs_changed += choose_and_update(svm, x)
                iteration += 1
        else:
            # 非边界的样本
            bound_samples = []
            for i in range(svm.n_samples):
                if svm.alphas[i, 0] > 0 and svm.alphas[i, 0] < svm.C:
                    bound_samples.append(i)
            for x in bound_samples:
                alpha_pairs_changed += choose_and_update(svm, x)
            iteration += 1
        # 在所有样本和非边界样本之间交替
        if entire_set:
            entire_set = False
        elif alpha_pairs_changed == 0:
            entire_set = True
    return svm


# 判断和选择两个alpha进行更新
def chose_and_update(svm, alpha_i):
    """

    :param svm:
    :param alpha_i:  选择出的第一个变量
    :return:
    """
    # 计算第一个样本的E_i
    error_i = cal_error(svm, alpha_i)

    # 判断选择出的第一个变量是否违反了KKT条件
    if (svm.train_y[alpha_i] * error_i < -svm.toler) and \
            (svm.alphas[alpha_i] < svm.C) or \
            (svm.train_y[alpha_i] * error_i > svm.toler) and \
            (svm.alphas[alpha_i] > 0):

        # 选择第二个变量


        pass
    pass

# 计算误差
def cal_error(svm, alpha_k):
    pass


# 选择第二个变量
def select_second_sample_j(svm, alpha_i, error_i):
    pass


# 重新计算误差值
def update_error_tmp(svm, alpha_k):
    pass