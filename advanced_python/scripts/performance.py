import time

def place_order():
    print('placing order...')
    time.sleep(1.4)
    print('order placed')

def find_performance(fn):
    start=time.time()
    fn()
    end=time.time()
    print(f'Total Time taken is {end-start} seconds')


find_performance(place_order)