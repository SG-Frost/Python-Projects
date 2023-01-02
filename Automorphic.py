n=int(input("Enter a number_"))
t=n
if (t**2)%(10**len(str(t)))==(t):
    print(n,"is an Automorphic number.")
else:
    print(n,"is not an Automorphic number.")