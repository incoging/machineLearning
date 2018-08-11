line_1 = input().strip()
line_2 = input().strip()

typedefs_input = line_1.split(";")

typedefs = []
typedefs_index = []

is_error = False

"""
typedef int INT1; typedef INT1* INT; typedef INT*** INTP;
INTP
"""
for typedef_one in typedefs_input:
    typedefs_one_split = typedef_one.strip().split(" ")

    if len(typedefs_one_split) != 3:
        is_error = False
        break

    if typedefs_one_split[0] == "typedef":
        def_type = typedefs_one_split[1]
        def_name = typedefs_one_split[2]

        exist_index = typedefs.index(def_type) if def_type in typedefs else -1
        name_index = typedefs.index(def_name) if def_name in typedefs else -1

        if exist_index < 0:
            typedefs.append(def_type)
            typedefs_index.append(-1)
            if name_index < 0:
                typedefs.append(def_name)
                typedefs_index.append(len(typedefs_index) - 1)
            else:
                typedefs_index[name_index] = len(typedefs_index) - 1
        else:
            if name_index < 0:
                typedefs.append(def_name)
                typedefs_index.append(exist_index)
            else:
                typedefs_index[name_index] = exist_index
                pass
            pass
        pass
    pass

if is_error or line_2 not in typedefs:
    print(None)
else:
    index = typedefs.index(line_2)
    print_result = ""
    while True:
        if typedefs_index[index] == -1:
            new_type = typedefs[index]
            has_p = False
            while True:
                if "*" in new_type:
                    print_result += " *"
                    has_p = True
                    new_type = new_type.strip()[0: -1]
                else:
                    break
                pass
            if has_p and new_type in typedefs:
                index = typedefs.index(new_type)
            else:
                break
        index = typedefs_index[index]
    print_result = new_type + print_result
    print(print_result)
