import student, class_of_students, subject
def main():
#create students
	student1=student.Student('Kevin',40205858,100)
	student2=student.Student('Omar',1000001,80)
	student3=student.Student('Dennis',1111111,89)
	student4=student.Student('Jessica',2222222,70)
	student5=student.Student('Evelyn',333333333,99)
	#testing methods
	print('--Testing Methods for Students--')
	print(student1)
	print(student1.get_name())
	print(student1.get_studentID())
	student1.set_overall_score(100)
	print(student1.get_overall_score())
#create classes
	class1=class_of_students.ClassOfStudents('CS110',2)
	class2=class_of_students.ClassOfStudents('CS110',1)
	#testing methods and add students to the classes
	print('--Testing Methods for Classes--')
	class1.add_student(student1)
	class1.add_student(student2)
	class1.add_student(student3)
	class2.add_student(student4)
	class2.add_student(student5)
	print(class1)
	print(class2)
	print(class1.get_number_of_students())
	print(class2.get_average_score())
	class2.change_score(100)
	class2.print_student_details()
	class2.clear()
#create subject
	CS=subject.Subject('Computer Science')
	#testing methods
	print('--Testing Methods for Subject--')
	CS.add_class(class1)
	CS.add_class(class2)
	CS.add_class_section_numbers(class1)
	CS.add_class_section_numbers(class2)
	CS.print_classes()
	CS.print_class_section_numbers()
	CS.get_num_of_classes()
main()