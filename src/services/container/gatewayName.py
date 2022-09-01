from sys import exit
from subprocess import Popen, PIPE

def getGatewayName(index: int) -> str:
    """ Retorna o nome do gateway.

    Parameters
    ----------
    index: :class:`int`
        Índice da thread que está monitorando o gateway.

    Returns
    -------
    :class:`str`
    """

    try:
        output: str = str(
            Popen(
                f"hostname",
                stdout = PIPE, 
                shell  = True
            ).communicate()[0]
        )
    except:
        print("Erro ao tentar obter o hostname!")
        exit()
    else:
        # Sanitizando o retorno do comando.
        host_name: str = output.replace("b'", "").split("\\n")[0]

        gateway_name: str = f"{host_name}-{index}"

        return gateway_name
        