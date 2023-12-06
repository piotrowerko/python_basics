# https://www.codewars.com/kata/586560a639c5ab3a260000f3/train/python

def rotate(str_):
    if str_ == '':
        return []
    out_array = []
    for i, el in enumerate(str_):
        str_ = str_[1:] + str_[0]
        out_array.append(str_)
    return out_array

def rotate2(str):
    l = []
    for i in str:
        str = str[1:] + str[0]
        l.append(str)
    return l

def main():
    print(rotate("Hello"))

if __name__ == '__main__':
    main()