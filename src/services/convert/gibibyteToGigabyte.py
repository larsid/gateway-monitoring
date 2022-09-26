from re import findall, search

# ------------------------------ Constants ----------------------------------- #
ROUNDING_NUMBER = 2
# ---------------------------------------------------------------------------- #

def gibibyteToGigabyte(value: str) -> str:
    """ Converte um valor em Gibibyte para Gigabyte.

    Parameters
    ----------
    value: :class:`str`
        Valor em Gibibyte.

    Returns
    -------
    valueConverted: :class:`str`
    """

    if (value.find(".") != -1):
        # Pegando somente a parte racional da String.
        temp: float = float(findall("\d+\.\d+", value)[-1])
    else:
        # Pegando somente a parte inteira da String.
        temp: int = int(search(r'\d+', value).group())

    valueConverted: str = f"{round(temp * 1.07374, ROUNDING_NUMBER)}Gi"

    return valueConverted
