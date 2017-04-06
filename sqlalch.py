from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()
class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    department_id = Column(Integer, ForeignKey('department.id'))
    department = relationship(Department, backref=backref('employees', uselist=True))

engine = create_engine('sqlite:///')

session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
print('database created')

vekt = Employee(name='Vekt')
kabbal = Department(name='Black Sun')
vekt.department = kabbal
s = session()
s.add(vekt)
s.add(kabbal)
s.commit()
print('Changes commited')


