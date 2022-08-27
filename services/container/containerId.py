from typing import List
from sys import exit
from re import sub
from command import run

def getContainerIds(image_name: str) -> List[str]:
    """ Retorna uma lista contendo os Ids dos containers com base no nome de
    uma imagem

    Parameters
    ----------
    image_name: :class:`str`
        Nome da imagem sem a TAG.

    Returns
    -------
    container_ids: :class:`List[str]`
    """

    container_ids: List[str] = []
    
    try:
        output = run(["docker", "ps"]).output
    except:
        print("Error trying to list containers! Make sure Docker is on.")
        exit()
    else:
        # Sanitizando o retorno do comando.
        temp: str       = str(output).replace("b'", "")
        containers: str = sub(r"\s+", " " , temp)

        # Dividindo o retorno do comando pelas linhas.
        container_lines: list = containers.split("\\n")

        # Removendo a linha que contém o cabeçalho do comando.
        container_lines.pop(0)

        for container_line in container_lines:
            if(container_line.find(image_name) != -1):
                container_ids.append(container_line.split(" ")[0])

        return container_ids