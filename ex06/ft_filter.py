"""
Nos pide nuestra propia versión de la función filter y llamarla ft_filter:
Toma dos argumentos: una función y un iterable (por ejemplo, una lista).
Aplica la función a cada elemento del iterable.
Devuelve un iterable con sólo los elementos para los cuales la función
devuelve True.

La implementación debe usar "list comprehensions"
en lugar de, por ejemplo, un bucle for tradicional.
"""


def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if function is None:
        return iter([item for item in iterable if item])
    return iter([item for item in iterable if function(item)])
