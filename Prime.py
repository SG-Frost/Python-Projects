n=int(input("Enter a number_"))
a=0
if n==1:
    print(n,"is neither prime nor composite.")
for i in range(2,n):
    if n%i==0:
        a=a+1
if a>=1:
    print(n,"is not prime.")
elif a<1:
    print(n,"is prime.")