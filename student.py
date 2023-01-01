import csv
import pandas as pd
from createBatch import batch
def createstudent(student_id,namenew):
    studentid=[]
    studentid[:0]=student_id
    classrollno=studentid[5:7]
    batchname=studentid[0:3]
    datanew=[student_id,namenew,classrollno,batchname]
    csv_reader=[]
    with open("student.csv","r",newline="\n") as f:
        csv_reader=list(csv.reader(f, delimiter=","))
    fh=open("student.csv","w",newline="\n")
    for i in range(0,len(csv_reader)):
        if(csv_reader[i][0]==student_id):
           print("Data already exist")
           return
        else:
            stuwriter=csv.writer(fh)
            stuwriter.writerow(datanew)
def updaterecord(chngstudent_id):
    csv_reader=[]
    with open("student.csv","r",newline="\n") as f:
        csv_reader=list(csv.reader(f, delimiter=","))
    check=0
    column=0
    for i in range(0,len(csv_reader)):
        if(csv_reader[i][0]==chngstudent_id):
           check=1
           column=i
           break
    if(check==0):
        print("Student id does not exist")
        return
    print("1.Change student Id")
    print("2.Change Student name")
    i=int(input("Enter choice of change"))
    if(i==1):
        name1=csv_reader[column][1]
        removestudent(chngstudent_id)
        idnew=input("Enter updated id")
        df=pd.read_csv("student.csv")
        df.loc[column,"Student Id"]=idnew
        df.to_csv("student.csv",index=False)
        createstudent(idnew,name1)
    elif(i==2):
        namenew=input("Enter updated name")
        df=pd.read_csv("student.csv")
        df.loc[column,"Student Name"]=namenew
        df.to_csv("student.csv",index=False)
    else:
        print("Invalid choice")
def removestudent(deleteStudentId):
    csv_reader=[]
    with open("student.csv", "r", newline = "\n") as f:
        csv_reader = list(csv.reader(f, delimiter=","))
    check=0
    column=0
    for i in range(0,len(csv_reader)):
        if(csv_reader[i][0] ==deleteStudentId):
            check=1
            column=i
            break
    if(check==0):
        print("Incorrect Id Input")
        return
    else:
        df=pd.read_csv("student.csv")
        df=df.iloc[column-1,column]
def reportCard(reportstudentid):
     name=""
     csv_reader=[]
     with open("student.csv", "r", newline = "\n") as f:
        csv_reader = list(csv.reader(f, delimiter=","))
        check=0
        for i in range(0,len(csv_reader)):
            if(csv_reader[i][0] == reportstudentid):
                check=1
                name=csv_reader[i][1]
                break
        if(check==0):
            print("Wrong student id")
            return
     f=open((reportstudentid + ".txt"),"w")
     a="Student Id:" + reportstudentid + "\n"
     b="Student name:" + name + "\n"
     f.writelines([a,b])
     with open("course.csv", "r", newline = "\n") as fx:
        csv_reader = list(csv.reader(fx, delimiter=","))
     marks=[]
     subjects=[]
     for i in range(1, len(csv_reader)):
        marks.append(csv_reader[i][2])
        subjects.append(csv_reader[i][1])
     totalmarks=100
     obtainedmarks=0
     for i in range(0,len(subjects)):
        obtainedmarks=obtainedmarks+marks[i]
        percentage=(obtainedmarks/totalmarks)*100
        if(percentage >=90):
            print("In subject",subjects[i],"marks obtained",obtainedmarks,"grade","A","Pass")
        elif(percentage>=80):
            print("In subject",subjects[i],"marks obtained",obtainedmarks,"grade","B","Pass")
        elif(percentage>=70):
            print("In subject",subjects[i],"marks obtained",obtainedmarks,"grade","C","Pass")
        elif(percentage>=60):
            print("Insubject",subjects[i],"marks obtained",obtainedmarks,"grade","D","Pass")
        elif(percentage>=50):
            print("In subject",subjects[i],"marks obtained",obtainedmarks,"grade","E","Pass")
        else:
            print("In subject",subjects[i],"marks obtained",obtainedmarks,"grade","F","Fail")
def gradecheck(a):
    if(a>=90):
        return "A"
    elif(a>=80):
        return "B"
    elif(a>=70):
        return "C"
    elif(a>=60):
        return "D"
    elif(a>=50):
        return "E"
    else:
        return "F"         







    
    
    





