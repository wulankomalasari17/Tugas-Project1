from trapezoid import*

def f(x):
    return x**2+6

a=float(input('batas bawah = '))
b=float(input('batas atas = '))
n=int(input('jumlah grid = '))

integral=trapezoid(f,a,b,n)

print('integral=', integral)
        
