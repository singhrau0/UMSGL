from insert import inserted
from update import updated
from delete import deleted
from read import readed
obj = inserted()
obj2 = updated()
obj3 = deleted()
obj4 = readed()

print("Welcome to the University Management System!")
print("Database Information:")
print("- Number of tables: 4")
print("- Table names: Student, Department, Faculty, Course")

# Displaying student table information
print("\nStudent Table Information:")
print("- Number of records: 4")
print("- Columns: sid, sname, courseid, dptid")

# Displaying department table information
print("\nDepartment Table Information:")
print("- Number of records: 2")
print("- Columns: departmentid, departmentname")

# Displaying faculty table information
print("\nFaculty Table Information:")
print("- Number of records: 5")
print("- Columns: facultyid, facultyname, departmentid, salary, courseid")

# Displaying course table information
print("\nCourse Table Information:")
print("- Number of records: 4")
print("- Columns: courseid, coursename, coursefees, duration")


print('------------------------------------------------------------')

print('**You can do 4 operation on database **')
print('for adding the data write *add*:')
print('for updating the data write *update*:')
print('for deleting the data write *delete*:')
print('for reading the data write *read*:')
opr = input('Please Enter the Oeration:')

if opr=='add':
    print('For inserting data in department table please press - 1:')

    tab = int(input("please enter the number to insert data in table:"))

    if tab==1:
        dtid = int(input("Please Eneter dptid:"))
        dtname = input("please Enter Department Name:")
        obj.dptinsert(dtid,dtname)

if opr=='update':
    print('For updating data in department table please press - 1:')

    tab = int(input("please enter the number to update data in table:"))

    if tab==1:
        col = input("Please Enter the Column Name:")
        old = input("Please enter the oldvalue:")
        new = input("Please Enter the New Value:")
        obj2.dptupdate(colname=col,oldval=old,newval=new)
if opr=='delete':
    print('For deleting data in department table please press - 1:')

    tab = int(input("please enter the number to delete data in table:"))

    if tab==1:
        id = int(input("Please Enter the Department ID to delete data:"))
        obj3.dptdelete(id)
if opr=='read':
    print('For reading data in department table please press - 1:')

    tab = int(input("please enter the number to read data in table:"))

    if tab==1:
        id = int(input("Please Enter the Department ID to read data:"))
        obj4.readdpt(id)
