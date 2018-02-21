import sqlite3

connection = sqlite3.connect('jeopardy.db')
cursor = connection.cursor()

cursor.execute("SELECT name,game FROM category LIMIT 20")
results = cursor.fetchall()

print "Example categories:\n"
for category in results:
    name, game = category
    print "%s (game #%s)" %(name, game)



connection.close()
