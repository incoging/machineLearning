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

    # 把每个重量对应的状态先初始化为0
    res = [0 for j in range(c + 1)]

    # 这里i和j都加一直接就表示容量和第i件物品了，即不再从0开始
    for i in range(0, n + 1):
        for j in range(c + 1, -1, -1):
            if j >= w[i]:
                res[j] = res[j - w[i]] + v[i - 1]
    print("偷到宝贝的总价值为：", res[n])


bag()
# 宝贝价值：2,2,6,5,4
# 宝贝重量:6,3,5,4,6
# 小偷背包容量：10