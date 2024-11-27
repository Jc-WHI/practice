

def fac(n:int)->int:
    if (n==0|n==1):
        return 1
    else:
        result= fac(n-1) + fac(n-2)
        return result 
    


    if __name__ =='__main__':
        result = fac(5)
        print(f"{result}")
