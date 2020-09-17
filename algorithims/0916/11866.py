from collections import deque
n, k = map(int, input().split())
sequence = deque([i for i in range(1,n+1)])
residue = []
while len(sequence) != 1:
    for _ in range(k-1):
        sequence.append(sequence.popleft())
    residue.append(sequence.popleft())
residue.append(sequence[0])
print('<'+", ".join(map(str, residue))+'>')