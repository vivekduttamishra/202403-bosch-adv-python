import threading
import time


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

    #busy_main()
    #printing_main()
    #time.sleep(5)

    #wait_for_alive_threads(t1,t2,t3)

    t1.join() #main waits for t1 to (finish and) join
    t2.join() #main waits for t2 to (finish and) join
    t3.join() #main waits for t3 to (finish and) join

    print(f'{wait_loop_count=}')
    print('Main Thread Ends. This should be the last message from the program')
    

wait_loop_count=0

def wait_for_alive_threads(t1,t2,t3):
    global wait_loop_count
    while t1.is_alive() or t2.is_alive() or t3.is_alive():
        wait_loop_count+=1
        time.sleep(0.01) #10ms
        
    


def busy_main():
    for i in range(2_00_000):
        pass

def printing_main():
    for i in range(135):
        print('main thread is waiting...')

if __name__ == '__main__':
    main()