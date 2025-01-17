A=int(input())

r500=A//500 
re500=A%500 

r50=re500//50 
re50=re500%50 

r10=re50//10 
re10=re50%10 

r1=re10//1 
re1=re10%1

print("500: "+str(r500)+" 50: "+str(r50)+" 10: "+str(r10)+" 1: "+str(r1))
