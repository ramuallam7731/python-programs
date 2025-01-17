N=int(input()) 
for i in range(1,N+1):
    if i==1:
        print("  "*(N-1)+"*") 
    elif i==N:
        print("* "*N) 
    else:
        print("* "+"  "*(N-i-1)+"*")
