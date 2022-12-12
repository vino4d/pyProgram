a=0
b=0
t=0
d=100
while True:
    #t is time
    t+=1
    #a steps forward 1step per sec n reverse 2 step for every 10 sec
    if t%10==0:
        a-=2
        a+=1
    else:        
        a+=1
     #b steps forward 2step per sec n reverse 1 step for every 5 sec    
    if t%5==0:
        b-=1
        b+=2
    else:
        b+=2
    #to calc exact time for distance
    if a+b>d:
        t-=1
        a-=1
        b-=2
        t+=(d-a-b)/3
        break
print(t)