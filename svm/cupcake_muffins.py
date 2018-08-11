# coding=utf-8
"""
这个文档用来将cupcake和muffins使用svm进行分类
"""
import pandas as pd
import numpy as np
from sklearn import svm

import matplotlib.pyplot as plt
import seaborn as sns
sns.set(font_scale=1.2)

recipes = pd.read_csv("./data/recipes_muffins_cupcakes.csv")
recipes.head()

# sns.lmplot("Sugar", "Butter", data=recipes, hue="Type", palette="Set1", fit_reg=False, scatter_kws={"s":70})
# 用来将上面的设置好的seaborn可视化
# plt.show()
print("------------")

sugar_butter = recipes[["Flour", "Sugar"]].as_matrix()
type_label = np.where(recipes["Type"]=="Muffin", 0, 1)

model = svm.SVC(kernel="linear")
model.fit(sugar_butter, type_label)

# 得到分类的超平面
w = model.coef_[0]
a = -w[0] / w[1]
xx = np.linspace(30, 60)
yy = a * xx - (model.intercept_[0]) / w[1]

# Plot the parallels to the separating hyperplane that pass through the support vectors
b = model.support_vectors_[0]
yy_down = a * xx + (b[1] - a * b[0])
b = model.support_vectors_[-1]
yy_up = a * xx + (b[1] - a * b[0])

# 画出超平面
sns.lmplot('Flour', 'Sugar', data=recipes, hue='Type', palette='Set1', fit_reg=False, scatter_kws={"s": 70})
plt.plot(xx, yy, linewidth=2, color='black')
# plt.show()

# Look at the margins and support vectors
sns.lmplot('Flour', 'Sugar', data=recipes, hue='Type', palette='Set1', fit_reg=False, scatter_kws={"s": 70})
plt.plot(xx, yy, linewidth=2, color='black')
plt.plot(xx, yy_down, 'k--')
plt.plot(xx, yy_up, 'k--')
plt.scatter(model.support_vectors_[:, 0], model.support_vectors_[:, 1],
            s=80, facecolors='none')
plt.show()



# Create a function to guess when a recipe is a muffin or a cupcake# Create
def muffin_or_cupcake(flour, sugar):
    if(model.predict([[flour, sugar]]))==0:
        print('You\'re looking at a muffin recipe!')
    else:
        print('You\'re looking at a cupcake recipe!')

# Predict if 50 parts flour and 20 parts sugar
muffin_or_cupcake(50, 20)


# Plot the point to visually see where the point lies# Plot t
# sns.lmplot('Flour', 'Sugar', data=recipes, hue='Type', palette='Set1', fit_reg=False, scatter_kws={"s": 70})
# plt.plot(xx, yy, linewidth=2, color='black')
# plt.plot(50, 20, 'yo', markersize='9')