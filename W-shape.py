N=int(input())
M=0
print("* "*(2*N-1))
for i in range(1,N):

    print((" "*i+"* "*(N-i))+" "*M+("* "*(N-i)))
    M=M+2
