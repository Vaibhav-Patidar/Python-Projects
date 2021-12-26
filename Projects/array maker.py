# create a array of numbers from 0 to 10000
import sys
sys.setrecursionlimit(10000)

def fun(k, n = 0, arr = []):
    if n == k:
        return
    else:
        arr.append(n)
        fun(k,n+1,arr)
    return arr

o = int(input("enter the number whose array you want -> "))
nn = int(input("enter the value of n"))
o = fun(o,nn,[])
print(o)