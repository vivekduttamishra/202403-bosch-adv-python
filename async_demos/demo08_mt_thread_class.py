import threading

class CountDownThread(threading.Thread):
    def __init__(self, max, min=0):
        super().__init__()
        self.max = max
        self.min = min

    def run(self):        
        t=threading.current_thread()
        print(f'[#{t.ident}] starts from count {self.max}->{self.min}')
        for i in range(self.max, self.min, -1):
            print(f'[#{t.ident}] counts {i}')

        print(f'[#{t.ident}] ends')
            


def main():
    print('start three threads')
    
    t1=CountDownThread(100,20)
    t2=CountDownThread(40)
    t3=CountDownThread(70)

    t1.start()
    t2.start()
    t3.start()

    print('Main Thread Ends')
   

if __name__ == '__main__':
    main()