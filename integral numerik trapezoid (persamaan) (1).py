def trapezoidal_rule(func, a, b, n):
    """
    Menghitung integral numerik menggunakan metode trapesium.

    Parameters:
    - func: Fungsi yang akan diintegrasikan.
    - a: Batas bawah interval.
    - b: Batas atas interval.
    - n: Jumlah trapesium atau subinterval.

    Returns:
    - Nilai integral numerik.
    """
    h = (b - a) / n
    result = 0.5 * (func(a) + func(b))
    
    for i in range(1, n):
        result += func(a + i * h)
    
    result *= h
    return result

# Contoh penggunaan
def contoh_fungsi(x):
    return x**2

batas_bawah = 0
batas_atas = 1
jumlah_subinterval = 6

hasil_integral = trapezoidal_rule(contoh_fungsi, batas_bawah, batas_atas, jumlah_subinterval)
print(f"Hasil integral numerik: {hasil_integral}")
