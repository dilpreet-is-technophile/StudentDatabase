import sqlite3

conn = sqlite3.connect('result.db')

c = conn.cursor()

# c.execute("""CREATE TABLE Teacher_login(
#             Teacher_id integer,
#            Teacher_pass text
# )""")

c.execute(
    """INSERT INTO Teacher_login VALUES(3,'John')""")

# c.execute("""SELECT * FROM Student_login WHERE student_id=3""")
# print(c.fetchone())

conn.commit()

conn.close()
