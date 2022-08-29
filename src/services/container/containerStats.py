from typing import Dict, List
from sys import exit
from re import sub
from command import run

from ..convert.toGibibyte import toGibibyte

# ------------------------------ Constants ----------------------------------- #
ID_POSITION  = 0
CPU_POSITION = 2
MEM_POSITION = 3
# ---------------------------------------------------------------------------- #

def runDockerStats() -> str:
    """ Executa o comando `docker stats` e retorna a sua resposta.

    Returns
    -------
    output: :class:`str`
    """

    try:
        output = run(["docker", "stats", "--no-stream"]).output
        
        return str(output)
    except:   
        print("Erro ao tentar verificar o estado do container! Verifique se o Docker está executando.")
        exit()

def getContainerStats(output: str, container_id: str) -> Dict[str, str]:
    """ Retorna o ID, a porcentagem de utilização da CPU e a porcentagem de
    utilização da memória RAM de um container com base no ID especificado.

    Parameters
    ----------
    output: :class: `str`
        Resposta do comando `docker stats`.
    container_id: :class: `str`
        ID do container que deseja saber o estado.

    Returns
    -------
    container_stat: :class:`Dict[str, str, str]`
    """

    container_stat: Dict[str, str] = {}

    # Sanitizando o retorno do comando.
    temp: str       = output.replace("b'", "")
    containers: str = sub(r"\s+", " " , temp)

    # Dividindo o retorno do comando pelas linhas.
    container_lines: list = containers.split("\\n")

    for container_line in container_lines:
        # Procurando o container com o ID especificado.
        if(container_line.find(container_id) != -1):
            container_info: List[str] = container_line.split(" ")
            
            container_stat["id"]     = container_info[ID_POSITION]
            container_stat["cpu"]    = container_info[CPU_POSITION]
            container_stat["memory"] = toGibibyte(container_info[MEM_POSITION])
            
            return container_stat