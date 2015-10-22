__author__ = 'pedro'

class School(object):

    def __init__(self):
        self.streams=[]
    def add(self,stream):
        self.streams.append(stream)
    def find(self,stream):
        for room in self.streams:
            if room==stream:
                return room


class Stream(object):

    def __init__(self,stream):
        self.stream=stream
        self.students=[]
        self.teachers=[]

    def add_student(self,student):
        self.students.append(student)

    def add_teacher(self,teacher):
        self.teachers.append(teacher)

    def find_student(self,student):
        for studentt in self.students:
            if studentt.name==student:
                return studentt.name

    def find_teacher(self,teacher):
        for teacherr in self.teachers:
            if teacherr.name==teacher:
                return teacherr.name

class student(object):
    def __init__(self,name,age,parent_name):
        self.name=name
        self.age=age
        self.parent_name=parent_name

class teacher(object):
    def __init__(self,name):
        self.name=name



def register_student():
    name = raw_input("Enter student name")
    age = raw_input("Enter age")
    parent = raw_input("Enter parent name")
    studentt = student(name,age,parent)
    stream = Stream()
    stream.add_student(studentt)
    showmenue()

def register_teacher():
    name = raw_input("Enter teacher name")
    teacherr=teacher(name)
    stream = Stream()
    stream.add_teacher(teacherr)
    showmenue()

def register_stream():
    stream_name = raw_input("Enter stream name")
    stream=Stream(stream_name)
    school=School()
    school.add(stream)
    showmenue()

def showmenue():
    print "1 - Enter stream"
    print "2 - Enter student"
    print "3 - Enter teacher"
    print "4 - Find teacher"
    print "5 - Find student"
    menue = int(raw_input("Choose any number"))
    if menue==2:
        register_student()

    elif menue==3:
        register_teacher()

    elif menue==1:
        register_stream()

showmenue()