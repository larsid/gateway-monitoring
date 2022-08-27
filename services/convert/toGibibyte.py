from re import findall

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

    # Pegando somente a parte racional da String.
    temp: int = float(findall("\d+\.\d+", value)[-1])

    if (value.find("KiB") != -1): # Se o valor for dado em KiB
        valueConverted: str = f"{round(temp / 1048576, ROUNDING_NUMBER)}GiB"
    elif (value.find("MiB") != -1): # Se o valor for dado em MiB
        print(f"A {temp}")
        valueConverted: str = f"{round(temp / 1024, ROUNDING_NUMBER)}GiB"

    return valueConverted

