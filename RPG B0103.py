
# =====================================
# U PRAKTIKUM ALGORITMA
# Sistem Profil Karakter Game RPG
# =====================================

# 1. Membuat variabel profil karakter
nama_hero = "Shadow Knight"
level = 10
hp = 100.5
is_alive = True

inventory = ["Pedang", "Perisai", "Busur"]

atribut = {
    "kekuatan": 80,
    "kelincahan": 65
}

# 2. Menampilkan seluruh informasi karakter
print("=== PROFIL KARAKTER AWAL ===")
print("Nama Hero :", nama_hero)
print("Level     :", level)
print("HP        :", hp)
print("Is Alive  :", is_alive)
print("Inventory :", inventory)
print("Atribut   :", atribut)

# 3. Menampilkan tipe data setiap variabel
print("\n=== TIPE DATA VARIABEL ===")
print("Tipe nama_hero :", type(nama_hero))
print("Tipe level     :", type(level))
print("Tipe hp        :", type(hp))
print("Tipe is_alive  :", type(is_alive))
print("Tipe inventory :", type(inventory))
print("Tipe atribut   :", type(atribut))

# 4. Melakukan aksi karakter

# Menambahkan item baru ke inventory
inventory.append("Ramuan HP")

# Karakter naik level
level = float(level) + 0.5

# 5. Menampilkan informasi terbaru
print("\n=== PROFIL KARAKTER TERBARU ===")
print("Nama Hero :", nama_hero)
print("Level     :", level)
print("HP        :", hp)
print("Is Alive  :", is_alive)
print("Inventory :", inventory)
print("Atribut   :", atribut)

print("\nTipe Level Terbaru :", type(level))
