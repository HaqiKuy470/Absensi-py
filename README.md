# 📸 Sistem Absensi Wajah Anti-Lag (Face Recognition)

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
