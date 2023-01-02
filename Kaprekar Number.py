n=int(input("Enter a number_"))
t=n
a=n**2
b=(a//10**len(str(n)))%(10**len(str(n)))
c=a%(10**len(str(n)))
if (b+c)==n:
    print(n,"is a Kaprekar number.")
else:
    print(n,"is not a Kaprekar number.")