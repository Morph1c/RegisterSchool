##
# Libreria per ProjectSchool
#

# Inizializzo la classe registro
class Register:
    ## Inizializzo la classe
    #  @param path il percorso di memorizzazione dei database
    #
    def __init__(self, path):
        self._path = path
        with open(self._path, 'r') as database_path:
            database_path = database_path.readlines()[0].rstrip().replace(" ", "").split(',')
            self._databases_path = database_path

    ## Configura la lista delle materie
    #  @return una lista contenente tutte le materie dell'alunno
    #
    def subjectsConfigurations(self):
        with open(self._databases_path[0], 'r') as subjectsFile:
            subjectsList = subjectsFile.readlines()[0].rstrip().split(',')
        return subjectsList

    ## Stampa la materie numerandole
    #  @param subjectsList la lista delle materie dell'alunno
    #
    def printSubjects(self, subjectsList):
        for number, subject in enumerate(subjectsList, 1):
            print(number, ' --> ', subject)
    
    ## Calcola la media dei voti
    #  @param numeri lista contenente i numeri per fare la media
    #  @return la media dei numeri
    #
    def average(self, numbers_list):
        total = 0.0
        for str_number in numbers_list:
            try:
                number = float(str_number)
                total = total + number
            except:
                print("Invalid Argument")
                return
        if total == 0:
            print('Non hai voti')
        return round(total / len(numbers_list), 2)

    ## Legge i voti di una materia e li stampa
    #  @param subject numero corrispondente materia
    #  @return marks_list lista contenente i voti
    #
    def readSubjectMarks(self, subject):  
        with open(self._databases_path[1], 'r') as marks_file:
            if subject == "all":
                marks_list = marks_file.readlines()
                for i, j in enumerate(marks_list):
                    marks_list[i] = j.rstrip().split(",")
            else:
                marks_list = marks_file.readlines()[subject - 1].rstrip().split(",")
        return marks_list

    ## Crea una dictioanry comprehension per numerare le materie
    #  @return subjects_dictionary comprehension di tutte le materie
    #
    def subjects(self):
        subjects_dictionary= {ch:v for ch,v in enumerate(self.subjectsConfigurations(), 1)}
        return subjects_dictionary

    ## Stampa i voti di una materia dell'alunno con la corrispondente media
    #  @param marks_list lista contenente i voti dell'alunno
    #  @param subject il numero identificativo della materia
    #
    def printSubjectMarks(self, marks_list, subject):
        print("Ecco i voti in", self.subjects()[subject])
        for mark in marks_list:
            print(mark, end=" ")
        print("\nla tua media", ":", self.average(marks_list))

    ## aggiunge un o più voti ad una materia
    #  @param subject numero della materia nel dictionary comprehension
    #  @param mark il voto/i da aggiungere
    #
    def addMark(self, subject, mark):
        all_marks_list = self.readSubjectMarks("all")
        marks_list = self.readSubjectMarks(subject)
        marks_list.extend("0")
        marks_list[len(marks_list) - 1] = str(mark)
        all_marks_list[subject - 1] = marks_list
        with open(self._databases_path[1], 'w') as marks_file:
            for row in all_marks_list:
                row = str(row).replace("'", "").replace("[", "").replace("]", "").replace(" ", "") + "\n"
                marks_file.write(row)

    ## Rimuove un voto di una materia
    #  @param subject il numero identificativo della materia
    #  @param mark il voto da rimuovere
    #
    def removeMark(self, subject, mark):
        all_marks_list = self.readSubjectMarks("all")
        marks_list = self.readSubjectMarks(subject)
        print(marks_list)
        if str(mark) in marks_list:
            marks_list.pop(marks_list.index(str(mark)))
            marks_list = ','.join(marks_list) 
            all_marks_list[subject - 1] = marks_list
            with open(self._databases_path[1], 'w') as marks_file:
                for row in all_marks_list:
                    row = str(row).replace("'", "").replace("[", "").replace("]", "").replace(" ", "") + "\n"
                    marks_file.write(row)




