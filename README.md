# 📸 Sistem Absensi Wajah
```markdown
Sistem absensi cerdas berbasis Python yang menggunakan kamera laptop/PC untuk mengenali wajah secara *real-time*. Dilengkapi dengan sistem **Memory Cache** agar kamera tetap mulus (bebas *lag*) dan tidak membebani memori meskipun file *database* absensi sudah penuh.

## ✨ Fitur Utama

* **Deteksi Real-Time:** Mengenali wajah langsung dari *webcam*.
* **Memory Caching:** Mencegah program membaca/menulis file CSV berkali-kali dalam satu detik. Wajah yang sama hanya akan dicatat 1 kali dalam kurun waktu 1 jam.
* **Auto-Folder:** Otomatis membuat folder *database* jika belum ada.
* **CSV Logging:** Menyimpan data absensi (Nama, Jam, Tanggal) dengan rapi ke dalam file `Absensi.csv`.

---

## 🛠️ Persyaratan & Instalasi Library

Sebelum menjalankan *script* ini, pastikan Python sudah terpasang di komputer Anda. Buka terminal/CMD, lalu ketik perintah berikut untuk menginstal semua *library* pendukung:

```bash
pip install opencv-python numpy face_recognition
```

> **💡 TIPS PENTING (Khusus Pengguna Windows):**
> *Library* `face_recognition` membutuhkan *package* `dlib` untuk bisa berjalan. Jika proses *install* di Windows gagal, Anda harus menginstal **CMake** dan **Visual Studio C++ Build Tools** terlebih dahulu.

---

## 📂 Struktur Folder & Cara Penggunaan

Pastikan struktur *project* Anda terlihat seperti ini sebelum dijalankan:

```text
📁 Project-Folder/
│
├── 📄 Absen.py                 # Script utama aplikasi
├── 📄 Absensi.csv              # (Akan terbuat otomatis) File hasil absensi
└── 📁 ImagesAttendance/        # Folder tempat menaruh foto wajah
    ├── 🖼️ Haqi.jpg
    └── 🖼️ NamaLain.png
```

### Langkah-Langkah Penggunaan:

1. **Siapkan Database Wajah:** * Buat folder bernama `ImagesAttendance` sejajar dengan file `Absen.py`.
   * Masukkan foto wajah orang yang ingin dikenali (harus jelas menghadap depan).
   * **Ganti nama filenya** dengan nama orang tersebut (Contoh: `Haqi.jpg`). *Nama inilah yang akan muncul di layar dan masuk ke sistem absen*.
2. **Jalankan Program:**
   Buka terminal, arahkan ke folder *project*, lalu jalankan perintah:
   ```bash
   python Absen.py
   ```
3. **Melakukan Absensi:**
   Tatap kamera hingga kotak hijau dan nama Anda muncul. Di terminal akan muncul tulisan `[DATA MASUK] Nama berhasil absen...`. Data otomatis tersimpan di `Absensi.csv`.
4. **Mematikan Kamera:**
   Klik pada jendela kamera (*window* OpenCV), lalu tekan tombol **`q`** pada *keyboard* untuk mematikan kamera dengan aman.

---

## ⚠️ Kekurangan & Batasan Sistem

Sistem ini masih berupa *prototype* dasar dan memiliki beberapa batasan:

1. **Rentan Terhadap Manipulasi Foto (No Liveness Detection):** Sistem ini masih bisa diakali jika seseorang menghadapkan foto wajah cetak atau foto dari layar HP ke depan kamera. Sistem belum bisa membedakan mana wajah asli 3D dan foto 2D.
2. **Sangat Bergantung pada Pencahayaan:** Jika ruangan terlalu gelap atau posisi kamera *backlight* (membelakangi cahaya terang), wajah akan sulit dideteksi dan dikenali (akan sering muncul tulisan "Unknown").
3. **Beban CPU Tinggi (Tanpa GPU):** *Library* `face_recognition` sangat berat untuk CPU. Jika mendeteksi banyak wajah sekaligus dalam satu layar, kamera bisa mengalami penurunan *frame rate* (FPS drop).
4. **Sensitif Terhadap Sudut Wajah:** Wajah harus menghadap lurus ke depan kamera. Jika menoleh terlalu jauh ke samping atau menunduk, wajah mungkin tidak terdeteksi.
