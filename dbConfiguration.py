import mysql.connector as mysql

class DbConnection():
    def getConnection():
        connection = mysql.connect(
            host='127.0.0.1',
            database='sniffer_temperacture',
            user='root',
            password='admin'
        )

        if connection.is_connected():
            print('Connected at MySql Server', connection.database)

        return connection; 
