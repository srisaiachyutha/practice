def loveFunction():
    lover='sindhuja'
    for y in range(15,-15,-1):
        s=''
        for x in range(-30,30):
            if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0:
                s+=lover[(x-y)%8]
            else:
                s+=' '
        print(s)
loveFunction()
