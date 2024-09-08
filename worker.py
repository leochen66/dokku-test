import time

LOG_FILE_PATH = "/tmp/test_log"

def write_to_log():
    with open(LOG_FILE_PATH, "a") as log_file:
        log_file.write("Executing...\n")

def main():
    while True:
        write_to_log()
        time.sleep(10)  # 每 10 秒寫入一行

if __name__ == "__main__":
    main()
