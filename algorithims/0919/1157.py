from collections import Counter

word = input().upper()
center = Counter(word)

many = []

for k,v in center.items() :
    if v == max(center.values()) :
        many.append(k)
        
        if len(many) > 1 : 
            break
        
if len(many) == 1 :
    print(many[0])
else : 
    print('?')