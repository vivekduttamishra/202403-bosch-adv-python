
import time
import asyncio

async def long_running_task():
    print('Starting long-running')
    time.sleep(2) #sleep for two seconds
    print('Ending long-running task')

async def main():
    await long_running_task()
    

if __name__ == '__main__':
    asyncio.run(main())

