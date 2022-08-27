from io import TextIOWrapper
from typing import List
from csv import writer

# ------------------------------ Constants ----------------------------------- #
HEADER    = ["Tempo", "CPU", "Memória"]
DIRECTORY = "csv-files"
# ---------------------------------------------------------------------------- #

class CsvWriter:
    def __init__(self, file_name: str = None) -> None:
        """ Método construtor

        Parameters
        ----------
        file_name: :class:`str`
            Nome do arquivo sem a extensão.
        """

        file        = self.__createFile(file_name)
        self.writer = writer(file)

        self.__write_header()

    def __createFile(self, file_name: str) -> TextIOWrapper:
        """ Cria um arquivo `.csv`.

        Parameters
        ----------
        file_name: :class:`str`
            Nome do arquivo sem a extensão.
        """
        
        if(file_name is None):
            file_name = "file1"

        try:
           file = open(f'{DIRECTORY}/{file_name}.csv', 'w')

           return file
        except:
            print(f"Error trying to create the file `{file_name}`")

    def __write_header(self) -> None:
        """ Escreve o cabeçalho no arquivo `.csv`.
        """

        self.writer.writerow(HEADER)
        
    def write_row(self, data: List, debug: bool = False):
        """ Escreve uma linha no arquivo `.csv`.

        Parameters
        ----------
        data: :class:`List`
            Lista contendo os dados que serão escritos em uma linha do arquivo.

        Returns
        -------
        :class:`bool`
        """

        try:
            if (len(data) != len(HEADER)):
                print(f"Error, the data list must be the same length as the number of header columns {len(HEADER)}")

                return False

            if (debug):
                print(f"Writing... {data}")
            
            self.writer.writerow(data)

            return True
        except:
            print("Error trying to write the data list.")
            
            return False
