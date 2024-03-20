import threading


def main():
    print('starting application')

    #returns the current thread which is running this code
    t= threading.current_thread()
    
    print(f'current thread is {t}')
    print(f'{t.name=}')
    print(f'{t.ident=}') #id of the thread



if __name__ == '__main__':
    main()