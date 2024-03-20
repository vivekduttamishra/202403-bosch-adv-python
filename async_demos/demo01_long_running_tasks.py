
from utils.decorators import performance,delay,log_call

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


def main():
    backup_files()
    run_antivirus()


if __name__ == '__main__':
    main()