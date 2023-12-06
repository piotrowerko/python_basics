def plus_five(n):
    return n + 5




def main():
    res = plus_five(10)
    print(res)
    # lambda that accepts one argument
    plus_five_lambda = lambda n : n + 5
    print(type(plus_five_lambda))
    print(plus_five_lambda(10))


if __name__ == '__main__':
    main()