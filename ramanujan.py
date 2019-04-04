#this program is about the ramanujan sequence numbers to check the left side number
#sum is eual to the right side sum of equal length or less than the number of numbers
# example first sequence number is 6 as the sum of the left side numbers is equal to the right side
# sum of 1,2,3,4,5  is equal to the 7,8 the right side sum.


n=5
i=1
while n>=0:
    s=i*(i-1)//2
    s2=0
    j=i+1
    while s2<=s:
        s2+=j
        if s2==s:
            print(i)
            n-=1
            break
        j+=1
        
    i+=1
