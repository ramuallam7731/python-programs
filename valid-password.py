a=input() 
b=""
c="" 
d=""
for i in a:
    if i.isupper():
        b=True 
    elif i.islower(): 
        c=True 
    elif i.isdigit():
        d=True 
if b and c and d:
    print("Valid Password") 
else:
    print("Invalid Password")
        
