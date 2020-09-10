st = []
stairs = int(input())
mxs = [None] * 300
for i in range(stairs):
    st.append(int(input()))
for i in range(stairs):
    if i == 0:
        mxs[0] = st[i]
        continue
    elif i == 1:
        mxs[1] = st[0]+st[1]
        continue 
    elif i == 2:
        mxs[2] = max(st[0], st[1]) + st[2]
        continue
    mxs[i] = max(mxs[i-3] + st[i-1], mxs[i-2]) + st[i]

print(mxs[stairs-1])
