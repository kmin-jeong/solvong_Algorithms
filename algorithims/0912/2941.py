# 몇개의 크로아티아 알파벳으로 구성되어있는가?
#목록에 없는 알파벳은 한글자씩 센다
crowatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']
alphabet = input()
for printer in crowatia:
    alphabet = alphabet.replace(printer,'*')
#몇개?
print(len(alphabet))