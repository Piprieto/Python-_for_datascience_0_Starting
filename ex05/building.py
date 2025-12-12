
import sys


def num_chars(s):
    """
    The function takes a single string argument and displays the sums
    of its upper-case characters,
    lower-case, characters, punctuation characters, digits and spaces.
    """
    punctuation_chars = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    total = len(s)
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    digit = sum(1 for c in s if c.isdigit())
    space = sum(1 for c in s if c.isspace())
    punct = sum(1 for c in s if c in punctuation_chars)

    print(f"The text contains {total} charactres")
    print(f"{upper} upper-case letters")
    print(f"{lower} lower-case letters")
    print(f"{punct} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")


def main():
    try:
        if len(sys.argv) > 2:
            raise AssertionError("Only one argument is allowed.")
        elif len(sys.argv) == 2:
            input_str = sys.argv[1]
            num_chars(input_str)
        else:
            print("Please enter a string: ")
            try:
                input_str = input() + "\n"  # la func input elimina \n pero el
            except EOFError:                # ejerc indica incluirlo.
                return  # Ctrl + D → salir sin imprimir nada
            num_chars(input_str)

    except AssertionError as e:
        print(AssertionError.__name__ + ":", e)


if __name__ == "__main__":
    main()
