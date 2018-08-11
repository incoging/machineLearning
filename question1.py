while True:
    try:
        res = ''
        s = input()
        for i in s:
            if i.isupper():
                i = i.lower()
                res = res + i
            elif i.islower():
                i = i.upper()
                res = res + i
            else:
                res = res + i
        print(res)
    except:
        break