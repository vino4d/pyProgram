#Program to calc age of employees on Csv file


#install pandas library for processing data
import pandas as pd 
import datetime as dt

#to get Csv file from users
filepath=input("enter the filepath")
delimiters=input("enter the delimiters")
quotechar=input("enter the quotechar")
df=pd.read_csv(filepath,sep=delimiters,quotechar=quotechar)

df['birthdate'] = pd.to_datetime(df['birthdate'])
#to calc age
df['age']=(dt.datetime.now()-df['birthdate'])/365.24

for i in range(len(df)):
    a=str(df.loc[i,'age'])
    a=a.split()
    df.loc[i,'age']=int(a[0])
print(df.to_string())
