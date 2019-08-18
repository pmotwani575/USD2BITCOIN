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


with connection.cursor() as cursor:

    cursor.execute(
            "insert into `bitcoin`(`From_Currency Code`,`From_Currency Name`,`To_Currency Code`,`To_Currency Name`,`Exchange Rate`,`Last Refreshed`,`Time Zone`) values (%s,%s,%s,%s,%s,%s,%s) ", (v1['1. From_Currency Code'],v1['2. From_Currency Name'],
                    v1['3. To_Currency Code'],
                     v1['4. To_Currency Name'],
                     float( v1['5. Exchange Rate']),
                       v1['6. Last Refreshed'],
                        v1['7. Time Zone']
                           )
              )

    connection.commit();
