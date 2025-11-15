from pathlib import Path

def make_parent_path(abs_path):
	return Path(abs_path)

def make_lab_path(parent_folder_path, lab_num):
	lab_folder = f"lab{lab_num}"
	lab_path = parent_folder_path/lab_folder
	
	return lab_path

def make_output_path(name_list, lab_num, lab_path):
	file_path_str = f"[INF1316 - 3WB] Lab {lab_num} - " + " ".join(name for name in name_list)
	
	return lab_path/file_path_str

def list_c_files_and_code(lab_path):
	code_list = []
	
	for c_file in sorted(lab_path.glob("lab*e*.c")):
		with open(c_file, "r") as f:
			content = f.read()
		code_list.append((c_file.name, content))
		
	return code_list
