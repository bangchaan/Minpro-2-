# Minpro-2- DDP 2025
AULIA AISYAH AL HUMAIRA 25'A DDP
# Program Jasa Pengiriman Barang 

## Deskripsi Singkat  
Program ini dibuat untuk mensimulasikan sistem **jasa pengiriman barang** sederhana. 

Terdapat dua jenis pengguna:  
- **Admin** → bisa membuat, membaca, mengubah, dan menghapus data pengiriman.  
- **Customer** → hanya bisa membuat data pengiriman dan melihat daftar pengiriman serta tarif ongkir.  



## Fitur Utama  

###  Menu Awal  
1. Login sebagai **Admin** (username & password)  
2. Login sebagai **Customer**  
3. Keluar program  

### 👨‍💻 Fitur Admin  
- **Create Data Pengiriman** → Admin memasukkan data pengiriman (resi otomatis `ADM`, pengirim, penerima, barang, tujuan, berat).  
- **Read Data** → Menampilkan semua data pengiriman dalam bentuk tabel.  
- **Update Data** → Admin bisa mengubah *penerima*, *tujuan*, atau *berat barang*. Harga akan dihitung ulang otomatis.  
- **Delete Data** → Hapus data pengiriman berdasarkan nomor resi.  
- **Lihat Tarif Ongkir** → Menampilkan tabel tarif ongkir.  
- **Logout** → Kembali ke menu awal.  

☆ Fitur Untuk Customer
- **Create Data Pengiriman** → Customer hanya mengisi data pengiriman (resi otomatis `JSA`, pengirim, penerima, barang, tujuan, berat). Customer tidak bisa update/hapus data setelah disimpan.  
- **Read Data** → Menampilkan semua data pengiriman.  
- **Lihat Tarif Ongkir** → Menampilkan tabel tarif ongkir.  
- **Logout** → Kembali ke menu awal.  

---

## Perhitungan Ongkir  
Harga dihitung otomatis berdasarkan **TUJUAN** dan **BERAT BARANG** dengan aturan:

**Dalam negeri**
  - ≤ 1 kg → Rp10.000  
  - ≤ 5 kg → Rp25.000  
  - > 5 kg → Rp40.000  

- **Luar negeri**
  - ≤ 1 kg → Rp100.000  
  - ≤ 5 kg → Rp300.000  
  - > 5 kg → Rp600.000  

