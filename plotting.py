import mysql.connector
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import array as arr
TimeLineArray= arr.array('i', [])
ExchangeRateArray=arr.array('i', [])

from mysql.connector import Error
try:
   mySQLconnection = mysql.connector.connect(host='localhost',
                             database='bitcoin',
                             user='root',
                             password='password')
   sql_select_Query = "select Exchange Rate ,Last Refreshed Time from bitcoin"
   cursor = mySQLconnection .cursor()
   cursor.execute(sql_select_Query)
   records = cursor.fetchall()
   print("Total number of rows in bitcoin is - ", cursor.rowcount)
   print ("make array out of the records retrieved")
   for row in records:
       print("Exchange Rate = ", row[0], )
TimeLineArray.push(row[0])
ExchangeRateArray.push(row[1])
       print("Last Refreshed Date ", row[1])
   cursor.close()

except Error as e :
    print ("Error while connecting to MySQL", e)
finally:
    #closing database connection.
    if(mySQLconnection .is_connected()):
        connection.close()
        print("MySQL connection is closed")


TimeLine=np.array(TimeLineArray)
ExchangeRate=np.array(ExchangeRateArray)

plt.scatter(TimeLine,ExchangeRate)
plt.title("Relationship between ExchangeRate and TimeLine")
plt.xlabel("TimeLine")
plt.ylabel("ExchangeRate")
plt.show()
