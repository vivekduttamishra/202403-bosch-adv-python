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
        self._result=None
        self.start()

    def run(self):
        self._result=factorial(self.x)

    @property
    def result(self):
        self.join()
        return self._result



@performance
def permutation(n,r):

    fn=Factorial(n)     #factorial(n)
   

    fn_r=Factorial(n-r) #factorial(n-r)
   

    print('waiting for factorial calculatios...')
   
    # if you ask for a result, it will automaticaly wait for completeion
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