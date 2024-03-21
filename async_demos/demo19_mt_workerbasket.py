from utils.threadutils import asynchronous
from utils.decorators import performance
import time

class Basket:
    def __init__(self):
        self._apples=0
    
    def add(self):

        apples=self._apples

        time.sleep(0.001) #1ms
        
        apples+=1

        self._apples=apples

    @property
    def apples(self): return self._apples

@asynchronous
def worker(job_count, basket):
    for i in range(job_count):
        basket.add()

@performance
def manager(worker_count, job_count, use_private_basket=True):
    common_basket = Basket() if not use_private_basket else None
    workers=[]
    baskets=[]

    for i in range(worker_count):
        basket = common_basket
        if use_private_basket:
            basket=Basket()
            baskets.append(basket)

        w=worker(job_count, basket)
        workers.append(w)

    print('All workers scheduled. waiting for workers to complete')
    for w in workers:
        w.join()

    print('All workers completed. counting total work code')
    total=0
    if use_private_basket:
        for b in baskets:
            total+=b.apples    
    else:
        total=common_basket.apples

    print(f'Total work code: {total}')


def main():
    #1000 threads each count 10_000
    manager(1_000, 1_000, use_private_basket=True) #non shared resource
    manager(1_000, 1_000, use_private_basket=False) #shared resource


if __name__ == '__main__':
    main()