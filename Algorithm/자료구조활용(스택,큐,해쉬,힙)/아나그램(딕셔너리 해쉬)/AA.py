import sys

sys.stdin = open("./input.txt", "rt")

a = input()
b = input()

#방법1
# str1 = dict()
# str2 = dict()

# for x in a: 
#     str1[x] = str1.get(x,0)+1
# for x in b:
#     str2[x] = str2.get(x,0)+1

# for i in str1.keys():
#     if i in str2.keys():
#         if str1[i] != str2[i]:
#             print("No")
#             break
#     else:
#         print("No")
#         break
# else:
#     print("Yes")
#방법2
sH = dict()
for x in a:
    sH[x] = sH.get(x,0) +1
for x in b:
    sH[x] = sH.get(x,0) -1

for x in a:
    if sH.get(x) >0:
        print("no")
        break
else:
    print("Yes")