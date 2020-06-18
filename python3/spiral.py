#if we input the matrix size as 3
#we get ouput as
#   1   2    3
#   8   9    4
#   7   6    5
c=1
def prime():
    global c
    while True:
        k=0
        for i in range(1,c+1):
            if c%i==0:
                k+=1
        if k==2:
            c+=1
            return c-1
        else:
            c+=1

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

for l in range(k//2):
    i,j=l,l
    for j in range(l,n-l):
        m[i][j]=prime()
        

    j=n-1-l
    for i in range(l+1,n-l-1):
        m[i][j]=prime()
        

    j=n-1-l
    i=n-1-l
    for j in range(n-1-l,l,-1):
        m[i][j]=prime()
        

    j=l
    
    for i in range(n-1-l,l,-1):
        m[i][j]=prime()
        


for i in range(n):
    for j in range(n):
         print("%6d "%(m[i][j]),end="")
        #print(m[i][j], ' ',end='')
    print()


        
