import sqlite3

connection = sqlite3.connect('jeopardy.db')
cursor = connection.cursor()

cursor.execute("SELECT clue.text, clue.answer, category.name FROM clue, category WHERE isDD AND clue.category = category.id LIMIT 10")
results = cursor.fetchall()

print "\nExample clues:\n"
for clue in results:
    text, answer, name = clue
    print "[%s]" % (name,)
    print "A: %s" % (text,)
    print "Q: What is '%s'" % (answer,)
    print ""

connection.close()
