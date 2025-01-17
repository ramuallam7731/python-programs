num_list = [(10, 20, 30), (1, 2), (5, 10, 15, 45)]
# Write your code here
n=int(input())
lista=[]
for i in num_list:
    new=i[:-1]+(n,)
    lista.append(new)
print(lista)    
    
