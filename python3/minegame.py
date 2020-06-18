import random
def display(matrix,matrix2):
    '''this will display the matrix format of the game'''
    print('   0  1  2  3  4  5  6  7  8  9  ')
    for i in range(10):
        print(i,' ',end='')
        for j in range(10):
            if matrix2[i][j]==1:
                print(matrix[i][j],' ',end="")
            else:
                print(' ',' ',end='')
            
        print()
matrix1=[[0]*10 for _ in range(10)]
matrix2=[[-1]*10 for _ in range(10)]
cou=0
def create(matrix):
    '''this function will make the bombs count ready in the matrix'''
    for i in range(10):
        for j in range(10):
            c=0
            if matrix[i][j]!='b':
                x=i-1
                y=j-1
                if x>=0 and y>=0 and x<10 and y<10 and matrix[x][y]=='b':
                    c+=1
                x=i-1
                y=j
                if x>=0 and y>=0 and x<10 and y<10 and matrix[x][y]=='b':
                    c+=1

                x=i-1
                y=j+1
                if x>=0 and y>=0 and x<10 and y<10 and matrix[x][y]=='b':
                    c+=1

                x=i
                y=j-1
                if x>=0 and y>=0 and x<10 and y<10 and matrix[x][y]=='b':
                    c+=1

                x=i
                y=j+1
                if x>=0 and y>=0 and x<10 and y<10 and matrix[x][y]=='b':
                    c+=1

                x=i+1
                y=j-1
                if x>=0 and y>=0 and x<10 and y<10 and matrix[x][y]=='b':
                    c+=1

                x=i+1
                y=j
                if x>=0 and y>=0 and x<10 and y<10 and matrix[x][y]=='b':
                    c+=1

                x=i+1
                y=j+1
                if x>=0 and y>=0 and x<10 and y<10 and matrix[x][y]=='b':
                    c+=1
                if c!=0:
                    matrix[i][j]=c
                else:
                    matrix[i][j]='-'
 
def start(matrix1,matrix2,i,j):
    '''this function is the main function which will reveal the boxes'''
    matrix2[i][j]=1
    global count
    count-=1
    if matrix1[i][j]=='-':
        x=i-1
        y=j-1
        if x>=0 and y>=0 and x<10 and y<10 and matrix2[x][y]!=1:
            start(matrix1,matrix2,x,y)
        x=i-1
        y=j
        if x>=0 and y>=0 and x<10 and y<10 and matrix2[x][y]!=1:
            start(matrix1,matrix2,x,y)

        x=i-1
        y=j+1
        if x>=0 and y>=0 and x<10 and y<10 and matrix2[x][y]!=1:
            start(matrix1,matrix2,x,y)

        x=i
        y=j-1
        if x>=0 and y>=0 and x<10 and y<10 and matrix2[x][y]!=1:
            start(matrix1,matrix2,x,y)

        x=i
        y=j+1
        if x>=0 and y>=0 and x<10 and y<10 and matrix2[x][y]!=1:
            start(matrix1,matrix2,x,y)

        x=i+1
        y=j-1
        if x>=0 and y>=0 and x<10 and y<10 and matrix2[x][y]!=1:
            start(matrix1,matrix2,x,y)

        x=i+1
        y=j
        if x>=0 and y>=0 and x<10 and y<10 and matrix2[x][y]!=1:
            start(matrix1,matrix2,x,y)

        x=i+1
        y=j+1
        if x>=0 and y>=0 and x<10 and y<10 and matrix2[x][y]!=1:
            start(matrix1,matrix2,x,y)
c=10
while c>0:
    
    x=random.randint(0,9)
   
    y=random.randint(0,9)
    matrix1[x][y]='b'
    c-=1

create(matrix1)

for i in matrix1:
    cou+=i.count('b')
count=100-cou
print('the value of the count is ',count)
#count=100
win=True
while count>0:
    print('enter the x and y coordinates\n')
    n=int(input())
    m=int(input())
    if matrix1[n][m]=='b':
        win=False
        break
    start(matrix1,matrix2,n,m)
    display(matrix1,matrix2)
     
if win:
    print('you have won the game')
else:
    
    print('you have lost it')
for i in range(10):
        for j in range(10):
            matrix2[i][j]=1
display(matrix1,matrix2)
