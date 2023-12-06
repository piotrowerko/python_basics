#  https://stackabuse.com/unpacking-in-python-beyond-parallel-assignment/
from class_method import Student

def calc_line(**kwargs):
    x_start = kwargs['x1']
    x_end = kwargs['x2']
    try:
        color = kwargs['color']
    except KeyError:
        color = 'WHITE'
    output_line_data = {'length': x_end - x_start,
                        'color': color}
    return output_line_data




def main():
    student_no_1 = Student.from_birth_year('Pio', "Owe", 1985)
    student_no_2 = Student.from_birth_year('Rob', "Stark", 2000)
    print(student_no_1)
    print(student_no_1 + student_no_2)
    
    input_data_for__line = {'x1': 10,
                            'x2': 16,
                            'color': 'YELLOW'}
    
    my_line_out_data = calc_line(**input_data_for__line)
    print(my_line_out_data)
    
    
    
if __name__ == '__main__':
    main()