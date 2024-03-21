
from utils.decorators import performance,delay,log_call
import threading

@performance
@log_call
@delay(5)
def backup_files():
    pass


@performance
@log_call
@delay(4)
def run_antivirus():
    pass

@performance
def main():
    t1=threading.Thread(target=backup_files)
    t2=threading.Thread(target=run_antivirus)
    t1.start()
    t2.start()
    print('main finished')


if __name__ == '__main__':
    main()