from psutil import cpu_percent

def cpuUsageCheck() -> float:
    """ Retorna a taxa de utilização da CPU em porcentagem.

    Returns
    -------
    cpu_usage_percentage: :class:`str`
    """

    cpu_usage_percentage: float = cpu_percent()

    return f"{cpu_usage_percentage}%"