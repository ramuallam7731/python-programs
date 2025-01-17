n=int(input())
for i in range(n):
    row=" "*i+"* "*(n-i) 
    print(row)
for i in range(2,n+1):
    row=" "*(n-i)+"* "*i 
    print(row)    
