#single line Calculator
'''
Calculator that doing arthimetic operations
on single line queries by user.
Example: 6+8/2-3
         5/7*44+7-540
         4+8/9-55+34-22*2-6*295
'''

#lib for spl split func
import re
#to get user input
a=input()
num=re.split('(\+|/|-|\*)',a) 
    
#to separate operators 
oper=[] 
for i in range(len(num)):
    if num[i]=='+'or num[i]=='/'or num[i]=='*'or num[i]=='-':
        oper.append(num[i])
        
#to separate int values
val=[]
val=re.split('[+/\-\*]',a)
        
#define func to perfrom arthimetic operations using list of oper & val       
def arthmetic_func(sign):
    while sign in oper:
        for i in range(len(oper)):
            
            if oper[i]==sign:
                a=float(val[i])
                b=float(val[i+1])
                if sign=='/':
                    ans=a/b
                if sign=='*':
                    ans=a*b
                if sign=='+':
                    ans=a+b
                if sign=='-':
                    #assign sign and add elements to list for avoid precedence error
                    ans=a
                    val[i+1]=-b
                    val.insert(i,'dummy')
                    oper.insert(i+1,'+')
                oper.pop(i)
                oper.append('end')
                val.pop(i)
                val.pop(i)
                val.insert(i,ans)
    
while oper[0]!='end':
    arthmetic_func('/')
    arthmetic_func('*')
    arthmetic_func('-')
    arthmetic_func('+')
            
print(val[0])
                  
