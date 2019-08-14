import json
import requests
response = requests.get("https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=BTC&apikey=TLPB5KRYPO2BX23A")
todos = json.loads(response.text)
v1=todos['Realtime Currency Exchange Rate']
import pymysql.cursors


# Connect to the database.
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='password',
                             db='bitcoin',
                         )

print ("connect successful!!")


try:


    with connection.cursor() as cursor:

        # SQL

        # Execute query.
        sql="select * from bitcoin"
        cursor.execute(sql)

        print ("cursor.description: ", cursor.description)


finally:
    # Close connection.
    connection.close()
