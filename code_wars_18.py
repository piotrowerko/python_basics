def str_count(strng, letter):
    no_of_occ = 0
    for i in strng:
        if letter == i:
            no_of_occ += 1
    return no_of_occ

def str_count2(strng, letter):
    return strng.count(letter)

def str_count3(strng, letter):
    return len([i for i in strng if i == letter])

def main():
    print(str_count3("Hello", 'o'))
    print(str_count3("", 'z'))

if __name__ == '__main__':
    main()