# Pertemuan 11 - Dictionary/Map

Nama: Siti Nurhasanah  
NIM: 2225250073 
Kelas: 3B

## Tujuan

Memodelkan data pendidikan menggunakan dictionary dan pasangan key-value dalam Python, melakukan pencarian data berdasarkan NIM, menambah data, memperbarui data, menampilkan seluruh data, serta menghitung rata-rata nilai mahasiswa.

## Struktur Data

Program menggunakan dictionary bersarang (nested dictionary).

- Key utama berupa NIM mahasiswa.
- Value berupa dictionary yang berisi:
  - nama
  - kelas
  - nilai

Contoh:

```python
data_mahasiswa = {
    "A001": {
        "nama": "Ayu",
        "kelas": "A",
        "nilai": 85
    }
}
```

Keterangan:
- NIM digunakan sebagai key karena bersifat unik.
- Data mahasiswa disimpan sebagai value agar dapat menampung beberapa atribut sekaligus.

## Fungsi yang Digunakan

### 1. cari_mahasiswa(data, nim)

Digunakan untuk mencari data mahasiswa berdasarkan NIM.

```python
def cari_mahasiswa(data, nim):
    return data.get(nim, "Data tidak ditemukan")
```

### 2. rata_rata_nilai(data)

Digunakan untuk menghitung rata-rata nilai seluruh mahasiswa.

```python
def rata_rata_nilai(data):
    if len(data) == 0:
        return 0

    total = 0

    for info in data.values():
        total += info["nilai"]

    return total / len(data)
```

## Cara Menjalankan

Buka terminal pada folder proyek kemudian jalankan:

```bash
python3 praktik/data_mahasiswa.py
```

atau

```bash
python praktik/data_mahasiswa.py
```

## Test Case

| No | Input/Aksi | Hasil yang Diharapkan | Hasil Aktual | Status |
|----|------------|----------------------|--------------|---------|
| 1 | Cari NIM A003 | Data Citra ditampilkan | Data Citra tampil | ✅ Lulus |
| 2 | Cari NIM A999 | "Data tidak ditemukan" | Pesan tampil | ✅ Lulus |
| 3 | Ubah nilai A002 menjadi 82 | Nilai berubah menjadi 82 | Nilai berhasil berubah | ✅ Lulus |
| 4 | Tambah data A006 | Data A006 tersimpan | Data berhasil ditambah | ✅ Lulus |
| 5 | Tampilkan seluruh data dengan items() | Semua data tampil | Semua data tampil | ✅ Lulus |
| 6 | Hitung rata-rata nilai | Rata-rata benar | Rata-rata = 83.50 | ✅ Lulus |

## Hasil Program

Contoh keluaran:

```text
=== TEST CASE 1 : PENCARIAN TERSEDIA ===
{'nama': 'Citra', 'kelas': 'B', 'nilai': 92}

=== TEST CASE 2 : PENCARIAN TIDAK TERSEDIA ===
Data tidak ditemukan

=== TEST CASE 3 : PEMBARUAN NILAI ===
{'nama': 'Budi', 'kelas': 'A', 'nilai': 82}

=== TEST CASE 4 : PENAMBAHAN DATA ===
{'nama': 'Fajar', 'kelas': 'B', 'nilai': 80}

=== RATA-RATA NILAI ===
83.50
```

## Refleksi

Kesalahan yang ditemukan saat mempelajari dictionary adalah mencoba mengakses key yang tidak tersedia menggunakan kurung siku ([]), sehingga dapat menyebabkan KeyError.

Contoh:

```python
data["kelas"]
```

Jika key "kelas" tidak ada, program akan menghasilkan KeyError.

Perbaikannya adalah menggunakan method get() agar program tetap berjalan dengan aman.

```python
data.get("kelas", "Data tidak ditemukan")
```

Melalui latihan ini saya memahami bahwa dictionary lebih tepat digunakan dibandingkan list ketika data perlu diakses berdasarkan identitas unik seperti NIM.