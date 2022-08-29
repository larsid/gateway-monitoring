from os import getenv
from typing import Dict, List
from time import sleep
from dotenv import load_dotenv
from json import loads
from threading import Thread, Lock

from services import CsvWriter, getContainerIds, getContainerStats

# Permite a leitura do arquivo .env
load_dotenv()

# ------------------------------ Constants ----------------------------------- #
SLEEP_TIME_IN_SECONDS = int(getenv("SLEEP_TIME_IN_SECONDS"))
IMAGE_NAME            = loads(getenv("IMAGE_NAMES"))
# ---------------------------------------------------------------------------- #

class managerThread(Thread):
    def __init__(self):
        Thread.__init__(self)
      
    def run(self):
        global is_running
        is_running = True

        input("Pressione qualquer tecla+enter para finalizar: \n")
        is_running = False
        
        print("Manager finalizado")
    
class thread(Thread):
    __mgr = managerThread() 
    __mgr.start()
    running = True

    def __init__(self, file_name, container_id):
        self.csv: CsvWriter    = CsvWriter(file_name)
        self.container_id: str = container_id
        self.lock = Lock()
        
        Thread.__init__(self)

    def run(self):
        global is_running
        
        index: int = 0
        
        while (is_running):
            index += 1

            self.lock.acquire()
            container_stat: Dict[str, str] = getContainerStats(self.container_id)
            # TODO Executar o comando desse método somente uma vez, e passar seu retorno para esse método.

            self.csv.write_row(
                data  = [index, container_stat["cpu"], container_stat["memory"]],
                debug = True
            )
            
            sleep(SLEEP_TIME_IN_SECONDS)
            self.lock.release()
        
        self.running = False
        self.__mgr.join()

        print("Manager parado")

if __name__ == "__main__":    
    threads = {}

    container_ids: List[str] = getContainerIds(IMAGE_NAME)

    for index in range(len(container_ids)):
        threads[index] = thread(f"file{index}", container_ids[index])
        threads[index].start()