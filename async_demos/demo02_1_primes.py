from utils.primes import find_primes

# the below blocks are synchronous
# int the current model it can't be handled concurrently.

result1= find_primes(2,100_000) # 19sec
print( len(result1))

result2 = find_primes(2,100) # 0.0 second
print(len(result2))