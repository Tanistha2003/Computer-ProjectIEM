while(True):
    print("Press 1 to do student operations")
    print("Press 2 to do course operations")
    print("Press 3 to do batch operations")
    print("Press 4 to do department operations")
    print("Press 5 to do examination operations")
    print("Press 0 to stop")
    x = int(input("Enter your choice: "))
    if(x == 0):
        break
    else:
        if(x==1):
            from student import *
            while(True):
                print("1.To create Student")
                print("2.To update student")
                print("3.To remove student")
                print("4.To generate report card")
                ch=int(input("Enter your choice"))
                if(ch==1):
                    namenew=input("Enter Student name you want to create")
                    student_id=input("Enter Student id you want to create")
                    createstudent(student_id,namenew)
                elif(ch==2):
                    chngstudent_id=input("Enter student id that you want to change")
                    updaterecord(chngstudent_id)
                elif(ch==3):
                    deleteStudentId=input("Enter Student id that you want to remove")
                    removestudent(deleteStudentId)
                elif(c==4):
                    reportstudentid=input("Enter student id that you want to calculate marks")
                    reportCard(reportstudentid)
                else:
                    print("Invalid input")
                    break
        elif(x==2):
            from course import *
            while(True):
                 print("1.To create Course")
                 print("2.To view performance")
                 print("3.To view course statistics")
                 print("4.To stop")
                 ch=int(input("Enter your choice"))
                 if(ch==1):
                    coursename=input("Enter course name you want to create")
                    course_id=input("Enter course id you want to create")
                    create_Course(course_id,coursename)
                 elif(ch==2):
                    course_id=input("Enter course id that you want to view performance of")
                    view_performance(course_id)
                 elif(ch==3):
                    course_id=input("Enter course id to view statisctics")
                    course_stats(course_id)
                 elif(c==4):
                     break
        elif(x==3):
            from batch import *
            while(True):
                 print("1.To create batch")
                 print("2.To view list of students")
                 print("3.To view courses taught")
                 print("4.To view complete performance")
                 print("5.To view piechart percentage")
                 print("6.To stop")
                 ch=int(input("Enter your choice"))
                 if(ch==1):
                    batchname=input("Enter batch name you want to create")
                    createBatch(batchname)
                 elif(ch==2):
                    batch_id=input("Enter batch id to view students of")
                    viewStudents(batch_id)
                 elif(ch==3):
                    batch_id=input("Enter batch id to view courses")
                    viewCourses(batch_id)
                 elif(ch==4):
                    batch_id=input("Enter batch id to see complete performance")
                    viewPerformance(batch_id)
                 elif(ch==5):
                    batch_id=input("Enter batch id to view piechart percentage")
                    pieChart(batch_id)
                 elif(ch==6):
                    break
        elif(x==4):
            from department import *
            while(True):
                 print("1.To create department")
                 print("2.To view department")
                 print("3.To view average performance")
                 print("4.To view line plot")
                 print("5.To stop")
                 ch=int(input("Enter your choice"))
                 if(ch==1):
                    departmentid=input("Enter department id that you want to create")
                    department_name=input("Enter department name that you want to create")
                    createdepartment(departmentid,department_name)
                 elif(ch==2):
                    department_id=input("Enter department id to view")
                    view_department(department_id)
                 elif(ch==3):
                    department_id=input("Enter department id to view average performance")
                    average_performance(department_id)
                 elif(ch==4):
                    department_id=input("Enter department id to see line plot")
                    lineplot(department_id)
                 elif(ch==5):
                    break
        elif(x==5):
            from examination import*
            while(True):
                 print("1.To enter marks")
                 print("2.To view performance")
                 print("3.To view scatterplot")
                 print("4.To stop")
                 ch=int(input("Enter your choice"))
                 if(ch==1):
                    courseid=input("Enter course id that you want to enter marks to")
                    
                    enterMarks(courseid)
                 elif(ch==2):
                    course_id=input("Enter course id to view performance")
                    view_performance(course_id)
                 elif(ch==3):
                    
                    scatterplot()
                 elif(ch==4):
                    break
        else:
            print("Invalid.Please try again")
            


                     
                



