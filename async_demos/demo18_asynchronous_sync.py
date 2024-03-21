import time
import threading
from utils.decorators import performance,log_call
from utils.threadutils import asynchronous

@asynchronous
def factorial(x):
    fx=1
    for i in range(1,x+1):
        time.sleep(1)
        fx*=i
    return fx

@performance
def permutation(n,r):

    fn= factorial(n) # is not returning int. It is returning Task

    #if we want to run sync
    fn_r= factorial.sync(n-r) # this will run syncrhonously and return result (not task)

    print('waiting for factorial calculatios...')
   
    p=fn.result/fn_r
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