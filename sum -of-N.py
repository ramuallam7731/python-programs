X=int(input())
N=int(input())
sum=0
pwr=1
for i in range(1,N+1):
    if i%2!=0:
        num=X**i
        i=i+2
    else:
        num=-(X**i) 
        i=i+2
    sum=sum+num        
print(sum)    
