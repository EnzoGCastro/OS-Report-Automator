from file_utils import make_parent_path, make_lab_path, make_output_path, list_c_files_and_code
from io_utils import get_lab_info, get_student_info, get_questions
from report_generator import write_report
from pathlib import Path

def main():
	student_list = get_student_info()
	questions_list, question_num = get_questions()
	parent_string, lab_num = get_lab_info()
	
	parent_path = make_parent_path(parent_string)
	student_names_list = [student[0] for student in student_list]
	lab_path = make_lab_path(parent_path, lab_num)
	output_path = make_output_path(student_names_list, lab_num, lab_path)
	c_files_and_code = list_c_files_and_code(lab_path)
	
	write_report(output_path, questions_list, c_files_and_code, student_list)
	
	

if __name__ == "__main__":
    main()
