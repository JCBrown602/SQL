
import sqlite3

try:
    sqliteConnection = sqlite3.connect('kismetlab.db3')

    cursor = sqliteConnection.cursor()
    print('DB Init')

    query = 'select sqlite_version()'

    cursor.execute(query)
    result = cursor.fetchall()
    print('SQLite Version is {}'.format(result))

    cursor.close()

except sqlite3.Error as error:
    print('Error: ', error)

finally:

    if sqliteConnection:
        sqliteConnection.close()
        print('SQLite Connection Closed')
