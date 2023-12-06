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
    
    
def enum(s):
    example_string = "The quick brown fox jumps over the lazy dog"
    example_string = example_string.replace(" ","").upper()
    scores = {}
    for i in s.upper():
        if i in example_string:
            if i not in scores.keys():
                scores[i] = 1
    if len(scores) == 26:
        return print('True')
    else:
        return print('False')

import string

def is_pangram(s):
    return all(i in s.lower() for i in string.ascii_lowercase)



def is_pangram(s):
    s = s.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            return False
    return True

# https://www.codewars.com/kata/57ea70aa5500adfe8a000110/train/python
def _____fold_array(array, runs):
    folded = []
    for j in range(runs):
        if len(array) == 1:
            return array
        if j > 0:
            array = folded
            folded = []
        if len(array) == 1:
            return array
        i = 0
        for i in (range(len(array) // 2)):
            folded.append(array[i] + array[-(i+1)])
        if i+1 < (len(array) / 2) and len(array) > 2:
            folded.append(array[i+1])
    return folded


def fold_array(a, n):
    b = a[:]
    for i in range(n):
        for i in range(len(b)//2):
            b[i] += b[-i-1]
        b[:] = b[:(len(b)+1)//2]
    return(b)

# def fold_array(array, runs):
#     folded = []
#     for i in (range(len(array) // 2)):
#         folded.append(array[i] + array[-(i+1)])
#     if i+1 < (len(array) / 2) and len(array) > 2:
#         folded.append(array[i+1])
#     return folded
        


def _enum(s):
    return print(s.lower())


def main():
    # print(factorial_recursive(5))
    # print(factorial_loop(-5))
    # print(factorial_opti(5))
    # input_list = [10, 1, 4 , 5, 6]
    # print(factorial_sum(input_list))
    print(fold_array([2], 1))

if __name__ == '__main__':
    main()