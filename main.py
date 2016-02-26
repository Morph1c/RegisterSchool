##
# Main del programma ProjectSchool
#

from Register import Register

def main():
	studentRegister = Register("C:\MyPrograms\RegisterSchool\database\databasesPath.txt")
	done = False
	FUNC = ["View your marks", "Add mark/s", "Remove mark"]
	print("Welcome Student this is your Register's school\n")
	while not done:
		for n, f in enumerate(FUNC, 1):
			print(n, " > ", f)
		action = input("Select an action: ")
		if action == "1":
			print("\nThis is your marks: ")
			for subjectNumber in studentRegister.subjects():
				print(
					subjectNumber, " > ", studentRegister.subjects()[subjectNumber], end= " = "
					)
				for mark in studentRegister.readSubjectMarks(subjectNumber):
					print(mark, end= "  ")
				print(" avg: ", studentRegister.average(studentRegister.readSubjectMarks(subjectNumber))) 
		elif action == "2":
			print("You're adding mark\n")
			for subjectNumber in studentRegister.subjects():
				print(subjectNumber, " > ", studentRegister.subjects()[subjectNumber])
			str_number = input("Enter a subject: ")
			try:
				number = int(str_number)
				str_mark = input("Enter a mark: ")
				try:
					mark = float(str_mark)
					studentRegister.addMark(number, mark)
					print("Added mark")
				except IndexError:
					print("Invalid number for subject")
				except ValueError:
					print("Invalid mark")
			except:
				print("Invalid argument")
		elif action == "3":
			print("You're removing mark\n")
			for subjectNumber in studentRegister.subjects():
				print(subjectNumber, " > ", studentRegister.subjects()[subjectNumber])
			str_number = input("Enter a subject: ")

			try:
				number = int(str_number)
				for mark in studentRegister.readSubjectMarks(number):
					print(mark, end=" ")
				str_mark = input("\nEnter a mark to remove: ")##
				try:
					mark = float(str_mark)
					studentRegister.removeMark(number, mark)
					print("Removed mark")
				except IndexError:
					print("Invalid number for subject")
				except ValueError:
					print("inexistent mark")
			except:
				print("Invalid argument")
		else:
			print("Invalid Action")
		done = input("\nPush 1 to exit or ENTER to reboot: ")
		if done == "":
			done = False
		else:
			done = True
		print()

# Avvio programma
if __name__ == "__main__":
	main()



