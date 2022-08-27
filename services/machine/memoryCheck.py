from os import popen

def memoryUsageCheck(rounding_number: int = 2) -> float:
    """ Retorna a taxa de utilização da memória RAM em porcentagem.

    Parameters
    ----------
    rounding_number: :class:`int`
        Número de máximo de casas de decimais.

    Returns
    -------
    memory_usage_percentage: :class:`float`
    """

    (total_memory, used_memory, free_memory) = map(
        int, popen('free -t -m').readlines()[-1].split()[1:]
    )

    memory_usage_percentage: float = round(
        (used_memory/total_memory) * 100, 
        rounding_number
    )

    return memory_usage_percentage