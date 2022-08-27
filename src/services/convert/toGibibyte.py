from re import findall, search

# ------------------------------ Constants ----------------------------------- #
ROUNDING_NUMBER = 2
# ---------------------------------------------------------------------------- #

def toGibibyte(value: str) -> str:
    """ Converte um valor @iB para GiB.

    Parameters
    ----------
    value: :class:`class`
        Valor em KiB.

    Returns
    -------
    valueConverted: :class:`str`
    """

    if (value.find("GiB") != -1):
        return value

    if (value.find(".") != -1):
        # Pegando somente a parte racional da String.
        temp: float = float(findall("\d+\.\d+", value)[-1])
    else:
        # Pegando somente a parte inteira da String.
        temp:int = int(search(r'\d+', value).group())

    if (value.find("KiB") != -1): # Se o valor for dado em KiB
        valueConverted: str = f"{round(temp / 1048576, ROUNDING_NUMBER)}GiB"
    elif (value.find("MiB") != -1): # Se o valor for dado em MiB
        valueConverted: str = f"{round(temp / 1024, ROUNDING_NUMBER)}GiB"
    else:
        print("Error! not known unit measure.")
        
        return value

    return valueConverted

