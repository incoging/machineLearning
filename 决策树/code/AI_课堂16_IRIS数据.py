# coding=utf-8
"""
IRIS数据集介绍：
Iris数据集是常用的分类实验数据集，由Fisher, 1936收集整理。Iris也称鸢尾花卉数据集，是一类多重变量分析的数据集。
数据集包含150个数据，分为3类，每类50个数据，每个数据包含4个属性。可通过花萼长度，花萼宽度，
花瓣长度，花瓣宽度4个属性预测鸢尾花卉属于（Setosa，Versicolour，Virginica）三个种类中的哪一类。
"""
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn import neighbors, datasets

# 提取IRIS数据集，并展示
iris = datasets.load_iris()
X = iris.data[:, :2]
y = iris.target

sns.set(style='darkgrid')
for c, i, names in zip("rgb", [0, 1, 2], iris.target_names):
    plt.scatter(X[y == i, 0], X[y == i, 1], c=c, label=names)
plt.title('IRIS')
# plt.legend()
# plt.show()


# 构建K近邻分类器
def make_meshgrid(x, y, h=.02):
    x_min, x_max = x.min() - 1, x.max() + 1
    y_min, y_max = y.min() - 1, y.max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    return (xx, yy)


xx, yy = make_meshgrid(X[:, 0], X[:, 1])

for weights in ['uniform', 'distance']:
    clf = neighbors.KNeighborsClassifier(1, weights=weights)
    clf.fit(X, y)
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.figure()
    plt.contourf(xx, yy, Z, cmap=plt.cm.RdBu, alpha=0.8)
    for c, i, names in zip("rgb", [0, 1, 2], iris.target_names):
        plt.scatter(X[y == i, 0], X[y == i, 1], c=c, label=names, edgecolor='k')
    plt.title("3-Class classification (k = %i, weights = '%s')" % (7, weights))
    plt.legend()

plt.show()
