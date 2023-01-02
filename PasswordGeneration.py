import random
print("PASSWORD GENERATION PROJECT!")
uc=int(input("Enter the length of password: "))
cc=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7"
,"8","9","!","@","#","$","%","^","&","*","-","+","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w",
"v","w","x","y","z"]
cl = 0
sl=0
dt = 0
sy = 0
for i in range (0,uc):
    cd=random.choice(cc)
    print(cd,end="")
    for char in cd:
        if "A"<= char <= "Z":
            cl += 1
        elif "0"<=char <= "9":
            dt +=1
        elif "a"<=char <= "z":
            sl +=1
        else:
            sy += 1

print("\nLetters =", cl)
print("Digits =",dt)
print("Symbols =",sy)
print("Small=",sl)
if uc>=12 and cl>=1 and sl>=1 and sy>=1 and dt>=1 :
    print("Strong Password")
else:
    print("Weak Password")
