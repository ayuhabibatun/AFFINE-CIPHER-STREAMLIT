import streamlit as st

# Fungsi untuk memeriksa apakah dua bilangan coprime
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Fungsi enkripsi affine cipher
def affine_encrypt(p, a, b):
    cip = ''
    for i in range(len(p)):
        if p[i].isalpha():
            base = 97 if p[i].islower() else 65
            c = ((a * (ord(p[i]) - base) + b) % 26) + base
            cip += chr(c)
        else:
            cip += p[i]
    return cip

# Antarmuka Streamlit
st.title("Affine Cipher Encryptor")

# Input dari pengguna
p = st.text_input("Masukkan plaintext:")

a = st.number_input("Masukkan kunci a (harus coprime dengan 26):", min_value=1, step=1)
b = st.number_input("Masukkan kunci b:", min_value=0, step=1)

# Tombol enkripsi
if st.button("Enkripsi"):
    if gcd(a, 26) != 1:
        st.error("Kunci a harus coprime dengan 26.")
    else:
        ciphertext = affine_encrypt(p, a, b)
        st.success(f"Ciphertext: {ciphertext}")
