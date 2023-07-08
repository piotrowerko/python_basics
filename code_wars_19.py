def disemvowel(string_):
    vowels = ('a' , 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    string_list = list(string_)
    for i, el in enumerate(string_):
        if el in vowels:
            string_list[i] = ''
    # my_new_string = string_.replace('a' , 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U').replace("")
    return ''.join(string_list)


def disemvowel2(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s

def disemvowel3(string):
    return "".join(c for c in string if c.lower() not in "aeiou")

def main():
    print(disemvowel("This website is for losers LOL!"))


if __name__ == '__main__':
    main()