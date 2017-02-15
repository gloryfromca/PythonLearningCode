import  mysql.connector 
con=mysql.connector.connect(user='root',password='password',database='test')
cursor=con.cursor()
# cursor.execute('create table user (id varchar(20) primary key,name varchar(20))')
# cursor.execute('insert into user (id,name) values(%s,%s)',['3','michael'])
con.commit()
cursor.close()
cursor=con.cursor()
cursor.execute('select * from user where id = %s', ('3',))
values = cursor.fetchall()
print(values)
cursor.close()
con.close()

