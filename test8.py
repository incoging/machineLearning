
func1 = []
func2 = []
for i in range(10):
    real_num = int(input().strip())
    img_num = int(input().strip())
    func1.append((real_num, img_num))

for i in range(10):
    real_num = int(input().strip())
    img_num = int(input().strip())
    func2.append((real_num, img_num))


def conpute(n1, n2):
    return [n1[0]*n2[0]-n1[1]*n2[1], n1[0]*n2[1]+ n1[1]*n2[0]]

c = [[]]
for i in range(9):
    real = 0
    img = 0
    for j in range(i+1):
        temp = conpute(func1[j], func2[i-j])
        c[i] = [real+temp[0], img+temp[1]]


print(c[0][0] // 2)
print(c[0][1] // 2)
for i in range(1, 9):
    print(c[i][0])
    print(c[i][1])