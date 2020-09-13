#오름차순 정렬
"""
n = int(input())
num = []
for i in range(n):
    num.append(int(input()))
num = sorted(num)

for i in range(n):
    print(num[i])
-> python에서는 이렇게 푸니깐 시간 초과가 났었다. 백준&구글링으로 찾아보니 pypy3으로 풀었을 때 속도가 더 향상됨
"""    
#시간을 줄이기 위해 input 대신 sys.stdin.readline()를 사용
import sys
n = int(sys.stdin.readline())
num = list()
for i in range(n):
    num.append(int(sys.stdin.readline()))
num.sort()

for i in num:
    print(i)