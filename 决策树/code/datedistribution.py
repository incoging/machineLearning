import matplotlib.pyplot as plt
import numpy as np

from sklearn.tree import DecisionTreeClassifier as DTC
import seaborn as sns
from sklearn import datasets

X, y = datasets.make_moons(200, noise=0.2, random_state=0)

sns.set(style='darkgrid')
for i, v, l in [[0, 'r', 'class_0'], [1, 'b', 'class_1']]:
    plt.scatter(X[y == i][:, 0], X[y == i][:, 1], c=v, label=l)
plt.legend()
plt.show()

clf=DTC(criterion='entropy')
clf.fit(X,y)

dot_data=tree.export_graphviz(clf, out_file=None,
                        feature_names=['F_1','F_2'],
class_names=['class_0','class_2'],
filled=True, rounded=True,
                        special_characters=True)

graph=graphviz.Source(dot_data)

graph.render('MOON')