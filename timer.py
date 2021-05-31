import time
import time
def add(a,b):
    return(a+b)

t0=time.time()
i=5
while(i>0):
    print(add(2,2))
    #time.sleep(1)
    i-=1
    print("time took :",i)
t1 = time.time()
tot=t1-t0
print("time took :",tot)  # just checking wheather the time is close enough