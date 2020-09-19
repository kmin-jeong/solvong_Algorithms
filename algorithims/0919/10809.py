alphabet = list(map(chr, range(97, 123)))
dictionaries = dict(zip(alphabet, [-1]*26))

string = input()

for i, s in enumerate(string) : 
    if dictionaries[s] == -1 : 
        dictionaries[s] = i

for v in dictionaries.values() : 
    print(v, end=" ")