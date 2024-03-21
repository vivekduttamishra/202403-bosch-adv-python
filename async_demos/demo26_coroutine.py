
import time
import asyncio

async def make_coffee(coffee_type):
    print(f'boiling water')
    await asyncio.sleep(1) # will take time to boil
    print(f'adding  {coffee_type}')
    await asyncio.sleep(.5) # will take time again
    return coffee_type

async def make_salad(*args):
    salad=[]
    for ingredient in args:
        print(f'adding {ingredient}')
        salad.append(ingredient)
        await asyncio.sleep(.5) 

    return salad

async def main():
    coffee_task =asyncio.create_task(make_coffee('espresso'))
    salad_task =asyncio.create_task(make_salad('onion','lettuce','chicken','cheese'))
    
    coffee=await coffee_task
    salad=await salad_task

    print(f'{coffee=}')
    print(f'{salad=}')
    

if __name__ == '__main__':
    asyncio.run(main())

