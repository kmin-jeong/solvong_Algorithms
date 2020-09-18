n = int(input())
m = int(input())
ms = []
if m != 0:
    ms = list(input().split())

ans_num = 999999999
length = 0
for i in range(1000000):
    broken = False
    for s in str(i):
        if s in ms:
            broken = True
    if broken:
        pass
    else:
        if ans_num > abs(n - i):
            ans_num = abs(n - i)
            length = len(str(i))

ans_num = min(ans_num + length, abs(n - 100))

print(ans_num)