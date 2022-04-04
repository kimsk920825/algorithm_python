import sys

sys.stdin = open("./input.txt", "rt")

a = input()
b = input()

str1 = []
str2 = []

for alphabet in a:
    if alphabet.isupper():
        str1[ord(alphabet)-65] +=1
    else:
        str1[ord(alphabet)-71] +=1
for alphabet in b:
    if alphabet.isupper():
        str2[ord(alphabet)-65] +=1
    else:
        str2[ord(alphabet)-71] +=1
for i in range(52):
    if str1[i] != str2[i]:
        print("No")
        break
else:
    print("Yes")

