# gateway-monitoring
Realiza o monitoramento dos gateways presentes em uma máquina e escreve em um arquivo `.csv` seperado para cada *gateway*.

Ao executá-lo em uma máquina, o programa monitora todos os containers a partir da(s) imagem/imagens que é/são definida(s) no arquivo `.env`.

## Parâmetros monitorados

- Taxa de carga do *gateway* (%);
- Quantidade de memória RAM utilizada (GiB);
- Taxa de utilização de CPU (%);
- Número de dispositivos conectados ao *gateway*;

## Como utilizar

1. Clone este repositório;
2. Instale as dependências:
   ```powershell
   pip install -r requirements.txt
   ```
   Ou
   ```powershell
   # Linux/macOS
   python3 -m pip install -r requirements.txt
   ```
3. Defina as variáveis de ambiente:
   ```powershell
   cp .env.example .env
   ```
   
### Variáveis de ambiente
- `HEADER`: Lista contendo o cabeçalho da tabela. 
   - Obs: é necessário seguir o padrão definido no arquivo `.env.example`;
- `IMAGE_NAMES`: Lista contendo o nome da(s) imagem/imagens *Docker* que se deseja monitorar;
- `SLEEP_CSV_WRITER_THREAD`: Intervalo de tempo em **segundos** que a *thread* irá escrever os dados no arquivo `.csv`;
- `SLEEP_STATS_THREAD`: Intervalo de tempo em **segundos** que a *thread* irá monitorar o *gateway*;
  - Obs: Esse valor deverá ser menor que o definido em `SLEEP_CSV_WRITER_THREAD`;
