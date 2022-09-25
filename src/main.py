from os import getenv
from typing import Dict, List
from time import sleep
from dotenv import load_dotenv
from json import loads
from threading import Thread, Lock

from services import CsvWriter, getContainerIds, getContainerStats, runDockerStats, getGatewayLoadRate, getGatewayName, getGatewayDevicesConnected, memoryUsageCheck, cpuUsageCheck

# Permite a leitura do arquivo .env
load_dotenv()

# ------------------------------ Constants ----------------------------------- #
SLEEP_CSV_WRITER_THREAD = int(getenv("SLEEP_CSV_WRITER_THREAD"))
SLEEP_STATS_THREAD      = int(getenv("SLEEP_STATS_THREAD"))
IMAGE_NAME              = loads(getenv("IMAGE_NAMES"))
# ---------------------------------------------------------------------------- #

# Thread para aguar comandos do teclado e finalizar as demais.
class managerThread(Thread):
    def __init__(self):
        """ Método construtor.
        """

        Thread.__init__(self)
      
    def run(self):
        """ Método de execução da thread.
        """
        
        global is_running
        is_running = True

        input("Pressione qualquer tecla+enter para finalizar: \n")
        is_running = False
        
        print("Manager finalizado")
    
# Thread para executar o comando docker stats e atualizar a variável output.
class statsThread(Thread):
    __mgr = managerThread() 
    __mgr.start()
    running = True

    def __init__(self):
        """ Método construtor.
        """
        
        self.lock = Lock()

        Thread.__init__(self)

    def run(self):
        """ Método de execução da thread.
        """
        
        while (is_running):
            self.lock.acquire()
            
            global output
            output = runDockerStats()

            sleep(SLEEP_STATS_THREAD)
            self.lock.release()

        self.running = False
        self.__mgr.join()

        print("Manager parado")

class threadCsvWriter(Thread):
    __mgr = managerThread() 
    __mgr.start()
    running = True

    def __init__(self, file_name: str, container_id: str, gateway_index: int):
        """ Método construtor.

        Parameters
        ----------
        file_name: :class:`str`
            Nome do arquivo que será escrito.
        container_id: :class:`str`
            ID do container que será monitorado.
        """

        self.csv: CsvWriter     = CsvWriter(file_name)
        self.container_id: str  = container_id
        self.gateway_index: int = gateway_index
        
        self.lock = Lock()
        
        Thread.__init__(self)

    def run(self):
        """ Método de execução da thread.
        """

        index: int = 0
        
        while (is_running):
            index += 1

            self.lock.acquire()
            
            container_stat: Dict[str, str] = getContainerStats(output, self.container_id)
            container_load_rate: str       = getGatewayLoadRate(self.container_id)
            gateway_name: str              = getGatewayName(self.gateway_index)
            amount_connected_devices: int  = getGatewayDevicesConnected(self.container_id)
            machine_memory: str            = memoryUsageCheck()
            machine_cpu_rate: float        = cpuUsageCheck()

            self.csv.write_row(
                data = [
                    index, 
                    gateway_name,
                    container_load_rate,
                    container_stat["memory"],
                    machine_memory,
                    container_stat["cpu"], 
                    machine_cpu_rate,
                    amount_connected_devices
                ],
                debug = True
            )

            sleep(SLEEP_CSV_WRITER_THREAD)
            self.lock.release()
        
        self.running = False
        self.__mgr.join()

        print("Manager parado")

if __name__ == "__main__":    
    threads_csv_writer = {}

    container_ids: List[str] = getContainerIds(IMAGE_NAME)

    stats_thread = statsThread()
    stats_thread.start()
    
    # Tempo de espera para a primeira execução do comando docker stats.
    sleep(5)

    for index in range(len(container_ids)):
        threads_csv_writer[index] = threadCsvWriter(
            file_name     = f"gateway_{index + 1}", 
            container_id  = container_ids[index],
            gateway_index = index + 1
        )
            
        threads_csv_writer[index].start()