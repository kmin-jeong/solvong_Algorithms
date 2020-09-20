#이항계수 구글 검색하기
#math.factorial 활용
from math import factorial
N, K = list(map(int, input().split()))
print(factorial(N)//(factorial(K) * factorial(N-K)))