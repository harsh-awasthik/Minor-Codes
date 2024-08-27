from random import *

def main():
    n = get_digits_of_password()
    password = ""

    while True:
        ls = []
        password = ""

        for _ in range(n):
            ls.append(randrange(33, 127))
        
        if verify_password(ls):
            break
    
    for i in ls:
        password += chr(i)

    print("Your Pasword is:", password)


def verify_password(ls):
    symbols = False
    #ascii values for symbols in {~`!@#$%^&*()_-+={[}]|\:;"'<,>.?/"}
    symbols_ascii_list = [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47,
                            58, 59, 60, 61, 62, 63, 64, 91, 92, 93, 94, 95, 96, 123, 124, 
                            125, 126]
    
    Uppercase = False
    Uppercase_ascii_list = list(range(65, 91))

    lowercase = False
    lowercase_ascii_list = list(range(97, 123))

    Numeric = False
    Numeric_list = list(range(48,58))

    for i in ls:
        if i in symbols_ascii_list:
            symbols = True

        elif i in Uppercase_ascii_list:
            Uppercase = True
        
        elif i in lowercase_ascii_list:
            lowercase = True

        elif i in Numeric_list:
            Numeric = True

        if symbols and Uppercase and lowercase and Numeric:
            return True
    
    return False


def get_digits_of_password():
    n = 0
    while n < 4:
        try:
            n = int(input("Enter the Number of Password Characters(min 4). "))
        except ValueError:
            print("😕 ValueError\n")
            continue
        if n < 4:
            print("😕 There is no password of less than 4 digits.\n")

    return n


if __name__ == "__main__":
    main()