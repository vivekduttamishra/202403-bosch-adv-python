import threading


def count_down():
    max=20
    t=threading.current_thread()
    print(f'[#{t.ident}] starts from {max}')
    for i in range(max, 0, -1):
        print(f'[#{t.ident}] counts {i}')

    print(f'[#{t.ident}] ends')
        


def main():
    print('start three threads')
    t1=threading.Thread(target=count_down)
    t2=threading.Thread(target=count_down)
    t3=threading.Thread(target=count_down)

    t1.start()
    t2.start()
    t3.start()

    print('Main Thread Ends')
   

if __name__ == '__main__':
    main()