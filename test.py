# test.py

from des_algorithm import feistel_network
from keygen import key_schedule

# Fungsi untuk mengonversi string ke biner (bit)
def text_to_bits(text):
    return [int(bit) for bit in ''.join(f'{ord(c):08b}' for c in text)]

# Fungsi untuk mengonversi biner (bit) ke string
def bits_to_text(bits):
    chars = [bits[i:i+8] for i in range(0, len(bits), 8)]
    return ''.join(chr(int(''.join(map(str, byte)), 2)) for byte in chars)

# Fungsi untuk menghapus padding (hanya mengambil bagian yang relevan dari plaintext)
def remove_padding(bits):
    # Menghapus bit padding (0) di akhir
    while bits and bits[-1] == 0:
        bits.pop()
    return bits

# Input teks
input_text = "Hello, DES!"
print(f"Original text: {input_text}")

# Konversi teks ke biner (bit)
message = text_to_bits(input_text)

# Tambahkan padding jika panjang message tidak 64-bit
if len(message) % 64 != 0:
    padding = [0] * (64 - len(message) % 64)
    message += padding
    print(f"Message padded: {message}")

# Contoh kunci 64-bit
key = [0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1]

# Menghasilkan subkunci
subkeys = key_schedule(key)

# Enkripsi pesan
ciphertext = []
for i in range(0, len(message), 64):  # Proses blok 64-bit
    block = message[i:i+64]
    ciphertext.extend(feistel_network(block, subkeys, encrypt=True))

print(f"Ciphertext: {ciphertext}")

# Dekripsi ciphertext
plaintext_bits = []
for i in range(0, len(ciphertext), 64):  # Proses blok 64-bit
    block = ciphertext[i:i+64]
    plaintext_bits.extend(feistel_network(block, subkeys, encrypt=False))

print(f"Plaintext bits: {plaintext_bits}")

# Menghapus padding dari plaintext bits
plaintext_bits = remove_padding(plaintext_bits)

# Konversi kembali dari biner ke teks
decrypted_text = bits_to_text(plaintext_bits)
print(f"Decrypted text: {decrypted_text}")
