
import time
import asyncio

async def long_running_task():
    print('Starting long-running')
    time.sleep(2) #sleep for two seconds
    print('Ending long-running task')

def main():
    loop=asyncio.get_event_loop()
    loop.run_until_complete(long_running_task())
    loop.close()
    

if __name__ == '__main__':
    main()

