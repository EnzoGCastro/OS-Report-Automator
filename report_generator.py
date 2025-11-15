def write_students(student_list, file):
	
	for student in student_list:
		file.write(f"{student[0]} - {student[1]}")
		file.write("\n")

def write_questions(question_list, file_and_code_list, file):
	for i,question in enumerate(question_list):
		file.write(f"Questao {i + 1}: {question}\n")
		for filename, code in file_and_code_list:
			if str(i+1) in filename:
				file.write(f"Arquivo C {filename}\n")
				file.write(f"{code}\n")
		file.write("Saida: \n\n")
		file.write("Comando de Compilacao: \n\n")
		file.write("Conclusao: \n\n")
		
def write_report(output_file_path, question_list, file_and_code_list, student_list):
	with open(output_file_path, "w") as f:
		write_students(student_list, f)
		
		write_questions(question_list, file_and_code_list, f)
