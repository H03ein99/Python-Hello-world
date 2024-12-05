import os
from random import randint

temp = "abcdefghijklmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ ,!"
chars = [x for x in temp]
print(chars)
message = "Hello, World!"
res=""
i = len(temp)
while(res!=message):
    char = chars.pop(randint(0, i-1))
    i -= 1   
    res += char
    print(res)
    if(res==message[:len(res)]):
        chars = [x for x in temp]
        i = len(temp)
    else:
        res = res[:-1]
        os.system("cls")
        
     

        