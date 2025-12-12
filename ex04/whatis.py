
import sys


def is_even(num: int) -> str:
    """
    Tomamos un número como argumento y comprobamos si es par o impar.
    Si tenemos más de un argumento o no es un entero indicaremos el error
    """
    if num % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


def main():
    try:

        if len(sys.argv) > 2:  # Más de un argumento:lanzar AssertionError
            raise AssertionError(
                "AssertionError: more than one argument is provided"
                )
        elif len(sys.argv) == 1:  # Si no hay argumentos, no hacer nada
            return
        else:
            num = int(sys.argv[1])  # convertimos a un entero
            is_even(num)
    except ValueError:
        print("AssertionError: argument is not an integer")
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
