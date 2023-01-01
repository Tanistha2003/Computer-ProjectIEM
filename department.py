import json
import csv
from matplotlib import pyplot

def view_department(department_id1):
    csv_reader=[]
    batches=[]
    with open("department.csv","r",newline="\n") as f:
        csv_reader=list(csv.reader(f,delimiter=","))
    for i in range(0,len(csv_reader)):
        if(csv_reader[i][0]!=department_id1):
            print("Incorrect id given")
            return
        else:
            batches=csv_reader[i][2].split(":")
            break
    print("Batches in",department_id1,":")
    for i in batches:
        print(i)
def createdepartment(department_id,department_name):
    csv_reader=[]
    with open("department.csv","r",newline="\n") as f:
        csv_reader = list(csv.reader(f, delimiter=","))
    for i in range(0,len(csv_reader)):
        if(csv_reader[i][0]==department_id):
            print("Already exists")
            return
    data=[department_id,department_name,""]
    fh=open("department.csv","w",newline="\n")
    departmentwriter=csv.writer(fh)
    departmentwriter.writerow(data)
def average_performance(department_id2):
    csv_reader=[]
    with open("department.csv","r",newline="\n") as f:
        csv_reader=list(csv.reader(f,delimiter=","))
    batch=[]
    for i in range(0,len(csv_reader)):
        if(csv_reader[i][0]!=department_id2):
            print("Wrong id given")
            return
        else:
            batch=csv_reader[i][2].split(":")
            break
    if(len(batch)==0):
        print("No batches present")
        return
    performance=[]
    for i in batch:
        course=[]
        with open("batch.csv","r",newline="\n") as fh:
            csv_reader1=list(csv.reader(fh,delimiter=","))
        for j in range(0,len(csv_reader)):
            if(csv_reader1[j][0]==i):
                course=csv_reader1[j][3].split(":")
                break
        for cs in course:
            with open("course.csv","r",newline="\n") as fh:
                csv_reader2=list(csv.reader(fh,delimiter=","))
            obtainedmarks=[]
            store=[]
            for m in csv_reader2:
                store.append(json.loads(csv_reader2[m][2]))
                tm=0
                div=0
                for subjects in m:
                    tm=tm+subjects.get(m)
                    div=div+1
            if(div!=0):
             obtainedmarks.append(tm/div)
            else:
              obtainedmarks.append(0)
        total=0
        divs=0
        for x in obtainedmarks:
            total=total+x
            divs+=1
        if(div!=0):
            performance.append(total/divs)
        else:
            performance.append(0)
    total1=0
    divs1=0
    for y in range(0,len(csv_reader)):
        total1=total1+performance[y]
        divs+=1
    avg=0
    if(divs!=0):
        avg=total1/divs1
        print("Average percentage obtained in",department_id2,"is",avg)
def lineplot(department_id3):
    with open("department.csv", "r", newline = "\n") as f:
        csv_reader = list(csv.reader(f, delimiter=","))
    check = 0
    batches = []
    for i in range(1, len(csv_reader)):
        if(csv_reader[i][0] == department_id3):
            check = 1
            batches = csv_reader[i][2].split(":")
            break
    if(check == 0):
        print("Department ID does not exist")
        return
    if(len(batches) == 0):
        print("No batches in department")
        return
    performances = []
    for batch in batches:
        students = []
        student_performances = []
        with open("batch.csv", "r", newline = "\n") as f:
            csv_reader = list(csv.reader(f, delimiter=","))
        for i in range(0, len(csv_reader)):
            if(csv_reader[i][0] == batch):
                students = csv_reader[i][4].split(":")
                break
        for student in students:
            with open("course.csv", "r", newline = "\n") as f:
                csv_reader = list(csv.reader(f, delimiter=","))
            all_marks = []
            for i in range(1, len(csv_reader)):
                all_marks.append(json.loads(csv_reader[i][2]))
            total_marks = 0
            divs = 0
            for subjects in all_marks:
                if(isinstance(subjects.get(student), int)):
                    total_marks += subjects.get(student)
                    divs += 1
            if(divs != 0):
                student_performances.append(total_marks/divs)
            else:
                student_performances.append(0)
        total_marks = 0
        divs = 0
        for x in student_performances:
            total_marks += x
            divs += 1
        if(divs != 0):
            performances.append(total_marks/divs)
        else:
            performances.append(0)
    pyplot.plot(batches, performances)
    pyplot.show()


            











      