n=input("Enter something_")
l=[]
k=-1
for i in range(len(n),0,-1):
    l.append(n[k])
    k-=1
s=''
for j in l:
    s=s+j
if s==n:
    print("Palindrome")
else:
    print("Not Palindrome")