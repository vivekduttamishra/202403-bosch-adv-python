from utils.primes import find_primes
from utils.decorators import log_call


@log_call
def find_primes_cb( min, max, result_processor):
    result = find_primes(min, max)
    result_processor(min,max,result)



# the below two function are asynchronously
# now you may use the concurrently

find_primes_cb(2,100_000, 
    lambda min,max,result: print(f'Total Primes in range {min}-{max}:{len(result)}')) 


find_primes_cb(2,100, 
    lambda min,max,result: print(f'Primes in range {min}-{max}:{result}')) 
