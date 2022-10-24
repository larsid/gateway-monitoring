from os import popen

def memoryUsageCheck() -> str:
    """ Retorna a utilização da memória RAM

    Returns
    -------
    used_memory: :class:`str`
    """

    (total_memory, used_memory, free_memory) = map(
        str, popen('free -h').readlines()[0].split()[1:]
    )

    return used_memory