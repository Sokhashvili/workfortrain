from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from faker import Faker
from datetime import date

Base = declarative_base()
fake = Faker()


class Department(Base):
    __tablename__ = 'department'
    DepartmentID = Column(Integer, primary_key=True)
    DepartmentName = Column(String, nullable=False)


class Employee(Base):
    __tablename__ = 'employee'
    EmployeeID = Column(Integer, primary_key=True)
    FullName = Column(String, nullable=False)
    HireDate = Column(Date, nullable=False)
    DepartmentID = Column(Integer, ForeignKey('department.DepartmentID'), nullable=False)
    department = relationship("Department")


engine = create_engine('sqlite:///company.db', echo=True)


Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()


dept1 = Department(DepartmentName=fake.company())
dept2 = Department(DepartmentName=fake.company())
session.add(dept1)
session.add(dept2)
session.commit()


emp1 = Employee(FullName=fake.name(), HireDate=fake.date_between(start_date='-5y', end_date='today'), DepartmentID=dept1.DepartmentID)
emp2 = Employee(FullName=fake.name(), HireDate=fake.date_between(start_date='-5y', end_date='today'), DepartmentID=dept2.DepartmentID)
session.add(emp1)
session.add(emp2)
session.commit()


employees = session.query(Employee).all()
for emp in employees:
    print(f"EmployeeID: {emp.EmployeeID}, FullName: {emp.FullName}, HireDate: {emp.HireDate}, Department: {emp.department.DepartmentName}")

departments = session.query(Department).all()
for dept in departments:
    print(f"DepartmentID: {dept.DepartmentID}, DepartmentName: {dept.DepartmentName}")