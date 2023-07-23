from datetime import date

class Student():
    STATES = ("suspended", "active", "discharged", "alumnus")
    
    def __init__(self, name, last_name, age) -> None:
        self.name = name
        self.last_name = last_name
        self.age = age
        
    def __str__(self):
        return f"I am a student, my name is {self.name} {self.last_name}\
            my age is {self.age}"
    
    @classmethod
    def from_birth_year(cls, name, last_name, birth_year):
        return cls(name, last_name, date.today().year - birth_year)
    

def main():
    student_no_1 = Student.from_birth_year('Pio', "Owe", 1985)
    print(student_no_1)
    
if __name__ == '__main__':
    main()