

def fac(n:int)->int:
    if n==0 or n == 1:
        return 1
    else:
        result= n*fac(n-1)
        return result 
    


if __name__ =='__main__':
        result = fac(5)
        print(f"{result}")
