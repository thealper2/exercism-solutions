class School:
    def __init__(self):
        self.students = {}
        self.rosters = {}
        self.add_results = []

    def add_student(self, name, grade):
        if name in self.students:
            self.add_results.append(False)
            return False

        self.students[name] = grade
        if grade not in self.rosters:
            self.rosters[grade] = []

        self.rosters[grade].append(name)
        self.rosters[grade].sort()
        self.add_results.append(True)
        return True

    def roster(self):
        result = []
        for grade in sorted(self.rosters.keys()):
            result.extend(self.rosters[grade])

        return result

    def grade(self, grade_number):
        if grade_number not in self.rosters:
            return []

        return self.rosters[grade_number][:]

    def added(self):
        return self.add_results
