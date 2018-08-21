import matplotlib.pyplot as plt


def liner_func():
    x_list = [60, 34, 12, 34, 71, 28, 96, 34, 42, 37]
    y_list = [301, 169, 47, 178, 365, 126, 491, 157, 202, 184]
    length = len(x_list)
    x_mean = sum(x_list) / len(x_list)
    y_mean = sum(y_list) / len(y_list)
    xy_mean = sum([x_con * y_con for x_con in x_list for y_con in y_list]) / len(x_list)
    xx_mean = sum([x_con ** 2 for x_con in x_list]) / len(x_list)
    yy_mean = sum([y_con ** 2 for y_con in y_list]) / len(x_list)

    xy = 0
    x_square = 0
    for i in range(len(x_list)):
        xy += x_list[i] * y_list[i]
        x_square += x_list[i] ** 2

    m = (xy - length * x_mean * y_mean) / (x_square - length * (x_mean ** 2))
    b = y_mean - m * x_mean

    # 线性回归方程
    def func(x):
        f = m * x + b
        return f

    plt.scatter(x_list, y_list)
    x_ = list(range(00, 100, 1))
    y_ = [func(con) for con in x_]
    # plt.plot(x_, y_)
    # plt.show()

    # 计算R2
    # 总平方和
    sst = sum([(y_con - y_mean) ** 2 for y_con in y_list])
    # 回归平方和
    ssreg = sum([(func(x_con) - y_mean) ** 2 for x_con in x_list])
    # 残差平方和
    ssres = sum([(func(x_list[i]) - y_list[i]) ** 2 for i in range(length)])

    R2 = 1 - (ssres / sst)
    res = ssreg / sst
    print(R2, res)




if __name__ == '__main__':
    liner_func()