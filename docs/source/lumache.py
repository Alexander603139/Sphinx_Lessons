def get_random_ingredients(kind=None):
    """
    Возвращает список случайных ингредиентов в виде строк.

    :param kind: "kind" необязательное значение инградиентов.
    :type kind: list[str] или None
    :raise lumache.InvalidKindError: Если kind не действительный.
    :return: Список инградиентов.
    :rtype: list[str]

    """
    return ["shells", "gorgonzola", "parsley"]

class InvalidKindError(Exception):
    """Raised if the kind is invalid."""
    pass