import mysql.connector
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from functools import partial
import os
import matplotlib.figure
import matplotlib.patches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import datetime
import smtplib

mydb = mysql.connector.connect(
host = "localhost",
user = "root",
password = "nishi1503",
database = "school_portal")
mycursor = mydb.cursor()

class Teacher():

    def __init__(self, name, regno, dob, contactno, subject, pin, email):
        self.name = name
        self.regno = int(regno)
        self.dob = dob
        self.contactno = int(contactno)
        self.subject = subject
        self.pin = int(pin)
        self.emailID = email

class Student():

    def __init__(self, name, regno, dob, contactno, grade, section, pin, email):
        self.name = name
        self.regno = int(regno)
        self.dob = dob
        self.contactno = int(contactno)
        self.grade = int(grade)
        self.section = section
        self.pin = int(pin)
        self.emailID = email

def quit():
    root.destroy()

def start():
    welcomeLabel = Label(root, image= homelmsphoto ,text = "Learning Management System",compound = LEFT ,font=('Rubik-Regular',24),bg='#2c3436', fg= 'white').grid(column = 0, row = 0, padx = 70, pady = 60)

    createUserButton = Button(root, image=signupphoto, text = "SIGN UP",compound = LEFT, padx = 10, pady = 8, command = create_user, borderwidth = 1,font=('Rubik-Regular', 12,'bold'),bg='light green', fg= 'black').grid(column = 0, row = 3)

    loginButton = Button(root,image =loginkeyphoto, text = "LOGIN ", compound = LEFT, padx = 14, pady = 8, command = login, borderwidth = 1, font=('Rubik-Regular', 12,'bold'),bg='light green', fg= 'black').grid(row = 2, column = 0,pady=20)
    quit01Button = Button(root,image =quitphoto, text = "EXIT ", compound = LEFT, padx = 19, pady = 8, borderwidth = 1,command = quit, font=('Rubik-Regular', 12,'bold'),bg='light green', fg= 'black').grid(row = 4, column = 0,pady=20)
    copyrightLabel = Label(root, text = "Copyright © All Rights Reserved ",font=('Rubik-Regular',10),bg='#2c3436', fg= 'white').grid(column = 0, row = 5,pady=90,padx=390)

def create_user():

    root.wm_state('iconic')
    window1 = Toplevel()
    window1.title("Create User")
    window1.geometry("1000x600")
    window1.configure(bg = "#2c3436")
    window1.resizable(False, False)

    createUserLabel = Label(window1, image = lmsphoto ,text = "Create User For LMS" ,compound = LEFT , bg='#2c3136', fg= 'white',font=("Rubik-Regular", 24)).grid(row = 0, column = 1, padx = 70, pady = 60)

    RadioValue = StringVar()
    teacherRadio = Button(window1,image = teacherphoto, text = "TEACHER" ,compound =LEFT ,borderwidth = 1,border=0, bg='light green', fg= 'black',font = ('Rubik-Regular', 12 , 'bold'),padx = 10, pady = 10, command = create_teacher).grid(row = 1, column = 1)
    studentRadio = Button(window1, image = studentphoto ,text = "STUDENT", compound = LEFT, borderwidth = 1,border=0,bg='light green', fg= 'black',font = ('Rubik-Regular', 12,'bold'),padx = 10, pady = 10, command = create_student).grid(row = 2, column = 1,pady=50)
    copyrightLabel = Label(window1, text = "Copyright © All Rights Reserved ",font=('Rubik-Regular',10),bg='#2c3436', fg= 'white').grid(column = 1, row = 4,pady=180,padx=390)
def create_teacher():

    window_teacher = Toplevel()
    window_teacher.title("Create User")
    window_teacher.geometry("1000x600")
    window_teacher.configure(bg = "#2c3436")
    window_teacher.resizable(False, False)

    createUser = Label(window_teacher, image = lmsphoto,text = "LMS Users",compound = LEFT, bg='#2c3136', fg= 'white',font=("Rubik-Regular", 24)).grid(row = 0, column = 1, padx = 10,pady=10)

    nameLabel = Label(window_teacher, text = "Name",font=('Medium 500',12),bg='#2c3136', fg= 'white').grid(row = 2, column = 0, pady = 10)
    nameVar = StringVar()
    nameInput = Entry(window_teacher, textvariable = nameVar).grid(row = 2, column = 1, padx = (20, 20), pady = 10)

    regNoLabel = Label(window_teacher, text = "Registration number", font=('Medium 500',12),bg='#2c3136', fg= 'white').grid(row = 3, column = 0, pady = 10)
    regNoVar = IntVar()
    regNoInput = Entry(window_teacher, textvariable = regNoVar).grid(row = 3, column = 1, padx = (20, 20), pady = 10)

    dobLabel = Label(window_teacher, text = "Date of birth (YYYY-MM-DD)", font=('Medium 500',12),bg='#2c3136', fg= 'white').grid(row = 4, column = 0, pady = 10)
    dobVar = StringVar()
    dobInput = Entry(window_teacher, textvariable = dobVar).grid(row = 4, column = 1, padx = (20, 20), pady = 10)

    contactLabel = Label(window_teacher, text = "Contact number", font=('Medium 500',12),bg='#2c3136', fg= 'white').grid(row = 5, column = 0, pady = 10)
    contactVar = IntVar()
    contactInput = Entry(window_teacher, textvariable = contactVar).grid(row = 5, column = 1, padx = (20, 20), pady = 10)

    subjectLabel = Label(window_teacher, text = "Select Your Subject :-", font=('Medium 500',12),bg='#2c3136', fg= 'white').grid(row = 6, column = 0)
    subjectVar = StringVar()
    physicsRadio = Radiobutton(window_teacher, text = "PHYSICS",bg='#2c3136',border=0,padx=5,pady=5, fg= 'black' ,value = "Physics", font = ('Rubik-Regular', 12,'bold'), indicator = 0, background = "light green", variable = subjectVar).grid(row = 7, column = 0, padx = 0, pady = 30)
    mathsRadio = Radiobutton(window_teacher, text = "MATHEMATICS", bg='#2c3136',border=0,padx=5,pady=5, fg= 'black',value = "Maths", font = ('Rubik-Regulart', 12,'bold'), indicator = 0, background = "light green", variable = subjectVar).grid(row = 7, column = 1, padx = 0, pady = 30)
    chemistryRadio = Radiobutton(window_teacher, text = "CHEMISTRY",bg='#2c3136',border=0,padx=5,pady=5,fg= 'black', value = "Chemistry", font = ('Rubik-Regular', 12,'bold'), indicator = 0, background = "light green", variable = subjectVar).grid(row = 7, column = 2, padx = 0, pady = 30)
    csRadio = Radiobutton(window_teacher, text = "COMPUTER SCIENCE",bg='#2c3136',border=0,padx=5,pady=5,fg= 'black', value = "CS", font = ('Rubik-Regular', 12,'bold'), indicator = 0, background = "light green", variable = subjectVar).grid(row = 7, column = 3, padx = 30, pady = 30)

    emailLabel = Label(window_teacher, text = "Enter email address", font=('Medium 500',12),bg='#2c3136', fg= 'white').grid(row = 8, column = 0, pady = 10)
    emailVar = StringVar()
    emailInput = Entry(window_teacher, textvariable = emailVar).grid(row = 8, column = 1, pady = 10)

    pinLabel = Label(window_teacher, text = "Enter 4-digit pin", font=('Medium 500',12),bg='#2c3136', fg= 'white').grid(row = 9, column = 0, padx = (20, 20), pady = 10)
    pinVar = IntVar()
    pinEntry = Entry(window_teacher, textvariable = pinVar).grid(row = 9, column = 1, padx = (20, 20), pady = 10)
   
    def submit_createUser():

        try:
            teacherChar = Teacher(nameVar.get().title(), regNoVar.get(), dobVar.get(), contactVar.get(), subjectVar.get(), pinVar.get(), emailVar.get())
            sql = "INSERT INTO teachers (Name, Pin, Subject, RegistrationNo, DOB, ContactNo, EmailID) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (teacherChar.name, teacherChar.pin, teacherChar.subject, teacherChar.regno, teacherChar.dob, teacherChar.contactno, teacherChar.emailID)
            mycursor.execute(sql, val)
            mydb.commit()
            accountCreatedLabel = Label(window_teacher, text = "Account created successfully!",bg='#2c3136', fg= 'white' ).grid(row = 10, column = 1)

        except Exception as e:
            accoundNotCreatedLabel = Label(window_teacher, text = "Oops! We could not create the account.",bg='#2c3136', fg= 'white').grid(row = 10, column = 1)
            print(e)

    submitButton = Button(window_teacher,image = submitphoto ,text = "SUBMIT",compound = RIGHT, font=('Rubik-Regular',12,'bold'),command = submit_createUser,bg='light green', fg= 'black').grid(row = 10, column = 0,pady=30)
    copyrightLabel = Label(window_teacher, text = "Copyright © All Rights Reserved ",font=('Rubik-Regular',10),bg='#2c3436', fg= 'white').grid(column = 2, row = 11,pady=20,padx=2)
def create_student():

    window_student = Toplevel()
    window_student.title("Create User")
    window_student.geometry("1000x600")
    window_student.configure(bg = "#2c3436")
    window_student.resizable(False, False)

    createUserLabel = Label(window_student,image = lmsphoto, text = "LMS Users", compound = LEFT ,font=("Rubik-Regular", 24),bg='#2c3136', fg= 'white').grid(row = 0, column = 1, padx = 10, pady = 20)

    nameLabel = Label(window_student, text = "Name", font=('Medium 500',12),bg='#2c3136', fg= 'white').grid(row = 2, column = 0, pady = 10)
    nameVar = StringVar()
    nameInput = Entry(window_student, textvariable = nameVar).grid(row = 2, column = 1, padx = (20, 20), pady = 10)

    regNoLabel = Label(window_student, text = "Registration number", font=('Medium 500',12),bg='#2c3136', fg= 'white').grid(row = 3, column = 0, pady = 10)
    regNoVar = IntVar()
    regNoInput = Entry(window_student, textvariable = regNoVar).grid(row = 3, column = 1, padx = (20, 20), pady = 10)

    dobLabel = Label(window_student, text = "Date of birth (YYYY-MM-DD)", font=('Medium 500',12),bg='#2c3136', fg= 'white').grid(row = 4, column = 0, pady = 10)
    dobVar = StringVar()
    dobInput = Entry(window_student, textvariable = dobVar).grid(row = 4, column = 1, padx = (20, 20), pady = 10)

    contactLabel = Label(window_student, text = "Contact number", font=('Medium 500',12),bg='#2c3136', fg= 'white').grid(row = 5, column = 0, pady = 10)
    contactVar = IntVar()
    contactInput = Entry(window_student, textvariable = contactVar).grid(row = 5, column = 1, padx = (20, 20), pady = 10)

    gradeLabel = Label(window_student, text = "Grade", font=('Medium 500',12),bg='#2c3136', fg= 'white').grid(row = 6, column = 0, pady = 10)
    gradeVar = IntVar()
    gradeInput = Entry(window_student, textvariable = gradeVar).grid(row = 6, column = 1, pady = 10)

    sectionLabel = Label(window_student, text = "Section", font=('Medium 500',12),bg='#2c3136', fg= 'white').grid(row = 7, column = 0, pady = 10)
    sectionVar = StringVar()
    sectionInput = Entry(window_student, textvariable = sectionVar).grid(row = 7, column = 1, pady = 10)

    emailLabel = Label(window_student, text = "Enter email address", font=('Medium 500',12),bg='#2c3136', fg= 'white').grid(row = 8, column = 0, pady = 10)
    emailVar = StringVar()
    emailInput = Entry(window_student, textvariable = emailVar).grid(row = 8, column = 1, pady = 10)

    pinLabel = Label(window_student, text = "Enter 4-digit pin", font=('Medium 500',12),bg='#2c3136', fg= 'white').grid(row = 9, column = 0, padx = (20, 20), pady = 10)
    pinVar = IntVar()
    pinEntry = Entry(window_student, textvariable = pinVar).grid(row = 9, column = 1, padx = (20, 20), pady = 10)

    def submit_createUser():

        
        studentChar = Student(nameVar.get().title(), regNoVar.get(), dobVar.get(), contactVar.get(), gradeVar.get(), sectionVar.get(), pinVar.get(), emailVar.get())
        sql = "INSERT INTO students (Name, Pin, RegistrationNo, DOB, ContactNo, Grade, Section, EmailID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (studentChar.name, studentChar.pin, studentChar.regno, studentChar.dob, studentChar.contactno, studentChar.grade, studentChar.section, studentChar.emailID)
        mycursor.execute(sql, val)
        mydb.commit()
        sql = f"INSERT INTO attendance (Student) VALUES ('{studentChar.name}')"
        mycursor.execute(sql)
        mydb.commit()

            
        accountCreatedLabel = Label(window_student, text = "Account created successfully!",bg='#2c3136', fg= 'white').grid(row = 10, column = 1)

        #except Exception as e:
           # accoundNotCreatedLabel = Label(window_student, text = "Oops! Some Values Are Missing!!",bg='#2c3136', fg= 'white').grid(row = 10, column = 1)
            #print(e)

    submitButton = Button(window_student,image=submitphoto, text = "SUBMIT",compound = RIGHT, font=('Medium 500',12,'bold'),bg='light green',border=0, fg= 'black', command = submit_createUser).grid(row = 10, column = 0, pady = 40)
    copyrightLabel = Label(window_student, text = "Copyright © All Rights Reserved ",font=('Rubik-Regular',10),bg='#2c3436', fg= 'white').grid(column = 2, row = 11,pady=0,padx=1)

def login():

    root.wm_state('iconic')
    window2 = Toplevel()
    window2.title("Login")
    window2.geometry("1000x600")
    window2.configure(bg = "#2c3136")
    window2.resizable(False, False)

    createUserLabel = Label(window2,image = lmsphoto ,text = "LMS LOGIN",compound = LEFT ,bg='#2c3136', fg= 'white', font=("Semi-bold 600", 24)).grid(row = 0, column = 2, padx = 0, pady = 20)

    RadioValue = StringVar()
    teacherRadio = Radiobutton(window2,image=teacherphoto,text = "TEACHER",compound=LEFT, value = "Teacher", font = ('Rubik-Regular', 12), indicator = 0, background = "light green",fg= 'black', variable = RadioValue).grid(row = 1, column = 0, padx = (10,10), pady = 10)
    studentRadio = Radiobutton(window2,image=studentphoto,text = "STUDENT",compound=LEFT, value = "Student", font = ('Rubik-Regular', 12), indicator = 0, background = "light green",fg= 'black', variable = RadioValue).grid(row = 1, column = 1, padx = (10,10), pady = 20)

    regNoLabel = Label(window2, text = "Enter your registration number",bg='#2c3136', fg= 'white', font = ('Rubik-Regular', 12)).grid(row = 2, column = 0)
    global regNoVar
    regNoVar = IntVar()
    nameInput = Entry(window2, textvariable = regNoVar).grid(row = 2, column = 1, padx = 20, pady = 40)

    pinLabel = Label(window2, text = "Enter Password ",bg='#2c3136', fg= 'white', font = ('Rubik-Regular', 12)).grid(row = 3, column = 0, padx = (20, 20), pady = 20)
    pinVar = IntVar()
    pinEntry = Entry(window2, textvariable = pinVar).grid(row = 3, column = 1, padx = 20, pady = 20)

    def submit_login():

        try:
            mycursor.execute(f"select Pin from {RadioValue.get()}s where RegistrationNo = '{regNoVar.get()}'")
            actual_pin = mycursor.fetchall()

            if pinVar.get() == actual_pin[0][0]:
                if RadioValue.get() == "Teacher":
                    teacher()
                    window2.destroy()
                elif RadioValue.get() == "Student":
                    student()
                    window2.destroy()
            else:
                wrongPinLabel = Label(window2, text = "Wrong pin entered",bg='#2c3136', fg= 'white',font=('Medium 500',11,'bold')).grid(row = 4, column = 3)

        except Exception as e:
            errorLabel = Label(window2, text = "Oops! Some data are missing.",bg='#2c3136', fg= 'white',font=('Medium 500',11,'bold')).grid(row = 4, column = 3)
            print(e)

    loginButton = Button(window2, image = loginkeyphoto ,text = "LOGIN",compound = LEFT,padx = 12, pady = 6, borderwidth = 1,  font=('Medium 500',12,'bold'),bg='light green', fg= 'black',command = submit_login).grid(row = 4, column = 0 ,pady=60)
    forgetpass = Button(window2, text = "Forgot password?",padx = 12, pady = 6,border =0,  font=('Medium 500',11,'bold'),bg='#2c3436', fg= 'white',command = forget_pssword).grid(row = 4, column = 1 ,pady=60)
    copyrightLabel = Label(window2, text = "Copyright © All Rights Reserved ",font=('Rubik-Regular',10),bg='#2c3436', fg= 'white').grid(column = 2, row = 6,pady=20,padx=2)
def forget_pssword():
    window10 = Toplevel()
    window10.title("Forgot Password")
    window10.geometry("1000x600")
    window10.configure(bg='#2c3136')
    window10.resizable(False,False)
    
    
    def exitforgetwindow():
        window10.destroy()


    welcomeLabel = Label(window10, text = "FORGOT PASSWORD?", font=("Medium 500", 24), fg = "white",bg='#2c3136').grid(row = 0, column = 1, padx =0, pady = (40, 0))
    exitforgot = Button(window10, image = exitphoto, text = "exit",compound = LEFT,border=0, font=("Medium 500", 16), fg = "white",bg='#2c3136',command=exitforgetwindow).grid(row = 0, column = 3, padx =230, pady = (40, 0))
    RadioValue = StringVar()
    teacherRadio = Radiobutton(window10,image=teacherphoto,text = "TEACHER",compound=LEFT, value = "Teacher", font = ('Rubik-Regular', 12), indicator = 0, background = "light green",fg= 'black', variable = RadioValue).grid(row = 1, column = 0, padx = (10,10), pady = 10)
    studentRadio = Radiobutton(window10,image=studentphoto,text = "STUDENT",compound=LEFT, value = "Student", font = ('Rubik-Regular', 12), indicator = 0, background = "light green",fg= 'black', variable = RadioValue).grid(row = 1, column = 1, padx = (10,10), pady = 20)
    regNoLabel = Label(window10, text = "Enter your registration number",bg='#2c3136', fg= 'white', font = ('Rubik-Regular', 12)).grid(row = 2, column = 0,padx=20)
    global regNoVar
    regNoVar = IntVar()
    nameInput = Entry(window10, textvariable = regNoVar).grid(row = 2, column = 1, padx = 0, pady = 40)
    regNoLabel = Label(window10, text = "Enter your email id",bg='#2c3136', fg= 'white', font = ('Rubik-Regular', 12)).grid(row = 3, column = 0)
    global emailNoVar
    emailNoVar = StringVar()
    nameInput = Entry(window10, textvariable = emailNoVar).grid(row = 3, column = 1, padx = 0, pady = 40)
    def submit_details():

        try:
            mycursor.execute(f"select Pin from {RadioValue.get()}s where RegistrationNo = '{regNoVar.get()}'and emailID = '{emailNoVar.get()}'")
            actual_pin = mycursor.fetchall()
            pin = f"YOUR PASSWORD FOR LMS IS {actual_pin[0][0]}"
            to=emailNoVar.get()
            
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.ehlo()
            server.starttls()
            server.login('learningmanagements@gmail.com','wfvjplrkufnowotl')
            server.sendmail('learningmanagements@gmail.com',to,pin)
            server.close()
            pin= Label(window10, text = f'YOUR PASSWORD IS HAS BEEN SENT TO YOUR REGISTERED EMAIL ID.',bg='#2c3136', fg= 'white', font = ('Rubik-Regular', 12)).grid(row = 4, column =1 )
   
        except Exception as e:
            errorLabel = Label(window10, text = "Oops! Some data are missing.",bg='#2c3136', fg= 'white',font=('Medium 500',11,'bold')).grid(row = 4, column = 1)
            print(e)
    SubButton = Button(window10,text = "SUBMIT",padx = 12, pady = 6, borderwidth = 1,  font=('Medium 500',12,'bold'),bg='light green', fg= 'black',command = submit_details).grid(row = 4, column = 0 ,pady=60)
    copyrightLabel = Label(window10, text = "Copyright © All Rights Reserved ",font=('Rubik-Regular',10),bg='#2c3436', fg= 'white').grid(column = 1, row = 6,pady=20,padx=2)

def teacher():

    window3 = Toplevel()
    window3.title("Home Page")
    window3.geometry("1000x600")
    window3.configure(bg='#2c3136')
   
    window3.resizable(False, False)

    def quit():
        window3.destroy()

    sql = f"SELECT Name FROM teachers WHERE RegistrationNo = {regNoVar.get()}"
    mycursor.execute(sql)
    teacher_name = mycursor.fetchall()
    

    def info():
        window5=Toplevel()
        window5.title("Teacher's info")
        window5.geometry("400x600")
        window5.configure(bg='#2c3136')

        def quitinfo():
            window5.destroy()

        sql = f"SELECT Name FROM teachers WHERE RegistrationNo = {regNoVar.get()}"
        mycursor.execute(sql)
        teacher_name = mycursor.fetchall()
        sql = f"SELECT Subject FROM teachers WHERE RegistrationNo = {regNoVar.get()}"
        mycursor.execute(sql)
        sub = mycursor.fetchall()
        sql = f"SELECT DOB FROM teachers WHERE RegistrationNo ={regNoVar.get()}"
        mycursor.execute(sql)
        DOB =mycursor.fetchall()
        sql=f"SELECT emailID FROM teachers WHERE RegistrationNo ={regNoVar.get()}"
        mycursor.execute(sql)
        email =mycursor.fetchall()
        sql=f"SELECT ContactNo FROM teachers WHERE RegistrationNo ={regNoVar.get()}"
        mycursor.execute(sql)
        contact =mycursor.fetchall()
        
        infoid= Label(window5, text ="PERSONAL INFO ",font=('Medium 500',18,'bold'),bg='#2c3136', fg= 'white').grid(row = 0, column = 2,padx=90,pady=20)
        infoid1= Button(window5,image = infophoto,bg='#2c3136',border = 0 ,command=quitinfo).grid(row = 1, column = 2,padx=10,pady=30)
        regno= Label(window5, text =f"REGISTRATION NUMBER : {regNoVar.get()}",font=('Medium 500',10),bg='#2c3136', fg= 'white',justify = LEFT).grid(row = 2, column = 2,padx=10,pady=10)
        name= Label(window5, text =f"NAME : {teacher_name[0][0]}",font=('Medium 500',10),bg='#2c3136', fg= 'white',justify = LEFT).grid(row = 3, column = 2,padx=8,pady=10)
        subject= Label(window5, text =f" SUBJECT :{sub[0][0]}",font=('Medium 500',10),bg='#2c3136', fg= 'white',justify = LEFT).grid(row = 4, column = 2,padx=2,pady=10)
        contactid= Label(window5, text =f"CONTACT NUMBER : {contact[0][0]}",font=('Medium 500',10),bg='#2c3136', fg= 'white',justify = LEFT).grid(row = 5, column = 2,padx=10,pady=10)
        date= Label(window5, text = f" DATE OF BIRTH : {DOB[0][0]}",font=('Medium 500',10),bg='#2c3136', fg= 'white',justify = LEFT).grid(row = 6, column = 2,padx=10,pady=10)
        gmail= Label(window5, text =f"EMAIL ID :{email[0][0]}",font=('Medium 500',10),bg='#2c3136', fg= 'white',justify = LEFT).grid(row = 7, column = 2,padx=10,pady=10)
        copyrightLabel = Label(window5, text = "Copyright © All Rights Reserved ",font=('Rubik-Regular',10),bg='#2c3436', fg= 'white').grid(column = 2, row = 9,pady=10,padx=2)

    welcomeLabel = Label(window3, text = "  TEACHER's LMS DASHBOARD", font=("Medium 500", 24), fg = "white",bg='#2c3136').grid(row = 0, column = 1, padx = 48, pady = (40, 0))
    teacherlabel=Button(window3 , image= logophoto ,text = f"{teacher_name[0][0]} ",border=0,compound = LEFT,font=("Rubik-Regular", 13,'bold'), fg = 'white',bg='#2c3136',command=info).grid(row = 0, column = 0, padx = 10, pady = (40, 0))
    logoutButton = Button(window3, image = logoutphoto ,text = "LOG OUT",border = 0 ,compound = RIGHT,  font=('Medium 500',10,'bold'),fg = 'white',bg="#2c3136",command = quit).grid(row = 0, column = 2,pady=(40,0))
        
    def live_class():

        liveclassframe = Frame(window3,bg='#3f4a54')
        liveclassframe.grid(row = 1, column = 0)
    
        linkLabel = Label(liveclassframe, text = "Enter live class link:" ,font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = 0, column = 0)
        linkValue = StringVar()
        linkInput = Entry(liveclassframe, textvariable = linkValue).grid(row = 0, column = 1, padx = 5)
        

        

        def submit_link():

            sql = "DELETE FROM LiveClassLink"
            mycursor.execute(sql)
            mydb.commit()

            sql = f"INSERT INTO LiveClassLink VALUES ('{linkValue.get()}')"
            mycursor.execute(sql)
            mydb.commit()
            linkUploadSuccessfulLabel = Label(liveclassframe, text = "Link uploaded successfully").grid(row = 1, column = 0)

        def quit():

            liveclassframe.grid_forget()
            liveclassframe.destroy()

        linkSubmitButton = Button(liveclassframe, text = "SUBMIT",font=('Medium 500',12,'bold'),bg='LIGHT GREEN', fg= 'black', command = submit_link).grid(row = 2, column = 1, pady = 30)
        quitButton = Button(liveclassframe, text = "QUIT",font=('Medium 500',12,'bold'),bg='LIGHT GREEN', fg= 'black', command = quit).grid(row = 2, column = 0, pady = 30, padx = 10)


    def check_attendance():

        window_attendance = Toplevel()
        window_attendance.title("Attendance")
        window_attendance.geometry("1000x600")
        window_attendance.configure(bg = "#1c1f22")
        window_attendance.resizable(False, False)

        sql = "SELECT * FROM attendance ORDER BY Student ASC"
        mycursor.execute(sql)
        result = mycursor.fetchall()

        for i in range(len(result)):

            studLabel = Label(window_attendance, text = result[i][0],font=('Medium 500',15),bg='#3f4a54', fg= 'white').grid(row = 0, column = i)

            fig = matplotlib.figure.Figure(figsize=(2,2), facecolor='#1c1f22')
            ax = fig.add_subplot(111)

            school_start = datetime.datetime(2020, 3, 1)
            now = datetime.datetime.now()
            time_difference = now - school_start
            days_passed = time_difference.days
            present = result[i][1]
            absent = days_passed - result[i][1]

            ax.pie([present, absent])
            ax.legend([f"Present: {present}", f"Absent: {absent}"])

            circle=matplotlib.patches.Circle( (0,0), 0.7, color='#1c1f22')
            ax.add_artist(circle)

            canvas = FigureCanvasTkAgg(fig, master=window_attendance)
            canvas.get_tk_widget().grid(row = 1, column = i)
            canvas.draw()

    def assignment():

        assignmentframe = Frame(window3,bg='#3f4a54')
        assignmentframe.grid(row = 2, column = 0)

        chapterLabel = Label(assignmentframe, text = "Chapter name",font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = 0, column = 0, pady = 20)
        chapterValue = StringVar()
        chapterInput = Entry(assignmentframe, textvariable = chapterValue).grid(row = 0, column = 1, pady = 20, padx = 5)

        topicLabel = Label(assignmentframe, text = "Topic",font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = 1, column = 0, pady = 20)
        topicValue = StringVar()
        topicInput = Entry(assignmentframe, textvariable = topicValue).grid(row = 1, column = 1, pady = 20, padx = 5)

        lastDateLabel = Label(assignmentframe, text = "Last date of submission (YYYY-MM-DD)",font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = 2, column = 0, pady = 20)
        lastDateValue = StringVar()
        lastDateInput = Entry(assignmentframe, textvariable = lastDateValue).grid(row = 2, column = 1, padx = 5, pady = 20)

        def choose_file():

            filename = filedialog.askopenfilename(initialdir = "*", title = "Select a file", filetypes = (("pdf files", "*.pdf"), ("text files", "*.txt")))

            sql = f"SELECT Subject FROM teachers WHERE RegistrationNo = {regNoVar.get()}"
            mycursor.execute(sql)
            result = mycursor.fetchall()

            sql = f"INSERT INTO assignments (Subject, Chapter, Topic, Link, LastDate) VALUES ('{result[0][0]}', '{chapterValue.get()}', '{topicValue.get()}', '{filename}', '{lastDateValue.get()}')"
            mycursor.execute(sql)
            mydb.commit()

            assignmentUploadSuccessful = Label(assignmentframe, text = "Assignment uploaded successfully,Please no more uploads for today!" ,font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = 5, column = 0)

        def quit():

            assignmentframe.grid_forget()
            assignmentframe.destroy()

        chooseFileButton = Button(assignmentframe,image = choosephoto ,text = "CHOOSE FILE", compound = LEFT,font=('Medium 500',12,'bold'),bg='LIGHT GREEN', fg= 'black', command = choose_file).grid(row = 3, column = 1, pady = 20)
        quitButton = Button(assignmentframe, text = "QUIT",font=('Medium 500',12,'bold'),bg='LIGHT GREEN', fg= 'black', command = quit).grid(row = 3, column = 0, pady = 20, padx = 10)


    def class_notes():

        notesframe = Frame(window3,bg='#3f4a54')
        notesframe.grid(row = 2, column = 1)

        chapterLabel = Label(notesframe, text = "Chapter name",font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = 0, column = 0, pady = 20)
        chapterValue = StringVar()
        chapterInput = Entry(notesframe, textvariable = chapterValue).grid(row = 0, column = 1, pady = 20, padx = 5)

        classNoLabel = Label(notesframe, text = "Class number",font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = 1, column = 0, pady = 20)
        classNoValue = IntVar()
        classNoInput = Entry(notesframe, textvariable = classNoValue).grid(row = 1, column = 1, pady = 20, padx = 5)

        def choose_file():

            filename = filedialog.askopenfilename(initialdir = "*", title = "Select a file", filetypes = (("pdf files", "*.pdf"), ("text files", "*.txt")))

            sql = f"SELECT Subject FROM teachers WHERE RegistrationNo = {regNoVar.get()}"
            mycursor.execute(sql)
            result = mycursor.fetchall()

            sql = f"INSERT INTO {result[0][0]} (Chapter, ClassNumber, Notes) VALUES ('{chapterValue.get()}', {classNoValue.get()}, '{filename}')"
            mycursor.execute(sql)
            mydb.commit()

            classNotesUploadSuccessful = Label(notesframe, text = "Notes uploaded successfully.",font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = 4, column = 0)

        def quit():

            notesframe.grid_forget()
            notesframe.destroy()

        chooseFileButton = Button(notesframe,image = choosephoto, text = "CHOOSE FILE",compound = LEFT,font=('Medium 500',12,'bold'),bg='LIGHT GREEN', fg= 'black', command = choose_file).grid(row = 2, column = 1, pady = 20)
        quitButton = Button(notesframe, text = "QUIT",font=('Medium 500',12,'bold'),bg='LIGHT GREEN', fg= 'black', command = quit).grid(row = 2, column = 0, pady = 20, padx = 10)

    def class_recording():

        recordframe = Frame(window3,bg='#3f4a54')
        recordframe.grid(row = 2, column = 2)

        chapterLabel = Label(recordframe, text = "Chapter name",font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = 0, column = 0, pady = 20)
        chapterValue = StringVar()
        chapterInput = Entry(recordframe, textvariable = chapterValue).grid(row = 0, column = 1, pady = 20, padx = 5)

        classNoLabel = Label(recordframe, text = "Class number",font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = 1, column = 0, pady = 20)
        classNoValue = IntVar()
        classNoInput = Entry(recordframe, textvariable = classNoValue).grid(row = 1, column = 1, pady = 20, padx = 5)

        def choose_file():

            filename = filedialog.askopenfilename(initialdir = "*", title = "Select a file", filetypes = [("Mp4 files", "*.mp4")])

            sql = f"SELECT Subject FROM teachers WHERE RegistrationNo = {regNoVar.get()}"
            mycursor.execute(sql)
            result = mycursor.fetchall()
    
            sql = f"INSERT INTO {result[0][0]} (Chapter, ClassNumber, Recording) VALUES ('{chapterValue.get()}', {classNoValue.get()}, '{filename}')"
            mycursor.execute(sql)
            mydb.commit()

            classRecordingUploadSuccessful = Label(recordframe, text = "Recording uploaded successfully.",bg='#3f4a54', fg= 'white').grid(row = 3, column = 0)

        def quit():

            recordframe.grid_forget()
            recordframe.destroy()

        chooseFileButton = Button(recordframe,image = choosephoto, text = "CHOOSE FILE",compound = LEFT,font=('Medium 500',12,'bold'),bg='LIGHT GREEN', fg= 'black',command = choose_file).grid(row = 2, column = 1, padx=2,pady = 20)
        quitButton = Button(recordframe, text = "QUIT", font=('Medium 500',12,'bold'),bg='LIGHT GREEN', fg= 'black', command = quit).grid(row = 2, column = 0, pady = 20, padx = 10)


    LiveClassLinkButton = Button(window3, image = liveClassPhoto, border=0,text="LIVE CLASS",compound=TOP,font=('Medium 500',12), bg='#2c3136', fg= 'white' ,command = live_class).grid(row = 1, column = 0, padx = 30, pady = 40)   
    checkAttendanceButton = Button(window3, image = attendancePhoto,border=0,text="CHECK ATTENDANCE",compound=TOP,font=('Medium 500',12), bg='#2c3136', fg= 'white' , command = check_attendance).grid(row = 1, column = 1, padx = 30, pady = 40)
    
    newAssignmentButton = Button(window3, image = assignmentPhoto, border=0,text="+ ASSIGNMENT",compound=TOP,font=('Medium 500',12), bg='#2c3136', fg= 'white', command = assignment).grid(row = 2, column = 0, padx = 30, pady = 40)
    classNotesButton = Button(window3, image = classNotesPhoto, border=0,text="+ CLASS NOTES",compound=TOP,font=('Medium 500',12), bg='#2c3136', fg= 'white', command = class_notes).grid(row = 2, column = 1, padx = 30, pady = 40)
    classRecordingButton = Button(window3, image = classRecordingPhoto,border=0,text="+ REC. LECTURES",compound=TOP,font=('Medium 500',12), bg='#2c3136', fg= 'white', command = class_recording).grid(row = 2, column = 2, padx = 10, pady = 40)
    copyrightLabel = Label(window3, text = "Copyright © All Rights Reserved ",font=('Rubik-Regular',10),bg='#2c3436', fg= 'white').grid(column = 1, row = 12,pady=100,padx=100)

def student():

    window4 = Toplevel()
    window4.title("Home Page")
    window4.geometry("1000x600")
    window4.configure(bg="#2c3136")
    window4.resizable(False, False)

    def quit():
        window4.destroy()
     
    sql = f"SELECT Name FROM students WHERE RegistrationNo = {regNoVar.get()}"
    mycursor.execute(sql)
    student_name = mycursor.fetchall()

    def stuinfo():
        window6=Toplevel()
        window6.title("Student's info")
        window6.geometry("400x600")
        window6.configure(bg='#2c3136')
        sql = f"SELECT Name FROM students WHERE RegistrationNo = {regNoVar.get()}"
        mycursor.execute(sql)
        stud_name = mycursor.fetchall()
        def quitinfo():
            window6.destroy()
        
        sql = f"SELECT DOB FROM students WHERE RegistrationNo ={regNoVar.get()}"
        mycursor.execute(sql)
        DOB =mycursor.fetchall()
        sql=f"SELECT emailID FROM students WHERE RegistrationNo ={regNoVar.get()}"
        mycursor.execute(sql)
        email =mycursor.fetchall()
        sql=f"SELECT ContactNo FROM students WHERE RegistrationNo ={regNoVar.get()}"
        mycursor.execute(sql)
        contact =mycursor.fetchall()
        
        infoid= Label(window6, text ="PERSONAL INFO ",font=('Medium 500',18,'bold'),bg='#2c3136', fg= 'white').grid(row = 0, column = 2,padx=90,pady=20)
        infoid1= Button(window6,image = infophoto,bg='#2c3136',border=0,command=quitinfo).grid(row = 1, column = 2,padx=10,pady=30)
        regno= Label(window6, text =f"REGISTRATION NUMBER : {regNoVar.get()}",font=('Medium 500',10),bg='#2c3136', fg= 'white',justify = LEFT).grid(row = 2, column = 2,padx=10,pady=10)
        name= Label(window6, text =f"NAME : {stud_name[0][0]}",font=('Medium 500',10),bg='#2c3136', fg= 'white',justify = LEFT).grid(row = 3, column = 2,padx=8,pady=10)
        contactid= Label(window6, text =f"CONTACT NUMBER : {contact[0][0]}",font=('Medium 500',10),bg='#2c3136', fg= 'white',justify = LEFT).grid(row = 4, column = 2,padx=10,pady=10)
        date= Label(window6, text = f" DATE OF BIRTH : {DOB[0][0]}",font=('Medium 500',10),bg='#2c3136', fg= 'white',justify = LEFT).grid(row = 5, column = 2,padx=10,pady=10)
        gmail= Label(window6, text =f"EMAIL ID :{email[0][0]}",font=('Medium 500',10),bg='#2c3136', fg= 'white',justify = LEFT).grid(row = 6, column = 2,padx=10,pady=10)
        copyrightLabel = Label(window6, text = "Copyright © All Rights Reserved ",font=('Rubik-Regular',10),bg='#2c3436', fg= 'white').grid(column = 2, row = 7,pady=80,padx=2)
    
    welcomeLabel = Label(window4, text = "STUDENT's LMS DASHBOARD", font=("Medium 500", 24), fg = "white",bg='#2c3136').grid(row = 0, column = 1, padx = 90, pady = (40, 0))
    studentlabel=Button(window4 , image= logophoto1 ,text = f"{student_name[0][0]} ",border = 0,compound = LEFT,font=("Rubik-Regular", 13,'bold'), fg = 'white',bg='#2c3136',command=stuinfo).grid(row = 0, column = 0, padx = 2, pady = (40, 0))
    logoutButton = Button(window4, image = logoutphoto ,text = "LOG OUT",border = 0 ,compound = RIGHT,  font=('Medium 500',10,'bold'),fg = 'white',bg="#2c3136",command = quit).grid(row = 0, column = 2,pady=(40,0))
    def live_class():

        sql = f"SELECT Name FROM students WHERE RegistrationNo = {regNoVar.get()}"
        mycursor.execute(sql)
        studName = mycursor.fetchall()

        #sql = f"UPDATE attendance SET NoOfDaysPresent = 0 where NoOfDaysPresent is NULL"
        #mycursor.execute(sql)
        #mydb.commit()
        sql1 = f"UPDATE attendance SET NoOfDaysPresent = NoOfDaysPresent+1 where Student = '{studName[0][0]}'"
        mycursor.execute(sql1)
        mydb.commit()
     
        print("Attendance marked successfully.")

        print("Joining live class...")
        from selenium import webdriver
        chromedriver = r"H:\school_project\chromedriver.exe"
        driver = webdriver.Chrome(chromedriver)

        sql = "SELECT Link FROM LiveClassLink"
        mycursor.execute(sql)
        result = mycursor.fetchall()[0][0]
        driver.get(result)
        driver.maximize_window()
        while True:
            pass

    def check_attendance():

        window_attendance = Toplevel()
        window_attendance.title("Attendance")
        window_attendance.geometry("400x400")
        window_attendance.configure(bg = "#1c1f22")
        window_attendance.resizable(False, False)
        def quit():
            window_attendance.destroy()

        sql = f"SELECT Name FROM students WHERE RegistrationNo = {regNoVar.get()}"
        mycursor.execute(sql)
        student_name = mycursor.fetchall()

        sql = f"SELECT * FROM attendance WHERE Student = '{student_name[0][0]}'"
        mycursor.execute(sql)
        result = mycursor.fetchall()

        studLabel = Label(window_attendance, text = result[0][0],font=('Medium 500',18),bg='#1c1f22', fg= 'white').grid(row = 0, column = 1,padx=10)

        fig = matplotlib.figure.Figure(figsize=(2,2), facecolor='#1c1f22')
        ax = fig.add_subplot(111)

        school_start = datetime.datetime(2020, 3, 1)
        now = datetime.datetime.now()
        time_difference = now - school_start
        days_passed = time_difference.days
        present = result[0][1]
        absent = days_passed - present

        ax.pie([present, absent])
        ax.legend([f"Present: {present}", f"Absent: {absent}"])

        circle=matplotlib.patches.Circle( (0,0), 0.7, color='#1c1f22')
        ax.add_artist(circle)

        canvas = FigureCanvasTkAgg(fig, master=window_attendance)
        canvas.get_tk_widget().grid(row = 1, column = 1)
        backButton = Button(window_attendance, image = backphoto ,text =f" BACK",border = 0 ,compound = LEFT,  font=('Medium 500',10,'bold'),fg = 'white',bg='#1c1f22',command = quit).grid(row = 0, column = 0,padx = 20 ,pady=20)
        canvas.draw()

    def assignment():

        assignmentWindow = Toplevel()
        assignmentWindow.title("Assignments")
        assignmentWindow.geometry("1000x600")
        assignmentWindow.configure(bg='#2c3136')
        assignmentWindow.resizable(False, False)
        window4.wm_state('iconic')

        def quit():
            assignmentWindow.destroy()
       

        def open_this(address):
            os.startfile(address)

        def physics_assignments():

            sql = "SELECT * FROM assignments WHERE Subject = 'Physics'order by Chapter"
            mycursor.execute(sql)
            result = mycursor.fetchall()

            physicsframe = Frame(assignmentWindow,bg='#3f4a54')
            physicsframe.grid(row = 1, column = 1)

            chapter = Label(physicsframe, text = "Chapter",font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = 0, column = 0, padx = 20, pady = 20)
            topic = Label(physicsframe, text = "Topic", font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = 0, column = 1, padx = 20, pady = 20)
            deadline = Label(physicsframe, text = "Deadlines", font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = 0, column = 2, padx = 20, pady = 20)
            sql = " SELECT UPLOAD FROM assign_submit WHERE"
            def choose_file():

                filename = filedialog.askopenfilename(initialdir = "*", title = "Select a file", filetypes = (("pdf files", "*.pdf"), ("text files", "*.txt")))

                sql = f"SELECT Name FROM students WHERE RegistrationNo = {regNoVar.get()}"
                mycursor.execute(sql)
                studname = mycursor.fetchall()
                
               
                sql = f"INSERT INTO assign_submit (student_name,reg_no, assign_id,link) VALUES ('{studname[0][0]}',{regNoVar.get()},'{result[i][5]}', '{filename}')"
                mycursor.execute(sql)
                mydb.commit()
                sql = f"UPDATE assign_submit SET UPLOAD = 0 where UPLOAD is NULL"
                mycursor.execute(sql)
                mydb.commit()
                assignmentUploadSuccessful = Label(physicsframe, text = "Assignment uploaded successfully.",font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = len(result)+1, column = 2)

            def quit():

                physicsframe.grid_forget()
                physicsframe.destroy()


            for i in range(len(result)):

                chapterLabel = Label(physicsframe, text = f"{result[i][1]}",font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = i+1, column = 0, padx = 20, pady = 20)
                topicButton = Button(physicsframe, image = downloadphoto ,text = f"{result[i][2]}",compound = RIGHT,font=('Medium 500',12,'bold'),bg='light green', fg= 'black', command = partial(open_this, result[i][3])).grid(row = i+1, column = 1, padx = 20, pady = 20)

                today = datetime.date.today()
                duedate = result[i][4]

                if today < duedate:
                    daysleft = str(duedate - today)
                    daysleft = daysleft.split(",")
                    daysleftLabel = Label(physicsframe, text = f"{daysleft[0]}",font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = i+1, column = 2, padx = 20, pady = 20)

                elif today > duedate:
                    daysleftLabel = Label(physicsframe, text = "You missed the deadline :(",font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = i+1, column = 2, padx = 20, pady = 20)

                elif today == duedate:
                    daysleftLabel = Label(physicsframe, text = "Today",font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = i+1, column = 2, padx = 20, pady = 20)

                chooseFileButton = Button(physicsframe, image = uploadphoto, text = "UPLOAD",compound = LEFT,font=('Medium 500',12,'bold'),bg='LIGHT GREEN', fg= 'black',border=0, command = choose_file).grid(row = i+1, column = 3,padx = 20, pady = 20)

            quitbutton = Button(physicsframe, text = "QUIT", font=('Medium 500',12,'bold'),bg='LIGHT GREEN', fg= 'BLACK', border=0,command = quit).grid(row = len(result)+1, column = 0, pady = 20, padx = 10)

        def maths_assignments():

            sql = "SELECT * FROM assignments WHERE Subject = 'maths' order by Chapter"
            mycursor.execute(sql)
            result = mycursor.fetchall()

            mathsframe = Frame(assignmentWindow,bg='#3f4a54')
            mathsframe.grid(row = 1, column = 3)

            chapter = Label(mathsframe, text = "Chapter",font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = 0, column = 0, padx = 20, pady = 20)
            topic = Label(mathsframe, text = "Topic", font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = 0, column = 1, padx = 20, pady = 20)
            deadline = Label(mathsframe, text = "Due in", font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = 0, column = 2, padx = 20, pady = 20)

            def choose_file():

                filename = filedialog.askopenfilename(initialdir = "*", title = "Select a file", filetypes = (("pdf files", "*.pdf"), ("text files", "*.txt")))

                sql = f"SELECT Name FROM students WHERE RegistrationNo = {regNoVar.get()}"
                mycursor.execute(sql)
                studname = mycursor.fetchall()

                sql = f"INSERT INTO assign_submit (student_name,reg_no, assign_id,link) VALUES ('{studname[0][0]}',{regNoVar.get()},'{result[i][5]}', '{filename}')"
                mycursor.execute(sql)
                mydb.commit()
                sql = f"UPDATE assign_submit SET UPLOAD = 0 where UPLOAD is NULL"
                mycursor.execute(sql)
                mydb.commit()
                assignmentUploadSuccessful = Label(mathsframe, text = "Assignment uploaded successfully.",font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = i+1, column = 5)

            def quit():

                mathsframe.grid_forget()
                mathsframe.destroy()

            for i in range(len(result)):

                    chapterLabel = Label(mathsframe, text = f"{result[i][1]}",font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = i+1, column = 0, padx = 20, pady = 20)
                    topicButton = Button(mathsframe , image = downloadphoto,text = f"{result[i][2]}",compound = RIGHT,border=0,font=('Medium 500',12),bg='light green', fg= 'black', command = partial(open_this, result[i][3])).grid(row = i+1, column = 1, padx = 20, pady = 20)

                    today = datetime.date.today()
                    duedate = result[i][4]

                    if today < duedate:
                        daysleft = str(duedate - today)
                        daysleft = daysleft.split(",")
                        daysleftLabel = Label(mathsframe, text = f"{daysleft[0]}",font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = i+1, column = 2, padx = 20, pady = 20)

                    elif today > duedate:
                        daysleftLabel = Label(mathsframe, text = "You missed the deadline :(",font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = i+1, column = 2, padx = 20, pady = 20)

                    elif today == duedate:
                        daysleftLabel = Label(mathsframe, text = "Today",font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = i+1, column = 2, padx = 20, pady = 20)

                    
                    chooseFileButton = Button(mathsframe,  image = uploadphoto, text = "UPLOAD",compound = LEFT,border=0,font=('Medium 500',12),bg='lightgreen', fg= 'black', command = choose_file).grid(row = i+1, column = 3,padx = 20, pady = 20)

                    

            quitButton = Button(mathsframe, text = "QUIT",border=0, font=('Medium 500',12),bg='lightgreen', fg= 'black', command = quit).grid(row = len(result)+1, column = 0, pady = 20, padx = 10)

        def chemistry_assignments():

            sql = "SELECT * FROM assignments WHERE Subject = 'Chemistry' order by Chapter"
            mycursor.execute(sql)
            result = mycursor.fetchall()

            chemframe = Frame(assignmentWindow,bg='#3f4a54')
            chemframe.grid(row = 2, column = 1)

            chapter = Label(chemframe, text = "Chapter", font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = 0, column = 0, padx = 20, pady = 20)
            topic = Label(chemframe, text = "Topic", font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = 0, column = 1, padx = 20, pady = 20)
            deadline = Label(chemframe, text = "Due in", font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = 0, column = 2, padx = 20, pady = 20)

            def choose_file():

                filename = filedialog.askopenfilename(initialdir = "*", title = "Select a file", filetypes = (("pdf files", "*.pdf"), ("text files", "*.txt")))

                sql = f"SELECT Name FROM students WHERE RegistrationNo = {regNoVar.get()}"
                mycursor.execute(sql)
                studname = mycursor.fetchall()

                sql = f"INSERT INTO assign_submit (student_name,reg_no, assign_id,link) VALUES ('{studname[0][0]}',{regNoVar.get()},'{result[i][5]}', '{filename}')"
                mycursor.execute(sql)
                mydb.commit()
                sql = f"UPDATE assign_submit SET UPLOAD = 0 where UPLOAD is NULL"
                mycursor.execute(sql)
                mydb.commit()

                assignmentUploadSuccessful = Label(chemframe, text = "Assignment uploaded successfully.",font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = i+1, column = 5)

            def quit():

                chemframe.grid_forget()
                chemframe.destroy()

            for i in range(len(result)):

                    chapterLabel = Label(chemframe, text = f"{result[i][1]}",font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = i+1, column = 0, padx = 20, pady = 20)
                    topicButton = Button(chemframe, image = downloadphoto,text = f"{result[i][2]}",compound = RIGHT,border=0,font=('Medium 500',12),bg='light green', fg= 'black', command = partial(open_this, result[i][3])).grid(row = i+1, column = 1, padx = 20, pady = 20)

                    today = datetime.date.today()
                    duedate = result[i][4]

                    if today < duedate:
                        daysleft = str(duedate - today)
                        daysleft = daysleft.split(",")
                        daysleftLabel = Label(chemframe, text = f"{daysleft[0]}",font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = i+1, column = 2, padx = 20, pady = 20)

                    elif today > duedate:
                        daysleftLabel = Label(chemframe, text = "You missed the deadline :(",font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = i+1, column = 2, padx = 20, pady = 20)

                    elif today == duedate:
                        daysleftLabel = Label(chemframe, text = "Today",font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = i+1, column = 2, padx = 20, pady = 20)

                    
                    chooseFileButton = Button(chemframe, image = uploadphoto, text = "UPLOAD",compound = LEFT,border=0,font=('Medium 500',12),bg='LIGHT GREEN', fg= 'BLACK', command = choose_file).grid(row = i+1, column = 3,padx = 20, pady = 20)

                    

            quitButton = Button(chemframe, text = "QUIT",border=0, font=('Medium 500',12),bg='LIGHT GREEN', fg= 'BLACK', command = quit).grid(row = len(result)+1, column = 0, pady = 20, padx = 10)

        def cs_assignments():

            sql = "SELECT * FROM assignments WHERE Subject = 'CS' order by Chapter"
            mycursor.execute(sql)
            result = mycursor.fetchall()

            csframe = Frame(assignmentWindow,bg='#3f4a54')
            csframe.grid(row = 2, column = 3)

            chapter = Label(csframe, text = "Chapter", font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = 0, column = 0, padx = 20, pady = 20)
            topic = Label(csframe, text = "Topic",font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = 0, column = 1, padx = 20, pady = 20)
            deadline = Label(csframe, text = "Due in", font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = 0, column = 2, padx = 20, pady = 20)

            def choose_file():

                filename = filedialog.askopenfilename(initialdir = "*", title = "Select a file", filetypes = (("pdf files", "*.pdf"), ("text files", "*.txt")))

                sql = f"SELECT Name FROM students WHERE RegistrationNo = {regNoVar.get()}"
                mycursor.execute(sql)
                studname = mycursor.fetchall()

                sql = f"INSERT INTO assign_submit (student_name,reg_no, assign_id,link) VALUES ('{studname[0][0]}',{regNoVar.get()},'{result[i][5]}', '{filename}')"
                mycursor.execute(sql)
                mydb.commit()
                sql = f"UPDATE assign_submit SET UPLOAD = 0 where UPLOAD is NULL"
                mycursor.execute(sql)
                mydb.commit()

                assignmentUploadSuccessful = Label(csframe, text = "Assignment uploaded successfully.",font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = i+1, column = 5)

            def quit():

                csframe.grid_forget()
                csframe.destroy()

            for i in range(len(result)):

                    chapterLabel = Label(csframe, text = f"{result[i][1]}",font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = i+1, column = 0, padx = 20, pady = 20)
                    topicButton = Button(csframe, image = downloadphoto, text = f"{result[i][2]}",compound = RIGHT,border=0,font=('Medium 500',12),bg='LIGHT GREEN', fg= 'black', command = partial(open_this, result[i][3])).grid(row = i+1, column = 1, padx = 20, pady = 20)

                    today = datetime.date.today()
                    duedate = result[i][4]

                    if today < duedate:
                        daysleft = str(duedate - today)
                        daysleft = daysleft.split(",")
                        daysleftLabel = Label(csframe, text = f"{daysleft[0]}",font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = i+1, column = 2, padx = 20, pady = 20)

                    elif today > duedate:
                        daysleftLabel = Label(csframe, text = "You missed the deadline :(",font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = i+1, column = 2, padx = 20, pady = 20)

                    elif today == duedate:
                        daysleftLabel = Label(csframe, text = "Today",font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = i+1, column = 2, padx = 20, pady = 20)

                    
                    chooseFileButton = Button(csframe ,image = uploadphoto, text = "UPLOAD",compound = LEFT,border=0,font=('Medium 500',12),bg='light green', fg= 'black', command = choose_file).grid(row = i+1, column = 3,padx = 20, pady = 20)

                    
            quitButton = Button(csframe, text = "QUIT",font=('Medium 500',12),border=0,bg='light green', fg= 'black', command = quit).grid(row = len(result)+1, column = 0, pady = 20, padx = 10)

        ASSIGN = Label(assignmentWindow, text = "Assignment's", font=("Medium 500", 24), fg = "white",bg='#2c3136').grid(row = 0, column = 3, padx = 100, pady = 20)
        backButton = Button(assignmentWindow, image = backphoto ,text = "BACK",border = 0 ,compound = LEFT,  font=('Medium 500',10,'bold'),fg = 'white',bg="#2c3136",command = quit).grid(row = 0, column = 0,padx = 20 ,pady=20)
        physicsAssignmentButton = Button(assignmentWindow, image = physicsphoto, border =0, text="PHYSICS ASSIGNMENT",compound=TOP,font=('Medium 500',12), bg='#2c3136', fg= 'white',command = physics_assignments ).grid(row = 1, column = 1, padx = (20, 20), pady = 50)
        mathsAssignmentButton = Button(assignmentWindow, image = mathsphoto,border=0,text="MATHEMATICS ASSIGNMENT",compound=TOP,font=('Medium 500',12), bg='#2c3136', fg= 'white', command = maths_assignments).grid(row = 1, column = 3, padx = (20, 20), pady = 50)
        chemistryAssignmentButton = Button(assignmentWindow, image = chemphoto,border=0,text="CHEMISTRY ASSIGNMENT",compound=TOP,font=('Medium 500',12), bg='#2c3136', fg= 'white' ,command = chemistry_assignments).grid(row = 2, column = 1, padx = (20, 20), pady = 40)
        csAssignmentButton = Button(assignmentWindow, image = csphoto, border=0,text="COMPUTER SCIENCE ASSIGNMENT",compound=TOP,font=('Medium 500',12), bg='#2c3136', fg= 'white' , command = cs_assignments).grid(row = 2, column = 3, padx = (20, 20), pady = 40)
        copyrightLabel = Label(assignmentWindow, text = "Copyright © All Rights Reserved ",font=('Rubik-Regular',10),bg='#2c3436', fg= 'white').grid(column = 3, row = 4,pady=100,padx=100)

    def class_notes():

        window_notes = Toplevel()
        window_notes.title("Class Notes")
        window_notes.geometry("1000x600")
        window_notes.configure(bg="#2c3136")
        window4.wm_state('iconic')

        def quit():
            window_notes.destroy()

        def open_this(address):
            os.startfile(address)

        def physics_notes():

            physicsframe = Frame(window_notes,bg='#3f4a54')
            physicsframe.grid(row = 1, column = 1)

            chapter = Label(physicsframe, text = "Chapter",font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = 0, column = 0, padx = 20, pady = 20)
            classno = Label(physicsframe, text = "Class No.",font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = 0, column = 1, padx = 20, pady = 20)

            sql = "SELECT * FROM physics where Notes is not NULL;"
            mycursor.execute(sql)
            result = mycursor.fetchall()

            def quit():

                physicsframe.grid_forget()
                physicsframe.destroy()

            for i in range(len(result)):
                link = f"Class {result[i][1]}"
                global address
                address = result[i][2]
                chapterLabel = Label(physicsframe, text = result[i][0],font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = i+1, column = 0)
                noteLinkButton = Button(physicsframe, image = downloadphoto ,text = link,compound = RIGHT,font=('Medium 500',12),bg='light green', fg= 'black', command = partial(open_this, address)).grid(row = i+1, column = 1, pady = 10)
            quitbutton = Button(physicsframe, text = "QUIT", font=('Medium 500',12),bg='LIGHT GREEN', fg= 'BLACK', border=0,command = quit).grid(row = len(result)+1, column = 0, pady = 20, padx = 10)   
        def maths_notes():

            mathsframe = Frame(window_notes,bg='#3f4a54')
            mathsframe.grid(row = 1, column = 3)

            chapter = Label(mathsframe, text = "Chapter", font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = 0, column = 0, padx = 20, pady = 20)
            classno = Label(mathsframe, text = "Class No.",font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = 0, column = 1, padx = 20, pady = 20)

            sql = "SELECT * FROM maths where Notes is not NULL"
            mycursor.execute(sql)
            result = mycursor.fetchall()
            
            def quit():

                mathsframe.grid_forget()
                mathsframe.destroy()

            for i in range(len(result)):
                link = f"Class {result[i][1]}"
                global address
                address = result[i][2]
                chapterLabel = Label(mathsframe, text = result[i][0],font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = i+1, column = 0)
                noteLinkButton = Button(mathsframe, image = downloadphoto, text = link,compound = RIGHT,font=('Medium 500',12),bg='light green', fg= 'black', command = partial(open_this, address)).grid(row = i+1, column = 1, pady = 10)
            quitbutton = Button(mathsframe, text = "QUIT", font=('Medium 500',12),bg='LIGHT GREEN', fg= 'BLACK', border=0,command = quit).grid(row = len(result)+1, column = 0, pady = 20, padx = 10)
        def chemistry_notes():

            chemframe = Frame(window_notes,bg='#3f4a54')
            chemframe.grid(row = 2, column = 1)

            chapter = Label(chemframe, text = "Chapter", font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = 0, column = 0, padx = 20, pady = 20)
            classno = Label(chemframe, text = "Class No.",font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = 0, column = 1, padx = 20, pady = 20)

            sql = "SELECT * FROM chemistry where Notes is not NULL"
            mycursor.execute(sql)
            result = mycursor.fetchall()

            def quit():

                chemframe.grid_forget()
                chemframe.destroy()

            for i in range(len(result)):
                link = f"Class {result[i][1]}"
                global address
                address = result[i][2]
                chapterLabel = Label(chemframe, image = downloadphoto ,text = result[i][0],compound = RIGHT,font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = i+1, column = 0)
                noteLinkButton = Button(chemframe, text = link,font=('Medium 500',12),bg='light green', fg= 'black', command = partial(open_this, address)).grid(row = i+1, column = 1, pady = 10)
            quitbutton = Button(chemframe, text = "QUIT", font=('Medium 500',12),bg='LIGHT GREEN', fg= 'BLACK', border=0,command = quit).grid(row = len(result)+1, column = 0, pady = 20, padx = 10)
        def cs_notes():

            csframe = Frame(window_notes,bg='#3f4a54')
            csframe.grid(row = 2, column = 3, padx = (20, 20), pady = 40)

            chapter = Label(csframe, text = "Chapter", font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = 0, column = 0, padx = 20, pady = 20)
            classno = Label(csframe, text = "Class No.",font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = 0, column = 1, padx = 20, pady = 20)

            sql = "SELECT * FROM cs where Notes is not NULL"
            mycursor.execute(sql)
            result = mycursor.fetchall()

            def quit():

                csframe.grid_forget()
                csframe.destroy()


            for i in range(len(result)):
                link = f"Class {result[i][1]}"
                global address
                address = result[i][2]
                chapterLabel = Label(csframe, text = result[i][0],font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = i+1, column = 0)
                noteLinkButton = Button(csframe, image = downloadphoto, text = link,compound = RIGHT,font=('Medium 500',12),bg='light green', fg= 'black', command = partial(open_this, address)).grid(row = i+1, column = 1, pady = 10)
            quitbutton = Button(csframe, text = "QUIT", font=('Medium 500',12),bg='LIGHT GREEN', fg= 'BLACK', border=0,command = quit).grid(row = len(result)+1, column = 0, pady = 20, padx = 10)
        NOTE = Label(window_notes, text = "SUBJECT NOTES", font=("Medium 500", 24), fg = "white",bg='#2c3136').grid(row = 0, column = 3, padx = 100, pady = 20)
        backButton = Button(window_notes, image = backphoto ,text = f" BACK",border = 0 ,compound = LEFT,  font=('Medium 500',10,'bold'),fg = 'white',bg="#2c3136",command = quit).grid(row = 0, column = 0,padx = 20 ,pady=20)
        physicsnotesButton = Button(window_notes, image = physicsphoto,border=0,text="PHYSICS NOTES",compound=TOP, font=('Medium 500',12),bg='#2c3136', fg= 'white', command = physics_notes).grid(row = 1, column = 1, padx = (20, 20), pady = 50)
        mathsnotesButton = Button(window_notes, image = mathsphoto,border=0,text="MATHEMATICS NOTES",compound=TOP, font=('Medium 500',12),bg='#2c3136', fg= 'white', command = maths_notes).grid(row = 1, column = 3, padx = (20, 20), pady = 50)
        chemistrynotesButton = Button(window_notes, image = chemphoto, border=0,text="CHEMISTRY NOTES",compound=TOP, font=('Medium 500',12),bg='#2c3136', fg= 'white', command = chemistry_notes).grid(row = 2, column = 1, padx = (20, 20), pady = 40)
        csnotesButton = Button(window_notes, image = csphoto, border=0,text="COMPUTER SCIENCE NOTES",compound=TOP, font=('Medium 500',12),bg='#2c3136', fg= 'white', command = cs_notes).grid(row = 2, column = 3, padx = (20, 20), pady = 40)
        copyrightLabel = Label(window_notes, text = "Copyright © All Rights Reserved ",font=('Rubik-Regular',10),bg='#2c3436', fg= 'white').grid(column = 3, row = 4,pady=100,padx=100)
    def class_recording():

        window_recording = Toplevel()
        window_recording.title("Class Recording")
        window_recording.geometry("1000x600")
        window_recording.configure(bg="#2c3136")
        window_recording.resizable(False, False)
        window4.wm_state('iconic')

        def quit():
            window_recording()


        def open_this(address):
            os.startfile(address)

        def physics_recording():

            physicsframe = Frame(window_recording,bg='#3f4a54')
            physicsframe.grid(row = 1, column = 2)

            chapter = Label(physicsframe, text = "Chapter",font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = 0, column = 0, padx = 20, pady = 20)
            classno = Label(physicsframe, text = "Class No.", font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = 0, column = 1, padx = 20, pady = 20)

            sql = "SELECT Chapter, ClassNumber, Recording FROM physics where Recording is not NULL"
            mycursor.execute(sql)
            result = mycursor.fetchall()

            def quit():

                physicsframe.grid_forget()
                physicsframe.destroy()


            for i in range(len(result)):
                link = f"Class {result[i][1]}"
                global address
                address = result[i][2]
                chapterLabel = Label(physicsframe, text = result[i][0],font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = i+1, column = 0)
                noteLinkButton = Button(physicsframe, image = downloadphoto, text = link,compound = RIGHT,font=('Medium 500',12),bg='light green', fg= 'black', command = partial(open_this, address)).grid(row = i+1, column = 1, pady = 10)
            quitbutton = Button(physicsframe, text = "QUIT", font=('Medium 500',12),bg='LIGHT GREEN', fg= 'BLACK', border=0,command = quit).grid(row = len(result)+1, column = 0, pady = 20, padx = 10)
        def maths_recording():

            mathsframe = Frame(window_recording,bg='#3f4a54')
            mathsframe.grid(row = 1, column = 3)

            chapter = Label(mathsframe, text = "Chapter", font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = 0, column = 0, padx = 20, pady = 20)
            classno = Label(mathsframe, text = "Class No.",font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = 0, column = 1, padx = 20, pady = 20)

            sql = "SELECT Chapter, ClassNumber, Recording FROM maths where Recording is not NULL"
            mycursor.execute(sql)
            result = mycursor.fetchall()
            def quit():

                mathsframe.grid_forget()
                mathsframe.destroy()


            for i in range(len(result)):
                link = f"Class {result[i][1]}"
                global address
                address = result[i][2]
                chapterLabel = Label(mathsframe, text = result[i][0], font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = i+1, column = 0)
                noteLinkButton = Button(mathsframe, image = downloadphoto, text = link,compound = RIGHT, font=('Medium 500',12),bg='light green', fg= 'black',command = partial(open_this, address)).grid(row = i+1, column = 1, pady = 10)
            quitbutton = Button(mathsframe, text = "QUIT", font=('Medium 500',12),bg='LIGHT GREEN', fg= 'BLACK', border=0,command = quit).grid(row = len(result)+1, column = 0, pady = 20, padx = 10)
        def chemistry_recording():

            chemframe = Frame(window_recording,bg='#3f4a54')
            chemframe.grid(row = 2, column = 2)

            chapter = Label(chemframe, text = "Chapter",font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = 0, column = 0, padx = 20, pady = 20)
            classno = Label(chemframe, text = "Class No.", font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = 0, column = 1, padx = 20, pady = 20)

            sql = "SELECT Chapter, ClassNumber, Recording FROM chemistry where Recording is not NULL"
            mycursor.execute(sql)
            result = mycursor.fetchall()

            def quit():

                chemframe.grid_forget()
                chemframe.destroy()


            for i in range(len(result)):
                link = f"Class {result[i][1]}"
                global address
                address = result[i][2]
                chapterLabel = Label(chemframe, text = result[i][0],font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = i+1, column = 0)
                noteLinkButton = Button(chemframe, image = downloadphoto, text = link,compound = RIGHT,font=('Medium 500',12),bg='light green', fg= 'black', command = partial(open_this, address)).grid(row = i+1, column = 1, pady = 10)
            quitbutton = Button(chemframe, text = "QUIT", font=('Medium 500',12),bg='LIGHT GREEN', fg= 'BLACK', border=0,command = quit).grid(row = len(result)+1, column = 0, pady = 20, padx = 10)
        def cs_recording():

            csframe = Frame(window_recording,bg='#3f4a54')
            csframe.grid(row = 2, column = 3, padx = (20, 20), pady = 40)

            chapter = Label(csframe, text = "Chapter",font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = 0, column = 0, padx = 20, pady = 20)
            classno = Label(csframe, text = "Class No.",font=('Medium 500',12),bg='#3f4a54', fg= 'white').grid(row = 0, column = 1, padx = 20, pady = 20)

            sql = "SELECT Chapter, ClassNumber, Recording FROM cs where Recording is not NULL"
            mycursor.execute(sql)
            result = mycursor.fetchall()

            def quit():

                csframe.grid_forget()
                csframe.destroy()


            for i in range(len(result)):
                link = f"Class {result[i][1]}"
                global address
                address = result[i][2]
                chapterLabel = Label(csframe, text = result[i][0],font=("Medium 500", 12), fg = "white",bg='#3f4a54').grid(row = i+1, column = 0)
                noteLinkButton = Button(csframe, image = downloadphoto, text = link,compound = RIGHT,font=("Medium 500", 12), fg = "black",bg='light green', command = partial(open_this, address)).grid(row = i+1, column = 1, pady = 10)
            quitbutton = Button(csframe, text = "QUIT", font=('Medium 500',12),bg='LIGHT GREEN', fg= 'BLACK', border=0,command = quit).grid(row = len(result)+1, column = 0, pady = 20, padx = 10)

        REC = Label(window_recording, text = "Recorded Lectures", font=("Medium 500", 24), fg = "white",bg='#2c3136').grid(row = 0, column = 3, padx = 100, pady = 20)
        backButton = Button(window_recording, image = backphoto ,text =f" BACK",border = 0 ,compound = LEFT,  font=('Medium 500',10,'bold'),fg = 'white',bg="#2c3136",command = quit).grid(row = 0, column = 0,padx = 20 ,pady=20)
        physicsrecButton = Button(window_recording, image = physicsphoto,border=0,text="PHYSICS",compound=TOP, font=('Medium 500',12),bg='#2c3136', fg= 'white', command = physics_recording).grid(row = 1, column = 2, padx = 50, pady = 50)
        mathsrecButton = Button(window_recording, image = mathsphoto, border=0,text="MATHEMATICS",compound=TOP,font=('Medium 500',12),bg='#2c3136', fg= 'white', command = maths_recording).grid(row = 1, column = 3, padx = (20, 20), pady = 50)
        chemistryrecButton = Button(window_recording, image = chemphoto,border=0,text="CHEMISTRY",compound=TOP, font=('Medium 500',12),bg='#2c3136', fg= 'white', command = chemistry_recording).grid(row = 2, column = 2, padx = 50, pady = 40)
        csrecButton = Button(window_recording, image = csphoto, border=0,text="COMPUTER SCIENCE",compound=TOP,font=('Medium 500',12),bg='#2c3136', fg= 'white', command = cs_recording).grid(row = 2, column = 3, padx = (20, 20), pady = 40)
        copyrightLabel = Label(window_recording, text = "Copyright © All Rights Reserved ",font=('Rubik-Regular',10),bg='#2c3436', fg= 'white').grid(column = 3, row = 4,pady=100,padx=100)

    LiveClassLinkButton = Button(window4, image = liveClassPhoto,border=0,text="JOIN CLASS",compound=TOP,font=('Medium 500',12), bg='#2c3136', fg= 'white', command = live_class).grid(row = 1, column = 0, padx = 30, pady = 40)
    checkAttendanceButton = Button(window4, image = attendancePhoto,border=0,text="ATTENDANCE",compound=TOP,font=('Medium 500',12), bg='#2c3136', fg= 'white', command = check_attendance).grid(row = 1, column = 1, padx = 30, pady = 40)
    newAssignmentButton = Button(window4, image = assignmentPhoto,border=0,text="ASSIGNMENT",compound=TOP,font=('Medium 500',12), bg='#2c3136', fg= 'white', command = assignment).grid(row = 2, column = 0, padx = 30, pady = 40)
    classNotesButton = Button(window4, image = classNotesPhoto,border=0,text="CLASS NOTES",compound=TOP,font=('Medium 500',12), bg='#2c3136', fg= 'white', command = class_notes).grid(row = 2, column = 1, padx = 30, pady = 40)
    classRecordingButton = Button(window4, image = classRecordingPhoto,border=0,text="REC. LECTURES",compound=TOP,font=('Medium 500',12),bg='#2c3136', fg= 'white', command = class_recording).grid(row = 2, column = 2, padx = 30, pady = 40)
    copyrightLabel = Label(window4, text = "Copyright © All Rights Reserved ",font=('Rubik-Regular',10),bg='#2c3436', fg= 'white').grid(column = 1, row = 12,pady=100,padx=100)

root = Tk()
root.title("Learning Management System")
root.geometry("1000x600")
root.configure(bg="#2c3436")
root.attributes("-fullscreen", False)
root.resizable(False,False)


#---------------------------IMAGES----------------------------------------------------------------
#You need to initialise them here instead of inside the functions, otherwise they take too much time to load

liveClassPhoto = PhotoImage(file = r"Images\liveclass.png")
classNotesPhoto = PhotoImage(file = r"Images\classnotes.png")
classRecordingPhoto = PhotoImage(file = r"Images\recording.png")
assignmentPhoto = PhotoImage(file = r"Images\assignment.png")
attendancePhoto = PhotoImage(file = r"Images\attendance.png")
logophoto = PhotoImage(file = r"Images\logo.png")
logophoto1 = PhotoImage(file = r"Images\logo1.png")
teacherphoto = PhotoImage(file =r"Images\teacher.png")
studentphoto = PhotoImage(file =r"Images\student.png")
lmsphoto = PhotoImage(file =r"Images\lms.png")
loginkeyphoto = PhotoImage(file = r"Images\loginkey.png")
signupphoto = PhotoImage(file = r"Images\signup.png")
homelmsphoto = PhotoImage(file= r"Images\homelms.png")
submitphoto = PhotoImage(file = r"Images\submit.png")
physicsphoto = PhotoImage(file = r"Images\physics.png")
chemphoto = PhotoImage(file = r"Images\chemistry.png")
mathsphoto = PhotoImage(file = r"Images\maths.png")
csphoto = PhotoImage(file = r"Images\cs.png")
logoutphoto = PhotoImage(file = r"Images\logout.png")
choosephoto = PhotoImage(file = r"Images\choose file.png")
uploadphoto = PhotoImage(file = r"Images\upload.png")
downloadphoto = PhotoImage(file = r"Images\download.png")
backphoto = PhotoImage(file = r"Images\back.png")
infophoto = PhotoImage(file = r"Images\info.png")
quitphoto= PhotoImage(file = r"Images\quit.png")
exitphoto = PhotoImage(file= r"Images\exit.png")
start()

root.mainloop()
