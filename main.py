from time import sleep
from services import cpuUsageCheck, memoryUsageCheck, CsvWriter

# ------------------------------ Constants ----------------------------------- #
SLEEP_TIME_IN_SECONDS = 5
# ---------------------------------------------------------------------------- #

if __name__ == "__main__":
    csv: CsvWriter = CsvWriter()

    index: int = 0

    while(True):
        index += 1

        csv.write_row(
            data  = [index, cpuUsageCheck(), memoryUsageCheck()]
        )
        
        sleep(SLEEP_TIME_IN_SECONDS)

    