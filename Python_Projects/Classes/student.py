class Student:
#initializer/constructor
	def __init__(self,name,studentID,overall_score):
		self.__name=name
		self.__studentID=studentID
		self.__overall_score=overall_score
#getter/setter
	def get_name(self):
		return self.__name
	def get_studentID(self):
		return self.__studentID
	def set_overall_score(self,overall_score):
		self.__overall_score=overall_score
	def get_overall_score(self):
		return self.__overall_score
#string representation
	def __str__(self):
		return self.__name + ' ' + str(self.__studentID) + ' ' + str(self.__overall_score)