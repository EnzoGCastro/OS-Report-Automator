from pathlib import Path

parent_folder = Path("/home/enzogcastro/Desktop/LABS-INF1316")

lab_num = int(input("Insert lab num: "))

lab_folder = f"lab{lab_num}"

lab_path = parent_folder/lab_folder

student_num = int(input("Insert number of students in report: "))
student_list = []
for i in range(student_num):
	name = input("Insert student name: ")
	matr = input("Insert student id number: ")
	student = (name,matr)
	student_list.append(student)

file_path_str = f"[INF1316 - 3WB] Lab {lab_num} - " + ", ".join(student[0] for student in student_list)

file_path = lab_path/file_path_str



questionNum = int(input("Insert question num: "))

question_list = []

for i in range(questionNum):
	question = input(f"Insert question {i + 1}: ")
	question_list.append(question)
	


codeList = []

	

for c_file in sorted(lab_path.glob("lab*e*.c")):
	with open(c_file, "r") as f:
		content = f.read()
	codeList.append((c_file.name, content))


with open(file_path, "w") as f:
	
	for student in student_list:
		f.write(f"{student[0]} - {student[1]}")
		f.write("\n")
	
	for i,question in enumerate(question_list):
		f.write(f"Questao {i + 1}: {question_list[i]}\n")
		for filename, code in codeList:
			if str(i+1) in filename:
				f.write(f"Arquivo C {filename}\n")
				f.write(f"{code}\n")
		f.write("Saida: \n\n")
		f.write("Comando de Compilacao: \n\n")
		f.write("Conclusao: \n\n")
			 
		
		
	
	

