import student
class ClassOfStudents:
#initializer/constructor
	def __init__(self, name_of_class,section_num):
		self.__name_of_class=name_of_class
		self.__section_num=section_num
		self.__student_list=[]
#getters and setters
	def get_name_of_class(self):
		return self.__name_of_class
	def get_section_num(self):
		return self.__section_num
	def get_student_list(self):
		return self.__student_list
#string representation
	def __str__(self):
		return self.__name_of_class + ' ' + str(self.__section_num) + ' ' + str(self.__student_list)
#methods
	def add_student(self,student):
		self.__student_list.append(student)	
	def get_number_of_students(self):
		return str(len(self.__student_list))	
	def get_average_score(self):
		avg_Score=0
		for student in self.__student_list:
			avg_Score+=student.get_overall_score()
		avg_Score//=len(self.__student_list)
		return avg_Score 
	def change_score(self,score):
		for student in self.__student_list:
			setScore=student.get_overall_score()+score
			student.set_overall_score(setScore)
	def print_student_details(self):
		for student in self.__student_list:
			print(student)
	def clear(self):
		self.__student_list=[]