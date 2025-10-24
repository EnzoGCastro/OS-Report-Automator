def get_student_info():
	student_list = []
	student_num = int(input("Insert num of students: "))
	for i in range(student_num):
		name = input("Insert student name: ")
		matr = input("Insert student id number: ")
		student = (name,matr)
		student_list.append(student)
		
	return student_list;
	
def get_questions():
	question_num = int(input("Insert question num: "))
	question_list = []

	for i in range(question_num):
		question = input(f"Insert question {i + 1}: ")
		question_list.append(question)
		
	return (question_list, question_num)

def get_lab_info():
	lab_path_string = input("Insert absolute path to folder which contains all lab folders: ")
	lab_num = int(input("Insert lab num: "))
	
	return (lab_path_string,lab_num)
	
