import csv
import json
import matplotlib.pyplot
import pandas 
import gradecheck from student
import createBatch from batch
import Counter from collections
def create_Course(course_id,course_name):
    csv_reader=[]
    marks_obtained_d={}
    with open("course.csv","r",newline="\n") as f:
        csv_reader=list(csv.read(f,delimiter=","))
    for i in range(0,len(csv_reader)):
        if(course_id==csv_reader[i][0]):
            print("Course Id exists")
            return
    while(True):
        student_id=input("Enter Student Id ( to stop enter STOP)")
        if(student_id.upper()=="STOP"):
            break
        else:
            marks=int(input("Enter marks obtained in course"))
            marks_obtained_d[student_id]=marks
    data=[course_id,course_name,marks_obtained_d]
    with open("course.csv","w",delimiter="\n") as fh:
        stu=csv.writer(fh)
    stu.writerow(data)
def view_performance(course_id):
    csv_reader=[]
    data=[]
    student_marks={}
    with open("course.csv","r",newline="\n") as f:
        csv_reader=list(csv_reader(f,delimiter=","))
    for i in range(0,len(csv_reader)):
        if(csv_reader[i][0]!=course_id):
            print("Wrong id")
            return
        else:
            student_marks = json.loads(csv_reader[i][2])
    student_id=list(student_marks,keys())
    with open("student.csv", "r", newline = "\n") as f:
        csv_reader = list(csv.reader(f, delimiter=","))
    for i in range(0, len(student_id)):
        for j in range(0, len(csv_reader)):
            if(student_id[i] == csv_reader[j][0]):
                print("Student ID: " + student_id[i])
                print("Student Name: " + csv_reader[j][1])
                print("Student Roll Number: " + csv_reader[j][2])
                print("Marks obtained: " + str(student_marks.get(student_id[i])))
                print()
                data.append([student_id[i], csv_reader[j][1], csv_reader[j][2], student_marks.get(student_id[i])])
    return data
def course_stats(course_id):
    csv_reader = []
    with open("course.csv", "r", newline = "\n") as f:
        csv_reader = list(csv.reader(f, delimiter=","))
    check = 0
    for i in range(0, len(csv_reader)):
        if(csv_reader[i][0] == course_id):
            check = 1
            break
    if(check == 0):
        print("Course ID does not exist")
        return
    x = view_performance(course_id)
    grades = []
    for a in x:
        grades.append(gradeCheck(a[3]))
    grades.sort()
    letter_counts = Counter(grades)
    df = pandas.DataFrame.from_dict(letter_counts, orient='index')
    df.plot(kind='bar')
    matplotlib.pyplot.show()   


            
            
       