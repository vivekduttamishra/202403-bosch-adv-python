from utils.threadutils import asynchronous

def plus(x,y):
    return x+y

@asynchronous
def minus(x,y):
    return x-y

async def multiply(x,y):
    return x*y


def main():

    a= plus(2,3)
    b= minus(2,3)
    c= multiply(2,3)

    print(f'{a=}',f'{b=}',f'{c=}',sep='\n')    

if __name__ == '__main__':
    main()