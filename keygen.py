# keygen.py

from des_algorithm import permute, PC1, PC2, ROTATIONS

def key_schedule(key):
    # Permutasi awal PC1
    key = permute(key, PC1)
    left, right = key[:28], key[28:]
    subkeys = []
    
    for rotation in ROTATIONS:
        # Rotasi kiri
        left = left[rotation:] + left[:rotation]
        right = right[rotation:] + right[:rotation]
        # Menggunakan PC2 untuk mendapatkan subkunci
        subkeys.append(permute(left + right, PC2))
    
    return subkeys
