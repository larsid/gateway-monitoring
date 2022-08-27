from os import getenv
from typing import Dict, List
from time import sleep
from dotenv import load_dotenv
from json import loads

from services import CsvWriter, getContainerIds, getContainerStats

# Permite a leitura do arquivo .env
load_dotenv()

# ------------------------------ Constants ----------------------------------- #
SLEEP_TIME_IN_SECONDS = int(getenv("SLEEP_TIME_IN_SECONDS"))
IMAGE_NAME            = loads(getenv("IMAGE_NAMES"))
# ---------------------------------------------------------------------------- #

if __name__ == "__main__":
    csv: CsvWriter = CsvWriter()

    index: int = 0

    while(True):
        index += 1

        container_stat: Dict[str, str] = {}
        container_ids: List[str] = getContainerIds(IMAGE_NAME)

        for container_id in container_ids:
            container_stat = getContainerStats(container_id)

        csv.write_row(
            data  = [index, container_stat["cpu"], container_stat["memory"]],
            debug = True
        )
        
        sleep(SLEEP_TIME_IN_SECONDS)