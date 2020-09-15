text = int(input())
for i in range(text):
    num, s = input().split()
    texts = ''
    for i in s:
        texts += int(num) * i
    print(texts)