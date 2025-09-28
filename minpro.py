from prettytable import PrettyTable

# Tabel ongkir
tarif = PrettyTable()
tarif.field_names = ["Tujuan", "≤1 kg", "≤5 kg", ">5 kg"]
tarif.add_row(["Dalam negeri", "Rp10.000", "Rp25.000", "Rp40.000"])
tarif.add_row(["Luar negeri",  "Rp100.000", "Rp300.000", "Rp600.000"])

# Tabel data pengiriman
tabel = PrettyTable()
tabel.field_names = ["Resi","Pengirim","Penerima","Barang","Tujuan","Berat (kg)","Harga (Rp)"]

# Menampilkan dan menghitung ongkir
def tampil_data():
    if not tabel._rows:
        print("Belum ada data pengiriman.")
    else:
        print("\n>>>>> DATA PENGIRIMAN <<<<<")
        print(tabel)

def tampil_tarif():
    print("\n>>>>> TABEL TARIF ONGKIR <<<<<")
    print(tarif)

def hitung_harga(tujuan, berat):
    tujuan = tujuan.lower()
    if tujuan == "dalam negeri" and berat <= 1:
        return 10000
    elif tujuan == "dalam negeri" and berat <= 5:
        return 25000
    elif tujuan == "dalam negeri" and berat > 5:
        return 40000
    elif tujuan == "luar negeri" and berat <= 1:
        return 100000
    elif tujuan == "luar negeri" and berat <= 5:
        return 300000
    elif tujuan == "luar negeri" and berat > 5:
        return 600000
    else:
        return 0

# Fitur  sebagai admin
def buat_data_admin():
    resi     = f"ADM{len(tabel._rows)+1}"
    pengirim = input("Nama Pengirim: ")
    penerima = input("Nama Penerima: ")
    barang   = input("Jenis Barang: ")
    tujuan_input = input("Tujuan (dalam negeri/luar negeri) 1/2: ") 
    tujuan_barang = None 
    try:
        tujuan = int(tujuan_input)
        if tujuan == 1:
            tujuan_barang = "dalam negeri"
            print("Tujuan berhasil ditambahkan")
        elif tujuan == 2:
            tujuan_barang = "luar negeri"
            print("Tujuan berhasil ditambahkan")
        else:
            print("Tidak valid!")
            return 
    except ValueError:
        print("Input tujuan harus angka 1 atau 2.")
        return 

    try:
        berat = float(input("Berat barang (kg): "))
        if berat <= 0:
            print("Berat harus lebih dari 0.")
            return 
    except ValueError:
        print("Berat harus angka.")
        return 
    harga = hitung_harga(tujuan_barang, berat)
    tabel.add_row([resi, pengirim, penerima, barang, tujuan_barang, berat, f"Rp{harga:,}"])
    print(f"Data ditambahkan oleh Admin. Resi: {resi}")


def update_data_admin():
    tampil_data()
    resi = input("Masukkan resi yang mau diupdate: ")
    for x in tabel._rows:
        if x[0] == resi:
            penerima = input(f"Penerima baru (Enter skip) [{x[2]}]: ") or x[2]
            tujuan   = input(f"Tujuan baru (Enter skip) [{x[4]}]: ") or x[4]
            try:
                berat = float(input(f"Berat baru (kg) (Enter skip untuk {x[5]}): ") or x[5])
                if berat <= 0:
                    print("⚠️ Berat harus lebih dari 0.")
                    return # Exit function if berat is 0 or less
            except ValueError:
                berat = float(x[5])
            harga = hitung_harga(tujuan, berat)
            x[2] = penerima
            x[4] = tujuan
            x[5] = berat
            x[6] = f"Rp{harga:,}"
            print("Data berhasil diupdate.")
            return
    print("Resi tidak ditemukan.")

def hapus_data_admin():
    tampil_data()
    resi = input("Masukkan resi yang mau dihapus: ")
    for x in tabel._rows:
        if x[0] == resi:
            tabel._rows.remove(x)
            print("Data berhasil dihapus.")
            return
    print("Resi tidak ditemukan.")

#  Fitur Customer
def buat_data_user():
    resi     = f"JSA{len(tabel._rows)+1}"
    pengirim = input("Nama Anda (pengirim): ")
    penerima = input("Nama Penerima: ")
    barang   = input("Jenis Barang: ")
    tujuan_input = input("Tujuan (dalam negeri/luar negeri) 1/2: ") # Get input as string first
    tujuan_barang = None 
    try:
        tujuan = int(tujuan_input)
        if tujuan == 1:
            tujuan_barang = "dalam negeri"
            print("Tujuan berhasil ditambahkan")
        elif tujuan == 2:
            tujuan_barang = "luar negeri"
            print("Tujuan berhasil ditambahkan")
        else:
            print("Tidak valid!")
            return 
    except ValueError:
        print("tujuan harus angka 1 atau 2.")
        return 

    try:
        berat = float(input("Berat barang (kg): "))
        if berat <= 0:
            print("Berat harus lebih dari 0.")
            return 
    except ValueError:
        print("Berat harus dalam angka.")
        return 

    harga = hitung_harga(tujuan_barang, berat) # Pass both 'tujuan_barang' and 'berat'
    tabel.add_row([resi, pengirim, penerima, barang, tujuan_barang, berat, f"Rp{harga:,}"]) # Add 'berat' to the row
    print(f"Data berhasil ditambahkan. resi Anda: {resi}")

# Menu jika memilih sebagai admin
def menu_admin():
    while True:
        print("\n>>>>> MENU ADMIN <<<<<")
        print("1. Create data pengiriman")
        print("2. Read / tampilkan data")
        print("3. Update data")
        print("4. Delete data")
        print("5. Lihat Tarif Ongkir")
        print("6. Logout")
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Gunakan angka 1-6.")
            continue
        except (KeyboardInterrupt, EOFError):
            print("\nShortcut diblokir! Gunakan menu Logout untuk keluar.")
            continue

        if pilih == 1:
            try:
                buat_data_admin()
            except (KeyboardInterrupt, EOFError):
                print("\nAksi dibatalkan.")
        elif pilih == 2:
            tampil_data()
        elif pilih == 3:
            try:
                update_data_admin()
            except (KeyboardInterrupt, EOFError):
                print("\nAksi dibatalkan.")
        elif pilih == 4:
            try:
                hapus_data_admin()
            except (KeyboardInterrupt, EOFError):
                print("\nAksi dibatalkan.")
        elif pilih == 5:
            tampil_tarif()
        elif pilih == 6:
            print("Selesai (logout admin).")
            break
        else:
            print("Pilihan tidak ada")

# Menu jika memilih sebagai  costumer
def menu_user():
    while True:
        print("\n>>>>> MENU CUSTOMER <<<<<")
        print("1. Create data pengiriman")
        print("2. Tampilkan data")
        print("3. Lihat Tarif Ongkir")
        print("4. Logout")
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Gunakan angka 1-4.")
            continue
        except (KeyboardInterrupt, EOFError):
            print("\nShortcut diblokir! Gunakan menu Logout untuk keluar.")
            continue

        if pilih == 1:
            try:
                buat_data_user()
            except (KeyboardInterrupt, EOFError):
                print("\nAksi dibatalkan.")
        elif pilih == 2:
            tampil_data()
        elif pilih == 3:
            tampil_tarif()
        elif pilih == 4:
            print("Selesai (logout customer).")
            break
        else:
            print("Pilihan tidak ada")

# Memilih login sebagai admin atau customer
def menu_awal():
    while True:
        print("\n>>>>> MENU AWAL <<<<<")
        print("1. Login sebagai Admin")
        print("2. Login sebagai Customer")
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Masukkan angka 1/2 saja.")
            continue
        except (KeyboardInterrupt, EOFError):
            print("\nShortcut diblokir! Gunakan menu yang tersedia.")
            continue

        if pilih == 1:
            try:
                user = input("Username: ")
                pw   = input("Password: ")
            except (KeyboardInterrupt, EOFError):
                print("\nShortcut diblokir! Kembali ke menu awal.")
                continue
            if user == "admin" and pw == "0000":
                print("Login Sebagai Admin berhasil")
                menu_admin()
            else:
                print("Username/password salah.")
        elif pilih == 2:
            print("Login Sebagai Customer berhasil")
            menu_user()
        else:
            print("Pilihan tidak ada")
menu_awal()