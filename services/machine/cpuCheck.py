from os import cpu_count
from psutil import getloadavg

def cpuUsageCheck(rounding_number: int = 2) -> float:
    """ Retorna a taxa de utilização da CPU em porcentagem.

    Parameters
    ----------
    rounding_number: :class:`int`
        Número máximo de casas de decimais.

    Returns
    -------
    cpu_usage_percentage: :class:`float`
    """
    
    (load1, load5, load15) = getloadavg()

    cpu_usage_percentage:float = round((load15/cpu_count()) * 100, rounding_number)

    return cpu_usage_percentage
