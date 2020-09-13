"""
문자열에는 몇개의 단어? ==> 단어는 공백으로 구분한다
1. 문장 앞과 뒤 양쪽에 공백이 있는 경우(and)
2. 단어가 없고 공백이 있는 경우(none)
3. 문장의 앞 이나 뒤에 공백이 있는 경우(or)
"""
"""
strings = input("")
if strings == " ": #2
    print(0)
    
else : 
    words = strings.split(" ") #단어는 구분하는 방법
    
    while '' in words : #1번일 경우에 공백을 없애서 단어를 구분해 낸다
        words.remove('')
        
print(len(words))
"""
#축약

string = input("")
words = string.split(" ")
words = [w for w in words if w != ""]
print(len(words)) 

