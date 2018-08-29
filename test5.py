# str = input().strip()

str = "AB1CD2E33"
str = str+ "A"
# str = str.split()
stack_list = []
num_list = []
temp_num = []
flag = 1
for con in str:
    if ord(con) == 45:
        stack_list.append(con)
        flag = 1
    elif 47 < ord(con) < 58:
        flag = 0
        temp_num.append(con)
    else:
        flag = 1
    if flag:
        if len(stack_list) % 2 == 0:
            try:
                num_list.append(int("".join(temp_num)))
                stack_list.clear()
                temp_num.clear()
            except:
                continue
        else:
            try:
                num_list.append(-int("".join(temp_num)))
                stack_list.clear()
                temp_num.clear()
            except:
                continue

print(sum(num_list))
