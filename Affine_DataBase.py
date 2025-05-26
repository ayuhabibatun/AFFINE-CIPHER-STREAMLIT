import streamlit as st
import sqlite3

# ---------------------- Fungsi Affine Cipher ----------------------
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def affine_encrypt(text, a, b):
    cip = ''
    for char in text:
        if char.isalpha():
            base = 97 if char.islower() else 65
            c = ((a * (ord(char) - base) + b) % 26) + base
            cip += chr(c)
        else:
            cip += char
    return cip

# ---------------------- Database ----------------------
def create_table():
    conn = sqlite3.connect('affine_cipher.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS mahasiswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT,
            nim TEXT,
            prodi TEXT,
            a INTEGER,
            b INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def insert_mahasiswa(nama, nim, prodi, a, b):
    conn = sqlite3.connect('affine_cipher.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO mahasiswa (nama, nim, prodi, a, b)
        VALUES (?, ?, ?, ?, ?)
    ''', (nama, nim, prodi, a, b))
    conn.commit()
    conn.close()

def fetch_all_mahasiswa():
    conn = sqlite3.connect('affine_cipher.db')
    c = conn.cursor()
    c.execute('SELECT * FROM mahasiswa ORDER BY id DESC')
    data = c.fetchall()
    conn.close()
    return data

# ---------------------- Streamlit UI ----------------------
st.set_page_config(page_title="Enkripsi Mahasiswa Affine Cipher")
st.title("🔐 Enkripsi Data Mahasiswa dengan Affine Cipher")

create_table()

menu = st.sidebar.radio("Menu", ["Enkripsi Mahasiswa", "Lihat Data Mahasiswa"])
a = st.sidebar.number_input("Kunci a (coprime dengan 26)", min_value=1, step=1, value=5)
b = st.sidebar.number_input("Kunci b", min_value=0, step=1, value=8)

if gcd(a, 26) != 1:
    st.sidebar.error("❌ Nilai a harus coprime dengan 26!")

if menu == "Enkripsi Mahasiswa":
    st.subheader("📝 Formulir Data Mahasiswa")

    nama = st.text_input("Nama Mahasiswa")
    nim = st.text_input("NIM")
    prodi = st.text_input("Program Studi")

    if st.button("🔐 Enkripsi dan Simpan"):
        if not nama or not nim or not prodi:
            st.error("Semua kolom harus diisi!")
        elif gcd(a, 26) != 1:
            st.error("Nilai a tidak valid. Harus coprime dengan 26.")
        else:
            nama_encrypted = affine_encrypt(nama, a, b)
            nim_encrypted = affine_encrypt(nim, a, b)
            prodi_encrypted = affine_encrypt(prodi, a, b)

            insert_mahasiswa(nama_encrypted, nim_encrypted, prodi_encrypted, a, b)
            st.success("Data mahasiswa terenkripsi dan disimpan!")

elif menu == "Lihat Data Mahasiswa":
    st.subheader("📄 Data Mahasiswa Terenkripsi")
    records = fetch_all_mahasiswa()

    if not records:
        st.info("Belum ada data mahasiswa.")
    else:
        for r in records:
            st.write(f"ID: {r[0]}")
            st.write(f"Nama (encrypted): `{r[1]}`")
            st.write(f"NIM (encrypted): `{r[2]}`")
            st.write(f"Prodi (encrypted): `{r[3]}`")
            st.write(f"Kunci a: {r[4]} | b: {r[5]}")
            st.markdown("---")
