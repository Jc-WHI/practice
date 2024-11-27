
##파이썬도 함수 리턴 타입 선언 가능

def fib(n:int)->int:
    if(n<2):
        return n
    else:
        return fib(n-2)+fib(n-1)
    



if __name__ == '__main__':
    n = 20
    for i in range(n+1):
        result = fib(i)
        print(f"{result}")