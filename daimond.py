N=int(input()) 
for i in range(1,N+1):
    print(" "*(N-i)+("*"+" ")*i+" "*(N-i)) 
for i in range(1,N):
    if i<N-1:
        print(" "*i+"* "+"  "*(N-i-2)+"*") 
    else:
        print(" "*(N-1)+"* ")
    
