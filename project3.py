from sqlalchemy import *
from sqlalchemy.orm import declarative_base,sessionmaker
DB_URL = "mysql://root:abcdef@localhost:3306/adhyayan"

ENG = create_engine(DB_URL)
print(ENG)
Base = declarative_base()

class Student(Base):
    __tablename__ = "student_tb1"
    rn = Column(Integer,primary_key=True)
    name = Column(String(32))
    marks = Column(Float)


Base.metadata.create_all(ENG)
print("Table Created")

Session = sessionmaker(bind=ENG)
sess = Session()
'''
#Session = sessionmaker(bind=ENG)

#s1 = Student(rn=1,name="abcd",marks=10.0)
#s2 = Student(rn=2,name="efgh",marks=20.0)
#s3 = Student(rn=3,name="ijkl",marks=30.0)
#s4 = Student(rn=4,name="mnop",marks=40.0)
#s5 = Student(rn=5,name="qrst",marks=50.0)
#sess.add(s1)
#sess.commit()
#print("Object created")

students = sess.query(Student)
for  stu in students:
    print(stu.rn,stu.name,stu.marks)
    '''
while True:
 ch = int(input(" Enter Your Choice:\n1.Add Student.\n2.Update Student\n3.Delete STudent.\n4.Show Student\n5.Exit"))
 match ch:
    case 1:
        print("Add a student")
        r = int(input("enter roll number"))
        n = input("enter name")
        m = float(input("enter marks"))
        s1 = Student(rn=r,name=n,marks=m)
        sess.add(s1)
        sess.commit()
        print("succesfully added")
    case 2:
        print("Update a student")
        r = int(input("enter roll number to update"))
        #n = input("enter name")
        m = float(input("enter updated marks"))
        sess.query(Student).filter(Student.rn==r).update({Student.marks:m})
        sess.commit()
        print("Sucessfully updated ")
    case 3:
        print("Delete a student")
        r = int(input("enter roll number to delete"))
        x = sess.query(Student).filter(Student.rn==r).delete()
        print(x)
        #print("Deleted Sucessfully")
        if x==0:
            print("roll no is not available")
        else:
            print("deleted sucessfully")
        sess.commit()    
        
                 
    case 4:
        print("Show a student")
        students = sess.query(Student)
       # print(students)
       # print(students.value())
        print("ln75=",students.count())
        if stu in students.count==0:
            print("student unavailable")

        else:
            for stu in students:
                print(stu.rn,'\t',stu.name,'\t',stu.marks)
            
    case 5:
        print("Exit...")
        break
    case _:
        print("invalid choice")
        
