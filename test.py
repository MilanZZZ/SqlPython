import pyodbc
import time
server = '' #add server address ex. 192.168.0.1
port = '' #add port
database = ''
username = ''
password = ''
tableName = ''
sendFile = ''


try: #test to see if a connection can be established // also connect to server
   cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';PORT='+port+';DATABASE='+database+';UID='+username+';PWD='+ password)
except: #throw an exception if it can't
   print("connection failed, or sql server unavailable")

def showTable(tableName):

   cursor = cnxn.cursor()
   cursor.execute('SELECT * FROM {}'.format(tableName))

   for i in cursor:
      print(i)

def insertIntoTable(tableName, Value1):
   cursor = cnxn.cursor()
   cursor.execute('''INSERT INTO {}(TESTPODATAK) VALUES('{}')'''.format(tableName,Value1 )) #instead of TESTPODATAK insert column name/names from your table
   cnxn.commit()

insertIntoTable(tableName, sendFile)
showTable(tableName)





#