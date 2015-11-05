__author__ = 'pedro'


class School_directory(object):
    def __init__(self):
        self.schools = []

    def add(self, school_name):
        self.schools.append(school_name)

    def find(self, name):
        for school in self.schools:
            if school.school_name == name:
                return school

    def get_school(self):
        return self.schools


class School(object):
    def __init__(self, school_name):
        self.streams = []
        self.school_name = school_name

    def add(self, stream):
        self.streams.append(stream)

    def find(self, stream_name):
        for stream in self.streams:
            if stream.name == stream_name:
                return stream

    def __repr__(self):
        return self.school_name


school_directory = School_directory()


class Stream(object):
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def find_student(self, student_name):
        for student in self.students:
            if student.name == student_name:
                return student.name

    def find_teacher(self, teacher_name):
        for teacher in self.teachers:
            if teacher.name == teacher_name:
                return teacher.name

    def get_students(self):
        return self.students


class Student(object):
    def __init__(self, name, age, parent_name):
        self.name = name
        self.age = age
        self.parent_name = parent_name

    def __repr__(self):
        return self.name


class Teacher(object):
    def __init__(self, name):
        self.name = name


def register_student():
    stream_name = raw_input("Enter the stream")
    school = raw_input("Enter name of the school")
    name = raw_input("Enter student name")
    age = raw_input("Enter age")
    parent = raw_input("Enter parent name")

    school_name = school_directory.find(school)
    student = Student(name, age, parent)
    stream = school_name.find(stream_name)
    stream.add_student(student)

    school_name = school_directory.find(school)
    stream = school_name.find(stream_name)

    print stream.get_students()

    showmenue()


def register_teacher():
    name = raw_input("Enter teacher name")
    teacher = Teacher(name)
    stream = Stream()
    stream.add_teacher(teacher)
    showmenue()


def register_stream():
    school = raw_input("Enter name of the school")
    stream_name = raw_input("Enter stream name")
    stream = Stream(stream_name)
    school_name = school_directory.find(school)
    school_name.add(stream)
    showmenue()


def register_school():
    school_name = raw_input("Enter school name")
    school = School(school_name)
    school_directory.add(school)
    print school_directory.get_school()
    showmenue()


def showmenue():

    print "1 - Enter stream"
    print "2 - Enter student"
    print "3 - Enter teacher"
    print "4 - Enter school name"
    print "5 - Find school"
    print "6 - Find teacher"
    print "7 - Find student"


    menue = int(raw_input("Choose any number"))

    if menue == 2:
        register_student()

    elif menue == 3:
        register_teacher()

    elif menue == 1:
        register_stream()

    elif menue == 4:
        register_school()


showmenue()