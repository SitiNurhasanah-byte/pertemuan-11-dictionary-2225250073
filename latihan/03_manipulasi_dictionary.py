data = {
    "nama": "Ayu",
    "nilai": 85
}

# Menambah data baru
data["kelas"] = "A"

# Mengubah nilai
data["nilai"] = 90

# Menampilkan dictionary
print(data)

# Menghapus key "kelas"
data.pop("kelas")

# Menampilkan dictionary setelah penghapusan
print(data)