import datetime
import time
import shutil

def copy_files(source, destination):
    try:
        shutil.copy2(source, destination)
        print(f"Arquivo {source} copiado para {destination}")
        with open("log.txt", "a") as log_file:
            log_file.write(f"{source} copiado para {destination}\n")
    except FileNotFoundError:
        print(f"Arquivo {source} não encontrado.")
        with open("log.txt", "a") as log_file:
            log_file.write(f"Arquivo {source} não encontrado\n")
    except Exception as e:
        print(f"Erro ao copiar arquivo: {str(e)}")
        with open("log.txt", "a") as log_file:
            log_file.write(f"Erro ao copiar arquivo: {str(e)}\n")

print("Script em execução...")

while True:
    current_time = datetime.datetime.now()
    print(f"Data e hora atuais: {current_time}")
    
    current_day = current_time.weekday()
    current_hour = current_time.hour
    current_minute = current_time.minute

    if current_day == 4:  # Sexta-feira
        if current_hour == 17 and current_minute >= 55 and current_minute <= 59:
            copy_files("C:\\Users\\Usuario\\Scheduler\\Liberar\\C4\\breachingcharge.json", "C:\\OmegaManager\\servers\\Wasteland\\profiles\\BreachingCharge")
        elif current_hour == 21 and current_minute >= 55 and current_minute <= 59:
            copy_files("C:\\Users\\Usuario\\Scheduler\\Bloquear\\C4\\breachingcharge.json", "C:\\OmegaManager\\servers\\Wasteland\\profiles\\BreachingCharge")
    elif current_day == 5:  # Sábado
        if current_hour == 17 and current_minute >= 55 and current_minute <= 59:
            copy_files("C:\\Users\\Usuario\\Scheduler\\Liberar\\C4\\breachingcharge.json", "C:\\OmegaManager\\servers\\Wasteland\\profiles\\BreachingCharge")
        elif current_hour == 21 and current_minute >= 55 and current_minute <= 59:
            copy_files("C:\\Users\\Usuario\\Scheduler\Bloquear\C4\\breachingcharge.json", "C:\\OmegaManager\\servers\\Wasteland\\profiles\\BreachingCharge")

    if current_day == 4:  # Sexta-feira
        if current_hour == 17 and current_minute >= 55 and current_minute <= 59:
            copy_files("C:\\Users\\Usuario\\Scheduler\\Liberar\\Codelock\\CodeLockConfig.json", "C:\\OmegaManager\\servers\\Wasteland\\profiles\\CodeLock")
        elif current_hour == 21 and current_minute >= 55 and current_minute <= 59:
            copy_files("C:\\Users\\Usuario\\Scheduler\\Bloquear\\Codelock\\CodeLockConfig.json", "C:\\OmegaManager\\servers\\Wasteland\\profiles\\CodeLock")
    elif current_day == 5:  # Sábado
        if current_hour == 17 and current_minute >= 55 and current_minute <= 59:
            copy_files("C:\\Users\\Usuario\\Scheduler\\Liberar\\Codelock\\CodeLockConfig.json", "C:\\OmegaManager\\servers\\Wasteland\\profiles\\CodeLock")
        elif current_hour == 21 and current_minute >= 55 and current_minute <= 59:
            copy_files("C:\\Users\\Usuario\\Scheduler\\Bloquear\\Codelock\\CodeLockConfig.json", "C:\\OmegaManager\\servers\\Wasteland\\profiles\\CodeLock")
            
    if current_day == 4:  # Sexta-feira
        if current_hour == 17 and current_minute >= 55 and current_minute <= 59:
            copy_files("C:\\Users\\Usuario\\Scheduler\\Liberar\\Chat\\Chat.json", "C:\\OmegaManager\\servers\\Wasteland\\profiles\\AC\\Settings")
        elif current_hour == 21 and current_minute >= 55 and current_minute <= 59:
            copy_files("C:\\Users\\Usuario\\Scheduler\\Bloquear\\Chat\\Chat.json", "C:\\OmegaManager\\servers\\Wasteland\\profiles\\AC\\Settings")
    elif current_day == 5:  # Sábado
        if current_hour == 17 and current_minute >= 55 and current_minute <= 59:
            copy_files("C:\\Users\\Usuario\\Scheduler\\Liberar\\Chat\\Chat.json", "C:\\OmegaManager\\servers\\Wasteland\\profiles\\AC\\Settings")
        elif current_hour == 21 and current_minute >= 55 and current_minute <= 59:
            copy_files("C:\\Users\\Usuario\\Scheduler\\Bloquear\\Chat\\Chat.json", "C:\\OmegaManager\\servers\\Wasteland\\profiles\\AC\\Settings")

    time.sleep(60)  # Aguarda 60 segundos antes de verificar novamente
