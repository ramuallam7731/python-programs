import datetime 
U=int(input())
zero=datetime.datetime(1970,1,1) 
seconds=datetime.timedelta(seconds=U)
time=seconds+zero 
print(time)
