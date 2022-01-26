import sqlite3

print("This is the Beginning of the database application.")

sqlite_file = './LabAssignment5.sqlite'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

print("Connecting to database file: " + sqlite_file)
print("Connected.\n")

c.execute("DROP TABLE IF EXISTS STUDENT")

sql = """CREATE TABLE STUDENT (StudentID INTEGER, StudentLastName TEXT, StudentFirstName TEXT, DOB TEXT, IsActive TEXT);"""

c.execute(sql)


c.execute('''INSERT INTO STUDENT (StudentID, StudentLastName, StudentFirstName, DOB, IsActive)VALUES (100001, 'Johnson','Ariel', '1999-07-10', 'N' ), (100002, 'Green', 'Robin', '2001-11-02', 'N'), (100003, 'Johnson', 'Charles', '1995-01-12', 'N'), (100004, 'Pearson', 'Jeffery', '1996-02-06', 'N'), (100005, 'Sears',  'Miguel', '1998-10-31', 'N' ), (100006, 'Kyle', 'Leah', '2000-05-29', 'N' ), (100007, 'Myers', 'Lynda', '1980-08-24', 'N' )''')

conn.commit()

print("New rows are inserted. Current rows in the table are: ")

c.execute("SELECT * FROM STUDENT")

updatedtable = c.fetchall()

for x in updatedtable:
  print(x)

sql = "DELETE FROM STUDENT WHERE (StudentID = '100002')"

c.execute(sql)

conn.commit()

sql = "DELETE FROM STUDENT WHERE (StudentID = '100005')"

c.execute(sql)

conn.commit()

sql = "DELETE FROM STUDENT WHERE (StudentID = '100006')"

c.execute(sql)

conn.commit()

c.execute("SELECT * FROM STUDENT")

print("============================================================")
print("\nRows are deleted. Current rows in the table are: ")

#print
updatedtable = c.fetchall()

for x in updatedtable:
  print(x)

c.execute(sql)

conn.commit()

sql = "SELECT * FROM STUDENT WHERE StudentID = '100007'"

c.execute(sql)

print("============================================================")
print("\nLast name is updated. The updated row is: ")
#print
updatedtable = c.fetchall()

for x in updatedtable:
  print(x)

print("============================================================")
#Request user input
print('\nWhich student’s information do you want to see?')
x =  input('Enter Student Number: ')
y = "SELECT * FROM STUDENT WHERE StudentID = " + x
print("The information of student " + x + " is: ")

sql = y

c.execute(sql)

#print
myresult = c.fetchall()

for x in myresult:
  print(x)

print("============================================================")

quit = False;
while quit != True :
  cont = input("Do you want to see another student(Y/N)?")
  if(cont  == "Y" or cont  == "y" ):
    print('\nWhich student’s information do you want to see?')
    x =  input('Enter Student Number: ')
    y = "SELECT * FROM STUDENT WHERE StudentID = " + x
    print("The information of student " + x + " is: ")

    sql = y

    c.execute(sql)

    #print
    myresult = c.fetchall()

    for x in myresult:
      print(x)

    print("==========================================================\n")
  if(cont == "N" or cont == "n"):
    quit = True

c.execute("DELETE FROM STUDENT")

conn.commit()
conn.close()

print("\nAll data in the table is deleted.")
print("Program terminated.")

