def all_thing_is_obj(object: any) -> int:
    """
    Function that prints the object type and returns 42.

    Args:

    object: Any type of object (list, tuple, set, dictionary, string, integer, etc.).

    Returns:

    int: Always returns the integer value 42.
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
