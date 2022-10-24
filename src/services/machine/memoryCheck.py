from os import popen

def memoryUsageCheck() -> str:
    """ Retorna a utilização da memória RAM

    Returns
    -------
    used_memory: :class:`str`
    """

    (total_memory, used_memory, free_memory) = map(
        str, popen('free -h').readlines()[1].split()[1:4]
    )

    return used_memory