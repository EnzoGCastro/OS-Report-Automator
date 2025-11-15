from pathlib import Path
import json

saved_data_path = Path(__file__).parent
settings_path = saved_data_path/"report_settings.json"

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

def get_lab_parent_path_str():
	lab_path_string = input("Insert absolute path to folder which contains all lab folders: ")
	return lab_path_string

def get_lab_num():
	lab_num = int(input("Insert lab num: "))
	return lab_num

def save_data(parent_path, student_list):
	
	data = {
		"parent_path": str(parent_path),
		"student_num": len(student_list),
		"student_list": student_list
	}
	
	with open(settings_path, "w") as f:
		json.dump(data, f, indent=4)

def load_data():
	if settings_path.exists():
		with open(settings_path, "r") as f:
			data = json.load(f)
			data["parent_path"] = Path(data["parent_path"])
			return data
	return None
