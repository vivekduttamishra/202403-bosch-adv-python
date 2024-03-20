import threading


def show_thread_info():
    t=threading.current_thread()
    print(f'Current Thread is {t.name=}, {t.ident=}')

def main():
    print('starting application')
    #creating a user defined thread
    # create a new thread that will run show_thread_info function asynchronously
    user_thread= threading.Thread(target=show_thread_info)

    #thread is created but not running
    #to run it we must start it
    user_thread.start()  # will run show_thread_info function on a separate thread (path)

    show_thread_info()  # will run show_thread_info on the main thread
    
# this program with call show_thread_info twice
# once inside main thread and once inside a new user_thread   
# which one will print firs can't be ensured
# they are independent


if __name__ == '__main__':
    main()