def cari_mahasiswa(data, nim):
    """
    Mencari mahasiswa berdasarkan NIM.
    Mengembalikan data mahasiswa jika ditemukan,
    atau string pesan jika tidak ditemukan.
    """
    return data.get(nim, "Data tidak ditemukan")


def rata_rata_nilai(data):
    """
    Menghitung rata-rata nilai seluruh mahasiswa.
    """
    if len(data) == 0:
        return 0

    total = 0

    for info in data.values():
        total += info["nilai"]

    return total / len(data)


# Data awal mahasiswa
data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}

print("=== TEST CASE 1 : PENCARIAN TERSEDIA ===")
hasil = cari_mahasiswa(data_mahasiswa, "A003")
print(hasil)

print("\n=== TEST CASE 2 : PENCARIAN TIDAK TERSEDIA ===")
hasil = cari_mahasiswa(data_mahasiswa, "A999")
print(hasil)

print("\n=== TEST CASE 3 : PEMBARUAN NILAI ===")
data_mahasiswa["A002"]["nilai"] = 82
print("Nilai A002 setelah diubah:")
print(data_mahasiswa["A002"])

print("\n=== TEST CASE 4 : PENAMBAHAN DATA ===")
data_mahasiswa["A006"] = {
    "nama": "Fajar",
    "kelas": "B",
    "nilai": 80
}

print("Data A006:")
print(data_mahasiswa["A006"])

print("\n=== TEST CASE 5 : REKAP SELURUH DATA ===")
for nim, info in data_mahasiswa.items():
    print(
        f"NIM: {nim}, "
        f"Nama: {info['nama']}, "
        f"Kelas: {info['kelas']}, "
        f"Nilai: {info['nilai']}"
    )

print("\n=== RATA-RATA NILAI ===")
print(f"Rata-rata nilai = {rata_rata_nilai(data_mahasiswa):.2f}")