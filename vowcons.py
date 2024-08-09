a=input("enter a string: ")
b="aeiou"
vow=0
const=0
space=0
for i in a:
    if i in b:
        vow+=1
    elif i.isspace():
        space+=1
    else:
        const+=1
print("no of vowels:",vow)
print("no. of consonants:",const)
