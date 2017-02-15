from sqlalchemy import Column,String,create_engine,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base
import  mysql.connector 
con=mysql.connector.connect(user='root',password='password',database='test')
cursor=con.cursor()
cursor.execute('create table if not exists book (id varchar(20) primary key,name varchar(20),user_id varchar(20))')
cursor.close()
con.close()
base=declarative_base()
class user(base):
	__tablename__='user'
	id=Column(String(20),primary_key=True)
	name=Column(String(20))
	book=relationship('book')
class book(base):
	__tablename__='book'
	id=Column(String(20),primary_key=True)
	name=Column(String(20))
	user_id=Column(String(20),ForeignKey('user.id'))

engine=create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
dbsession=sessionmaker(bind=engine)
session=dbsession()
new_book=book(id='1',user_id='119',name='learning python')
session.commit()
user=session.query(user).filter(user.id=='119').one()
# user=session.query(user).all()
print(user)
print(user.name)
print(user.book[0].name)
print(type(user.book))
session.close()
