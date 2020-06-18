n=int(input('enter the number to check whether it is prime are not'))
def isprime(n):
    def prime(n,var):
        if var==1:
            return n
        elif n%var==0 and var!=0:
            return 0
        else:
            return prime(n,var-1)
    if n<=1:
        return 0
    k=prime(n,n//2)
    return k
k=isprime(n)
if k==0:
    print('it is not prime')
else:
    print('it is prime;')
    
