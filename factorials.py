# def foo(a:”int”, b:”float”=5.0)  -> ”int”


def factorial_recursive(input:"int", prev:"int"=0) -> "int": 
    if isinstance(input, int) == False:
        raise TypeError(f"input must be an integer!")
    if input < 0:
        input = - input
    if input == 1:
        return prev
    if prev == 0:
        prev = input
    prev1 = prev * (input - 1)
    output = input-1
    return factorial_recursive(output, prev1)

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


def main():
    print(factorial_recursive(-5))
    print(factorial_loop(-5))


if __name__ == '__main__':
    main()