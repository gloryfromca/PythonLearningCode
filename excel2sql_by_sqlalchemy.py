from sqlalchemy import Column, String, create_engine,MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Table
import xlrd
data=xlrd.open_workbook('C:/Users/Administrator/Desktop/123.xls')
table=data.sheets()[1]
# print(type(table))
# print(table.row_values(1))
# print(type(table.row_values(1)))
# print(type(table.row_values(1)[9]))
engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test1')
metadata=MetaData()
alldata=Table('alldata',metadata,
Column('num',String(20), primary_key=True),
Column('id',String(100)),
Column('mail',String(100)),
Column('name',String(100)),
Column('serv',String(20))
# serv = Column('serv',String(20))奇葩的错误原因
             ) 

metadata.drop_all(engine)
# metadata.create_alldata(engine)
alldata.create(engine,checkfirst=True)

Base = declarative_base()
class alldata(Base):
    __tablename__ = 'alldata'
    num = Column('num',String(20), primary_key=True)
    id = Column('id',String(100))
    mail = Column('mail',String(100))
    name  = Column('name',String(100))
    serv = Column('serv',String(20))


DBSession = sessionmaker(bind=engine)
session = DBSession()

try:
    i=0
    while i<table.nrows:
        a=table.row_values(i)
        new_user = alldata(num=a[0],id=a[1], mail=a[2],name=a[3],serv=a[4])
        session.add(new_user)  
        i=i+1
        session.commit()
except Exception as e:
    session.rollback()
    raise e
finally:
    session.close()




