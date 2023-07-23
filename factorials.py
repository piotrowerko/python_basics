def factorial_recursive(input:"int", prev:"int"=0) -> "int": 
    # if isinstance(input, int) == False:
    #     raise TypeError(f"input must be an integer!")
    if input < 0:
        input = - input
    if input == 1:
        return prev
    if prev == 0:
        prev = input
    prev1 = prev * (input - 1)
    output = input-1
    return factorial_recursive(output, prev1)

def factorial_opti(input:"int") -> "int": 
    if input == 1:
        return 1
    else:
        return input * factorial_opti(input-1)
    
def factorial_sum(input:"list") -> "int": 
    if len(input) == 1:
        return input[0]
    else:
        return input[0] + factorial_sum(input[1:])

def factorial_loop(input):
    if isinstance(input, int) == False:
        raise TypeError(f"input must be an integer!")
    if input < 0:
        input = - input
    if  0 < input < 3:
        return input
    j = 1
    for i in range(1, input+1):
        j *= i
    return j

# optional types defined in inputs by annotations:
def rect_beand_index(b:[int, float], h:[int, float]) -> float: 
    return (b * h ** 2) / 6.0


def print_input(in_string):
    if isinstance(input, str) == False:
        raise TypeError(f"input must be an integer!")
    print(in_string)

def main():
    # print(factorial_recursive(5))
    # print(factorial_loop(-5))
    # print(factorial_opti(5))
    # input_list = [10, 1, 4 , 5, 6]
    # print(factorial_sum(input_list))
    print_input(2)

if __name__ == '__main__':
    main()