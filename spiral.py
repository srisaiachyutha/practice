#if we input the matrix size as 3
#we get ouput as
#   1   2    3
#   8   9    4
#   7   6    5


n=int(input('enter the size of the matrix'))
m=[]
for i in range(n):
    l=[]
    for j in range(n):
        l.append(0)
    m.append(l)
#print(m)
k=n
if n%2!=0:
    k=n+1
c=1
for l in range(k//2):
    i,j=l,l
    for j in range(l,n-l):
        m[i][j]=c
        c+=1

    j=n-1-l
    for i in range(l+1,n-l-1):
        m[i][j]=c
        c+=1

    j=n-1-l
    i=n-1-l
    for j in range(n-1-l,l,-1):
        m[i][j]=c
        c+=1

    j=l
    
    for i in range(n-1-l,l,-1):
        m[i][j]=c
        c+=1


for i in range(n):
    for j in range(n):
        print(m[i][j], ' ',end='')
    print()


        
