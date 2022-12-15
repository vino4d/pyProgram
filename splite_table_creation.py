#Program to create db & tables using sqlite3

import sqlite3
#create db
conn=sqlite3.connect("companydetails.db")
c=conn.cursor()

#create table Employee
c.execute("create table Employee(emp_id integer primary key, name text, salary integer)")
#insert val to Employee
c.execute("insert into Employee values('1','aaa','44000')")
c.execute("insert into Employee values('2','bbb','55800')")

#Create table Department
c.execute("create table Department(dept_name text, emp_id integer, foreign key(emp_id) references Employee(emp_id) )")
#insert val into Department
c.execute("insert into Department values('Engineering',1)")
c.execute("insert into Department values('Tech support',2)")

#Create table Project
c.execute("create table Project(project_name text, role text, emp_id integer, foreign key(emp_id) references Employee(emp_id) )")
#insert val into Project
c.execute("insert into Project values('Automation Evole','Project Manager',1)")
c.execute("insert into Project values('Automation Evole','Support Engineer',2)")

conn.commit()
# to to print tables one by one for ref
c.execute("select * from Employee")
print(c.fetchall())
c.execute("select * from Department")
print(c.fetchall())

c.execute("select* from Project;")
print(c.fetchall())

print("†***********†")
#to print data by combined tables
c.execute("select Employee.emp_id,Employee.name,Project.project_name from(Employee inner join Project on Employee.emp_id=Project.emp_id)")
print(c.fetchall())
print("†***********†")
c.execute("select a.*,b.project_name,b.role,c.dept_name from((Employee as a inner join Project as b on a.emp_id=b.emp_id) inner join Department as c on a.emp_id=c.emp_id)")
print(c.fetchall())
