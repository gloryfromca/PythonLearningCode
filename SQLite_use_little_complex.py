import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)


conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()

def get_score_in(low, high):
    con = sqlite3.connect(db_file)
    cursor = con.cursor()
    cursor.execute('select * from user order by score')
    value=cursor.fetchall()
    print(value)
    cursor.execute('select * from user  where (score>? and score<?) order by score asc ',(low,high))#注意传参数的写法，别很智障的直接写进去low,high
    value=cursor.fetchall()
    print(value)
    cursor.close()
    con.close()
get_score_in(70,100)