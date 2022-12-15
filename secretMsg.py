#Secret Message
'''
Program to Encrypt the text that given by
user. Encryption node was reverse alphabets.
EXAMPLE: Abcd -> zyxw

'''


import string 
msg=input().lower()
#get list of revrse alphabets
alp=string.ascii_lowercase
ralp=alp[::-1]
smsg=list()
n=0
ni=0
#compare user text& revrse list to encrypt
for m in msg:
    if m.isalpha():
        for al in alp:
            if al==m:
                break
            n+=1
        
        for ral in ralp:
            if ni==n:
                smsg.append(ral)
            
                break
            ni+=1
    else:
        smsg.append(m)
sm="".join(smsg)
print(sm)          