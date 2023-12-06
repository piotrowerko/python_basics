import math

def poly_string(n):
    if n == 0:
        return '1'
    if n == 1:
        return 'a+b'
    if n == -1:
        return '1/(a+b)'
    answer = 'a^' + str(abs(n))
    for i in range(1, abs(n)):
        if (abs(n)-i) == 1 and i == 1:
            current_symbol = str(math.comb(abs(n), i)) + 'a' + 'b'
        elif (abs(n)-i) == 1:
            current_symbol = str(math.comb(abs(n), i)) + 'a' + 'b^' + str(i)
        elif i == 1:
            current_symbol = str(math.comb(abs(n), i)) + 'a^' + str(abs(n)-i) + 'b'
        else:
            current_symbol = str(math.comb(abs(n), i)) + 'a^' + str(abs(n)-i) + 'b^' + str(i)
        answer += '+'+ current_symbol
    answer += ('+b^' + str(abs(n)))
    if n < -1:
        answer = f'1/({answer})'
    return answer

def main():
    print(poly_string(13))

if __name__ == '__main__':
    main()import math

def poly_string(n):
    if n == 0:
        return '1'
    if n == 1:
        return 'a+b'
    if n == -1:
        return '1/(a+b)'
    answer = 'a^' + str(abs(n))
    for i in range(1, abs(n)):
        if (abs(n)-i) == 1 and i == 1:
            current_symbol = str(math.comb(abs(n), i)) + 'a' + 'b'
        elif (abs(n)-i) == 1:
            current_symbol = str(math.comb(abs(n), i)) + 'a' + 'b^' + str(i)
        elif i == 1:
            current_symbol = str(math.comb(abs(n), i)) + 'a^' + str(abs(n)-i) + 'b'
        else:
            current_symbol = str(math.comb(abs(n), i)) + 'a^' + str(abs(n)-i) + 'b^' + str(i)
        answer += '+'+ current_symbol
    answer += ('+b^' + str(abs(n)))
    if n < -1:
        answer = f'1/({answer})'
    return answer


# from math import comb

# def formula(n):
#     return ( f'1/({ formula(-n) })' if n<0 else '1' if not n else
#              '+'.join(binom(n-i,i) for i in range(n+1)) )

    
# def binom(a,b):
#     c = comb(a+b,a)
#     return f"{ c if c>1 else '' }{ term('a',a) }{ term('b',b) }"


# def term(c,n):
#     return f'{c}^{n}' if n>1 else c if n else ''

# def main():
#     print(poly_string(13))

if __name__ == '__main__':
    main()