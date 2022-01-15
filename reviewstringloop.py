n = int(input())
temp = []
for i in range(0,n):
    s = input()
    temp.append(s)

for i in range(0,n):
    for j in range(0,len(temp[i]),2):
        print(temp[i][j],end='')
    print(end=' ')
    for j in range(1,len(temp[i]),2):
        print(temp[i][j],end='')
    print()


    # more simple
    for i in range(int(input())): s=input(); print(*["".join(s[::2]),"".join(s[1::2])])
