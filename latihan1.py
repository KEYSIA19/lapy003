import random

# Fungsi untuk menampilkan n bilangan acak yang lebih kecil dari 0.5
def generate_random_numbers(n):
    # Daftar untuk menyimpan hasil bilangan acak yang lebih kecil dari 0.5
    result = []
    
    # Perulangan menggunakan while dan for
    while len(result) < n:
        number = random.random()  # Generate bilangan acak antara 0 dan 1
        if number < 0.5:  # Jika bilangan lebih kecil dari 0.5, tambahkan ke daftar
            result.append(number)
    
    return result

# Contoh penggunaan fungsi dengan memasukkan nilai n secara langsung
n = 5  # Ganti sesuai kebutuhan
print(generate_random_numbers(n))