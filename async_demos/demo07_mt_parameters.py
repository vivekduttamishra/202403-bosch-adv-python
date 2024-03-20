import threading


def count_down(max,min=0):
    
    t=threading.current_thread()
    print(f'[#{t.ident}] starts from count {max}->{min}')
    for i in range(max, min, -1):
        print(f'[#{t.ident}] counts {i}')

    print(f'[#{t.ident}] ends')
        


def main():
    print('start three threads')
    
    t1=threading.Thread(target=count_down, args=(50,25))
    t2=threading.Thread(target=count_down, args=[40])

    t3=threading.Thread(target=lambda: count_down(70))

    t1.start()
    t2.start()
    t3.start()

    print('Main Thread Ends')
   

if __name__ == '__main__':
    main()