# import time

# def backup_files():
#     start = time.time()
#     print('backup_files started')
#     time.sleep(5)
#     print('backup_files finished')
#     end = time.time()
#     print(f'Time taken backup_files: {end - start} seconds')


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

@performance
def main():
    backup_files()
    run_antivirus()
    print('main finished')


if __name__ == '__main__':
    main()