#coding=utf-8


def replace_str(dict, str, flagg):
    if flagg:
        return str
    for item in dict.items():
        if item[1] in str:
            str.replace(item[1], item[0])
            flag = 1
        replace_str(dict, str, flagg)
        if flag:
            flagg = 1
    return str, flag





def repl_type():
    type_input = input()
    target = input()
    type_input = type_input.split(";")
    type_input_list = [con.split(" ") for con in type_input]
    the_dict = {}
    flag = 0
    for content in type_input_list:
        if content[2] == target:
            flag = 1
        if len(content) != 3:
            print("none")
        else:
            the_dict[content[2]] = content[1]
            pass

    # 即如果没有这个关键字的定义，输出none
    if flag == 0:
        print("none")

    for content in type_input_list:
        if content[2] == target:
            # 记录tf 的第一位
            temp = the_dict[target]
            _, mask = replace_str(temp)
            temp.replace("*", " *")
            print(temp)

if __name__ == '__main__':
    repl_type()


# typedef int INT; typedef INT** INTP;
# INTP
