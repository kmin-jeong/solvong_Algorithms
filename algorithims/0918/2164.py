#카드를 버린 후 앞으로 옮긴다
from collections import deque

N = int(input())
deque = deque([i for i in range(1, N + 1)])

while(not (len(deque) == 1)):
    deque.popleft()
    move_num = deque.popleft()
    deque.append(move_num)
    
print(deque[0])