def arm(a):
    t=a
    c=0
    while t>0:
        b=t%10
        c=c+(b**3)
        t=t//10
    if c==a:
        return "The inputted number is an Armstrong number."
    else:
        return "The inputted number is an Armstrong number."
    
a=int(input("Enter a number_"))
b=arm(a)
print(b)