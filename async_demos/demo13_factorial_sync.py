import time
from utils.decorators import performance,log_call

def factorial(x):
    fx=1
    for i in range(1,x+1):
        time.sleep(1)
        fx*=i
    return fx

@performance
def permutation(n,r):
    fn=factorial(n)
    fn_r=factorial(n-r)
    
    p=fn/fn_r
    return p

@log_call
def main():
    n=8
    r=3
    p=permutation(n,r) #2n-r
    print(f'{n} P {r} => {p}')


#assignment : bring the performance to "n" seconds by concurrently running two factorial calls

if __name__ == '__main__':
    main()