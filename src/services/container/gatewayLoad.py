from sys import exit
from re import sub
from json import loads
from subprocess import Popen, PIPE

# ------------------------------ Constants ----------------------------------- #
MAPPING_DEVICES_FILE_PATH = "opt/servicemix/etc/br.ufba.dcc.wiser.soft_iot.gateway.mapping_devices.cfg"
LOAD_MONITOR_FILE_PATH    = "opt/servicemix/etc/soft.iot.dlt.load.monitor.cfg"
# ---------------------------------------------------------------------------- #

def getGatewayLoadRate(container_id: str) -> str:
    """ Retorna a porcentagem de carga do gateway.

    Parameters
    ----------
    container_id: :class:`str`
        ID do container.

    Returns
    -------
    :class:`str`
    """

    amount_devices_connected: int = getGatewayDevicesConnected(container_id)
    load_limit: int               = __getLoadLimit(container_id)
    load_rate: float              = (amount_devices_connected/load_limit) * 100

    return f"{round(load_rate, 2)}%"

def getGatewayDevicesConnected(container_id: str) -> int:
    """ Retorna a quantidade de dispositivos que estão conectados a um 
    determinado gateway.

    Parameters
    ----------
    container_id: :class:`str`
        ID do container.

    Returns
    -------
    :class:`int`
    """

    try:
        output: str = str(
            Popen(
                f"docker exec {container_id} cat {MAPPING_DEVICES_FILE_PATH}",
                stdout = PIPE, 
                shell  = True
            ).communicate()[0]
        )
    except:
        print("Erro ao tentar acessar os arquivos do container! Verifique se o Docker está executando.")
        exit()
    else:
        # Sanitizando o retorno do comando.
        
        try:
            temp: str = output.replace("b'", "")
            temp = temp.split("\\n")[2] # Dividindo o retorno por linhas
            temp = temp.split(" = ")[1] # Dividindo o retorno no título e JSON.
        except:
            return 0
        else:
            temp = temp.replace("\\", "") # Removendo as '\\'

            json: str = loads(temp)

            return len(json)

def __getLoadLimit(container_id: str) -> int:
    """ Retorna a quantidade máxima de dispositivos que podem se conectar ao 
    gateway sem que o mesmo fique sobrecarregado.

    Parameters
    ----------
    container_id: :class:`str`
        ID do container.

    Returns
    -------
    :class:`int`
    """

    try:
        output: str = str(
            Popen(
                f"docker exec {container_id} cat {LOAD_MONITOR_FILE_PATH}",
                stdout = PIPE, 
                shell  = True
            ).communicate()[0]
        )
    except:
        print("Erro ao tentar acessar os arquivos do container! Verifique se o Docker está executando.")
        exit()
    else:
        # Sanitizando o retorno do comando.
        temp: str = output.replace("b'", "")

        temp = temp.split("\\n")[2] # Dividindo o retorno por linhas
        temp = temp.split("=")[1] # Dividindo o retorno no título e valor.
        temp = sub(r'[^\d]', "", temp) # Removendo tudo que não for caractere numérico.

        return int(temp)