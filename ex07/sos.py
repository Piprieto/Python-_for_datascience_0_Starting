import sys

MORSE = {
    "A": ".- ",     "B": "-... ",   "C": "-.-. ",   "D": "-.. ",
    "E": ". ",      "F": "..-. ",   "G": "--. ",    "H": ".... ",
    "I": ".. ",     "J": ".--- ",   "K": "-.- ",    "L": ".-.. ",
    "M": "-- ",     "N": "-. ",     "O": "--- ",    "P": ".--. ",
    "Q": "--.- ",   "R": ".-. ",    "S": "... ",    "T": "- ",
    "U": "..- ",    "V": "...- ",   "W": ".-- ",    "X": "-..- ",
    "Y": "-.-- ",   "Z": "--.. ",
    "0": "----- ",  "1": ".---- ",  "2": "..--- ",  "3": "...-- ",
    "4": "....- ",  "5": "..... ",  "6": "-.... ",  "7": "--... ",
    "8": "---.. ",  "9": "----. ",
    " ": "/ "
}


def changetomorse(message):
    """Convierte una cadena a código Morse"""
    # Convertir a mayúsculas para coincidir con las claves del diccionario
    message = message.upper()
    # Validar caracteres
    for char in message:
        if char not in MORSE:
            raise ValueError(f"Character \'{char}\' is not in our MORSE.")
    # Generar salida en morse
    output = ''.join(MORSE[char] for char in message)
    return output


def main():
    try:
        assert len(sys.argv) == 2      # un solo argumento a cambiar
        message = sys.argv[1]
    except AssertionError:
        print("AssertionError: the arguments are bad")
        return  # detenemos la ejecución si hay más de 1 arg
    try:
        output = changetomorse(message)
        print(output.strip())  # eliminamos espacio extra al final
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
