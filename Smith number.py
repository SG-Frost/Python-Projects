n=int(input("Enter a number_"))
t=n
l=[]
fl=[]
a=0
for i in range(2,t+1):
    if t%i==0:
        l.append(i)
print(l)
