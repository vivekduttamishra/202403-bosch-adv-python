import time
import threading
from utils.decorators import performance,log_call

def factorial(x):
    fx=1
    for i in range(1,x+1):
        time.sleep(1)
        fx*=i
    return fx


class Factorial(threading.Thread):
    def __init__(self,x):
        super().__init__()
        self.x = x
        self.result=1

    def run(self):
        self.result=factorial(self.x)



@performance
def permutation(n,r):

    fn=Factorial(n)     #factorial(n)
    fn.start()

    fn_r=Factorial(n-r) #factorial(n-r)
    fn_r.start()


    # now we should wait for the task to complete.
    fn.join()
    fn_r.join()


    p=fn.result/fn_r.result
    return p

@log_call
def main():
    n=8
    r=3
    p=permutation(n,r) #2n-r
    print(f'{n} P {r} => {p}')


#assignment : bring the performance to "n" seconds by concurrently running two factorial calls

def plus(x,y):return x+y

if __name__ == '__main__':
    main()