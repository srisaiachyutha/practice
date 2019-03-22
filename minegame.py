import random
import time
def display(matrix,matrix2):
    print('  ',end='')
    for _ in range(10):
        #print(' ',end='')
        print(_,'\t',end=" ")
    print()
    for i in range(len(matrix)):
        print(i,' ',end='')
        for j in range(len(matrix)):
            if matrix2[i][j]==1:
                print(' ',matrix[i][j],'\t',end="")
            else:
                print('  ','\t',end='')
        print()
matrix1=[[0]*10 for _ in range(10)]
matrix2=[[-1]*10 for _ in range(10)]


def create(matrix):
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
    
'''for i in range(10):
    m=[]
    for j in range(10):
        m.append(0)
    matrix1.append(m)
'''
def start(matrix1,matrix2,i,j):
    matrix2[i][j]=1
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

    
    


#matrix=[[' ']*10]*10
#print(matrix1)
c=10
while c>0:
    
    x=random.randint(0,9)
    #print(a)
    y=random.randint(0,9)
    #print(x,y)
    matrix1[x][y]='b'
    c-=1
create(matrix1)
count=100
win=True
while count>90:
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
    for i in range(10):
        for j in range(10):
            matrix2[i][j]=1
    display(matrix1,matrix2)
    print('you have lost it')
