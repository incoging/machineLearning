
n = int(input().strip())
the_list = []
for i in range(n):
    cow_dou = int(input().strip())
    month = int(input().strip())
    the_list.append([cow_dou, month])

res  =[]
for i in range(n):
    now_num = the_list[i][0]
    the_month = the_list[i][1]
    if the_month < 4:
        for j in range(the_month):
            now_num += 1
    if the_month >= 4:
        cow_list = []
        now_num = 5
        a = 1
        b = 2

        for j in range(4, the_month):
            cow_list.append(a)
            cow_list.append(b)
            a = a+b
            b = a+b
        now_num += cow_list[(the_month) // 2]
    res.append(now_num)

for con in res:
    print(con)