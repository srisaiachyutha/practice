d=int(input('enter the day ,month,year'))
m=int(input())
y=int(input())
day=['saturday','sunday','monday','tuesday','wedesday','thursday','friday']
totaldays=(y-1)//4

totaldays+=(y-1)*365

monthdays=[0,31,28,31,30,31,30,31,31,30,31,30,31]
if y%4==0 and y%100!=0 or y%400==0:
    monthdays[2]=29
    

for i in range(m):
    totaldays+=monthdays[i]
totaldays+=d
print(day[totaldays%7])
