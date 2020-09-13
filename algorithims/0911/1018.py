#체스판 생성
#8*8을 검사하되 'W','B'를 번갈아가면서 검사해야 한다
#'W'로 시작했을 때와(idex1) 'B'(idex2)로 시작했을 때 칠해야 하는 부분들이다             
#정사각형의 최소개수이므로 최소값을 출력해야 한다.
n, m = map(int, input().split())
chess = []
minimal = []

for _ in range(n):
    chess.append(input())

for a in range(n - 7):
    for i in range(m - 7):
        idx1 = 0
        idx2 = 0
        for b in range(a, a + 8):
            for j in range(i, i + 8):              
                if (j + b)%2 == 0:
                    if chess[b][j] != 'W': 
                        idx1 += 1  
                    if chess[b][j] != 'B': 
                        idx2 += 1
                else :
                    if chess[b][j] != 'B': 
                        idx1 += 1
                    if chess[b][j] != 'W': 
                        idx2 += 1
        minimal.append(idx1)                         
        minimal.append(idx2)                         

print(min(minimal))     
        
            
            