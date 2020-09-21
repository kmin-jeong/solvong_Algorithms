env = int(input())
box = 0
while True:
    if (env % 5) == 0:
        box = box + (env//5)
        print(box)
        break
    env = env-3
    box += 1
    if env < 0:
        print("-1")
        break