import os
import time
from check import Run

delay = 10

closetime = time.time()+delay
print(time.ctime(closetime))
while time.time() < closetime:
    obj = Run()
    obj.run()

print("hi")
a=[]
for i in range(0, 10):
    a.append(i)

print(a)

def newfunction():
    pass

newfunction()


print(os.getcwd())

