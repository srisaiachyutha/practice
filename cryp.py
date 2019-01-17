import math
string='abcdefghijklmnopqrstuvwxyz'
e={}
e1={}
p1={}
p={}
for i in range(32,127):
    #print(i,math.e**ord(i))
    e[chr(i)]=(str(math.e**(i))[2:8])
    e1[(str(math.e**(i))[2:8])]=chr(i)
    p[chr(i)]=(str(math.pi**(i))[2:8])
    p1[(str(math.pi**(i))[2:8])]=chr(i)
value=input('enter the value')
data=input("enter the data")
k=''


for i in data:
    k+=str(e[i])
print(k)
length=len(k)
de=''
i=0

while i<length:
    de+=k[i]
    i+=2
i=1
while i<length:
    #print(k[i],end='')
    de+=k[i]
    i+=2
print(de)

i=0
enc=''
while i<length:
    enc+=(chr(int(de[i:i+3])))
    i+=3
#encoding ends here
#decoding the encoded data
print(enc)


d=''
for i in enc:
    d+=str(ord(i))

t=''
i=0
while i<length//2:
    
    t+=d[i]
    if i==length//2-1:
        t+=d[i+(length//2)-1]
    else:
        t+=d[i+(length//2)]
    i+=1
print('\n'+t)
i=0
while i<length:
    if t[i:i+6] in e.values():
        print(e1[t[i:i+6]],end='')
    i+=6
        
