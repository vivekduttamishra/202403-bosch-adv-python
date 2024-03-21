
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
    coffee =await make_coffee('espresso')
    salad =await make_salad('onion','lettuce','chicken','cheese')
    print(f'{coffee=}')
    print(f'{salad=}')
    

if __name__ == '__main__':
    asyncio.run(main())

