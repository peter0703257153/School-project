__author__ = 'pedro'
student_file_object = open("students","r")
student_file_object_write = open("zabantu","w")
#print dir(student_file_object)
#print student_file_object.read(20)
#print student_file_object.readline()
print student_file_object.readlines()[0:3]
#for x in range(3):
    #print student_file_object.readline().strip()

#print dir()
print student_file_object_write.write("peter")
#print student_file_object_write.writelines("peterrr")