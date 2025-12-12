"""
Crearemos un programa que toma dos argumentos: un string (S) y un int (N)
cuya salida serán las palabras del string que tienen un número de letras > N
Las palabras estarán separadas por espacios, no hay caracteres especiales,
y el programa debe contener al menos una list comprehension y una
función lambda.  Si el número de argumentos no es dos o el tipo de
argumentos no es el correcto deberá indicarlo con un AssertionError
"""


import sys
from ft_filter import ft_filter


def main():
    try:
        """ Verificamos que haya exactamente 2 argumentos S y N
        assert sirve para comprobaciones: si False lanza una excepión y
        si es true continúa"""
        assert len(sys.argv) == 3, "Se requieren exactamente dos argumentos."
        input_string = sys.argv[1]
        try:
            min_length = int(sys.argv[2])
        except ValueError:
            raise AssertionError(
                "El segundo argumento debe ser un número entero."
                )

        # Verificamos que input_string y min_length sean de tipo válido
        # isinstance dará True si s es un sting o int
        # si da False con assert dará una excepción
        assert isinstance(input_string, str),  (
            "El primer argumento debe ser una cadena."
        )
        assert isinstance(min_length, int), (
            "El segundo argumento debe ser un entero."
        )
        # Filtramos palabras con list comprehension
        result = list(ft_filter(
            lambda word: len(word) > min_length, input_string.split()
            ))

        print(result)

    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
