def simpson_rule(func, a, b, n):
    """
    Menghitung integral numerik menggunakan metode Simpson.

    Parameters:
    - func: Fungsi yang akan diintegrasikan.
    - a: Batas bawah interval.
    - b: Batas atas interval.
    - n: Jumlah subinterval (harus genap).

    Returns:
    - Nilai integral numerik.
    """
    if n % 2 != 0:
        raise ValueError("Jumlah subinterval (n) harus genap untuk metode Simpson.")
    
    h = (b - a) / n
    result = func(a) + func(b)
    
    for i in range(1, n, 2):
        result += 4 * func(a + i * h)
    
    for i in range(2, n-1, 2):
        result += 2 * func(a + i * h)
    
    result *= h / 3
    return result

# Contoh penggunaan
def contoh_fungsi(x):
    return x**2+6

batas_bawah = 0
batas_atas = 1
jumlah_subinterval = 100

hasil_integral = simpson_rule(contoh_fungsi, batas_bawah, batas_atas, jumlah_subinterval)
print(f"Hasil integral numerik dengan metode Simpson: {hasil_integral}")
