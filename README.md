# Minpro-2- DDP 2025
AULIA AISYAH AL HUMAIRA 25'A DDP
# FLOWCHART
<img width="1663" height="1082" alt="minpro 2 drawio" src="https://github.com/user-attachments/assets/6ce9f4c0-dd2e-403f-b9e1-39e622287246" />

# Program Jasa Pengiriman Barang 
# DESKRIPSI SINGKAT

Program ini dibuat untuk mensimulasikan sistem **jasa pengiriman barang** sederhana. 

Terdapat dua jenis pengguna:  
- **Admin** → bisa membuat, membaca, mengubah, dan menghapus data pengiriman.  
- **Customer** → hanya bisa membuat data pengiriman dan melihat daftar pengiriman serta tarif ongkir.  


## Fitur Utama  

###  Menu Awal  
1. Login sebagai **Admin** (username & password)  
2. Login sebagai **Customer**  

###  Fitur Admin  
- **Create Data Pengiriman** → Admin memasukkan data pengiriman (resi otomatis `ADM`, pengirim, penerima, barang, tujuan, berat).  
- **Read Data** → Menampilkan semua data pengiriman dalam bentuk tabel.  
- **Update Data** → Admin bisa mengubah *penerima*, *tujuan*, atau *berat barang*. Harga akan dihitung ulang otomatis.  
- **Delete Data** → Hapus data pengiriman berdasarkan nomor resi.  
- **Lihat Tarif Ongkir** → Menampilkan tabel tarif ongkir.  
- **Logout** → Selesai.  

### Fitur Untuk Customer
- **Create Data Pengiriman** → Customer hanya mengisi data pengiriman (resi otomatis `JSA`, pengirim, penerima, barang, tujuan, berat). Customer tidak bisa update/hapus data setelah disimpan.  
- **Read Data** → Menampilkan semua data pengiriman.  
- **Lihat Tarif Ongkir** → Menampilkan tabel tarif ongkir.  
- **Logout** → Selesai  

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

### OUTPUT
![WhatsApp Image 2025-09-28 at 7 51 58 PM](https://github.com/user-attachments/assets/3f1e3a88-86fb-4c13-926e-b77ffc3228d7)
![WhatsApp Image 2025-09-28 at 7 54 29 PM](https://github.com/user-attachments/assets/daf7460b-4333-43a2-87fa-e0676ea79218)
![WhatsApp Image 2025-09-28 at 7 55 09 PM](https://github.com/user-attachments/assets/11873820-dc5d-4d1a-9e70-8aae2d755827)
![WhatsApp Image 2025-09-28 at 7 56 53 PM](https://github.com/user-attachments/assets/6fa27429-e861-423c-9db0-5cccf629ef93)
![WhatsApp Image 2025-09-28 at 7 56 52 PM](https://github.com/user-attachments/assets/344db979-a6f8-44ce-b618-9ffcbf8c61a9)


