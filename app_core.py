
from multiprocessing import Process 
def calcular_factorial(n):
    f = n
    for i in range(1,n):
        f = f*(n-i)
    print(f)
    return f
def calcular_multiplicación(lista):
    r = 1
    for i in lista:
        r = r*i
    print(r)
    return r
def main():
    
    p1 = Process(target=calcular_factorial,args=[10],name='p1')
    p2 =Process(target=calcular_multiplicación,args=[[2,4,6,10,5]])

    p1.start
    p2.start
    
    p1.run()
    p2.run()

    p1.join
    p1.join


    
main()
