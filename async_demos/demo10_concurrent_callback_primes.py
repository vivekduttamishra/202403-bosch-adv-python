from utils.primes import find_primes
from utils.decorators import log_call, performance
import threading

@log_call
def find_primes_cb( min, max, result_processor):
    result = find_primes(min, max)
    result_processor(min,max,result)

@performance
def main():

    # now we have concurrent model
    # this call will start find_primes
    threading.Thread(target=find_primes_cb, args=(2,100_000, 
        lambda min,max,result: print(f'Total Primes in range {min}-{max}:{len(result)}'))).start() 


    # we dont' wait but reach here immediately
    threading.Thread(target=find_primes_cb, args=(2,100, 
        lambda min,max,result: print(f'Primes in range {min}-{max}:{result}'))).start()

    # main ends.
    # but results will be printed once long running tasks are finished.

if __name__ == '__main__':
    main()