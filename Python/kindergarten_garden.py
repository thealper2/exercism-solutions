class Garden:
    PLANT_NAMES = {
        "G": "Grass",
        "C": "Clover",
        "R": "Radishes",
        "V": "Violets",
    }

    DEFAULT_STUDENTS = [
        "Alice", "Bob", "Charlie", "David",
        "Eve", "Fred", "Ginny", "Harriet",
        "Ileana", "Joseph", "Kincaid", "Larry",
    ]
    
    def __init__(self, diagram, students=None):
        rows = diagram.split('\n')
        self.row1 = rows[0]
        self.row2 = rows[1]

        if students is None:
            self.students = self.DEFAULT_STUDENTS
        else:
            self.students = sorted(students)

    def plants(self, student_name):
        student_index = self.students.index(student_name)
        pos1 = student_index * 2
        pos2 = student_index * 2 + 1
        plant = []
        plant.append(self.PLANT_NAMES[self.row1[pos1]])
        plant.append(self.PLANT_NAMES[self.row1[pos2]])
        plant.append(self.PLANT_NAMES[self.row2[pos1]])
        plant.append(self.PLANT_NAMES[self.row2[pos2]])
        return plant
