def all_thing_is_obj(object: any) -> int:
    """
    Función que imprime el tipo de objeto y devuelve 42.

    Args:
        object: Objeto de cualquier tipo (lista, tupla,
        conjunto, diccionario, cadena, entero, etc.).

    Returns:
        int: Siempre devuelve el valor entero 42.
    """

    object_type = type(object)

    if isinstance(object, list):
        print(f"List : {object_type}")
    elif isinstance(object, tuple):
        print(f"Tuple : {object_type}")
    elif isinstance(object, set):
        print(f"Set : {object_type}")
    elif isinstance(object, dict):
        print(f"Dict : {object_type}")
    elif isinstance(object, str):
        print(f"{object} is in the kitchen: {object_type}")

    elif isinstance(object, int):
        print("Type not found")
    else:
        print("Type not found")
    return 42
