def factorial(x):
    fx=1
    for i in range(1,x+1):
        fx*=i
    return fx


def permutation(n,r):

    fn=factorial(n)



    fn_r=factorial(n-r)



    return fn_r/fn

