n=int(input("Enter a number_"))
a=0
t=n
for i in range(1,t-1):
    if t%i==0:
        a=a+i
if a==t:
    print(n,"is a Perfect number.")
else:
    print(n,"is not a Perfect number.")