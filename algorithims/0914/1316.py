#연속하면 그룹단어, 떨어져나가면 그룹단어 아님
N=int(input())
answer=0
for i in range(N):
    word = input()
    for j in range(len(word)):
        if j!=len(word)-1:
            if word[j]==word[j+1]:
                pass
            elif word[j] in word[j+1:]:
                break
        else:
            answer+=1
print(answer)