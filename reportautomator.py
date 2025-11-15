from file_utils import make_parent_path, make_lab_path, make_output_path, list_c_files_and_code
from io_utils import get_lab_parent_path_str, get_lab_num, get_student_info, get_questions, save_data, load_data
from report_generator import write_report
from pathlib import Path

def main():
	
	load_result = load_data()
	
	if load_result:
		student_list = load_result["student_list"]
		student_num = load_result["student_num"]
		parent_path = load_result["parent_path"]
	else:
		#Get lab information
		student_list = get_student_info()
		parent_string = get_lab_parent_path_str()
		
	lab_num = get_lab_num()
	questions_list, question_num = get_questions()
	
	
	#Build filepaths
	if not load_result:
		parent_path = make_parent_path(parent_string)
	student_names_list = [student[0] for student in student_list]
	lab_path = make_lab_path(parent_path, lab_num)
	output_path = make_output_path(student_names_list, lab_num, lab_path)
	
	#Get c files and code
	c_files_and_code = list_c_files_and_code(lab_path)
	
	#Write the report
	write_report(output_path, questions_list, c_files_and_code, student_list)
	
	save_data(parent_path, student_list)

if __name__ == "__main__":
    main()
