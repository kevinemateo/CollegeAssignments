import class_of_students
class Subject:
#initializer/constructor
	def __init__(self,subject_name):
		self.__subject_name=subject_name
		self.__classes_list=[]
		self.__sections_list=[]
	def get_subject_name(self):
		return self.__subject_name
	def get_classes_list(self):
		return self.__classes_list
	def get_sections_list(self):
		return self.__sections_list
#string representation
	def __str__(self):
		return self.__subject_name + ' ' + self.__classes_list + ' ' + self.__sections_list
#methods	
	def add_class(self,Class):
		self.__classes_list.append(Class)
	def add_class_section_numbers(self,Class):
		sec_num=Class.get_section_num()
		self.__sections_list.append(sec_num)	
	def print_classes(self):
		for Class in self.__classes_list:
			print(Class)	
	def print_class_section_numbers(self):
		for section_number in self.__sections_list:
			print(section_number)	
	def get_num_of_classes(self):
		return len(self.__classes_list)