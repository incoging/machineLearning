def bag():
    v = input("宝贝价值：")
    v = v.split(",")
    v = [int(con) for con in v]
    n = len(v)

    w = input("宝贝重量:")
    w = w.split(",")
    w = [int(con) for con in w]

    c = input("小偷背包容量：")
    c = int(c)

    res = [[-1 for j in range(c + 1)] for i in range(n + 1)]
    for j in range(c + 1):
        res[0][j] = 0
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            res[i][j] = res[i - 1][j]
            if j >= w[i - 1] and res[i][j] < res[i - 1][j - w[i - 1]] + v[i - 1]:
                res[i][j] = res[i - 1][j - w[i - 1]] + v[i - 1]
    print("偷到宝贝的总价值为：", res[n][c])