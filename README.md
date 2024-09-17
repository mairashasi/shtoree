**Maira Shasmeen Mazaya 2306245724**

# Tugas 2 PBP

1. Tautan menuju aplikasi PWS = http://maira-shasmeen-shtoree.pbp.cs.ui.ac.id

2. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step :
- Pertama, saya membuat direktori baru dengan nama 'Shtoree' (tema aplikasi saya adalah e-commerce clothing brand).
- Setelah itu, saya mengatur Django dengan mengaktifkan virtual environment, menyiapkan dependencies dengan membuat berkas `requirements.txt`, menginstal dependencies dan membuat proyek dengan nama shtoree dengan perintah: 
```bash
    pip install -r requirements.txt
   django-admin startproject shtoree .
```
juga memodifikasi file `settings.py`.
- Lalu, saya membuat repo baru di Github dengan nama shtoree dan menghubungkannya dengan direktori lokal menggunakan perintah:
```bash
git branch -M main
git remote add origin https://github.com/maira-shasmeen/shtoree.git
```
- Kemudian, saya menambahkan file `.gitignore` untuk mengabaikan file yang tidak perlu disimpan di Git dan melakukan add, commit, dan push dari direktori repositori lokal.
- Saya melanjutkan dengan membuka PWS (Pacil Web Service) untuk membuat project baru. Saya memodifikasi file settings.py dengan menambahkan URL deployment PWS saya (maira-shasmeen-shtoree.pbp.cs.ui.ac.id) dan melakukan langkah-langkah deployment PWS seperti yang diajarkan di tutorial.
- Selanjutnya, saya membuat aplikasi Django menggunakan perintah:
```bash
python manage.py startapp main
```
dan membuat routing dan persiapan lainnya yang dijelaskan di Tutorial 1. Membuat folder templates di dalam folder main untuk membuat template lalu tambahkan file main.html.
- Setelah itu, saya membuat model pada aplikasi `main` dengan nama `Product`, yang berisi atribut-atribut:
   - name (CharField)
   - price (IntegerField)
   - description` (TextField)
   - size (CharField)
- Lalu, saya buat fungsi di `views.py`dia mengambil data dari model dan mengirimkan ke template untuk ditampilkan, variabel yang saya gunakan antara lain:
    - 'nama_aplikasi'
    - 'nama_mahasiswa'
    - 'nama_kelas'
    - 'name' : nama produk
    - 'price' : harga produk
    - 'description': deskripsi produk
    - 'size': ukuran produk
- Setelah itu, saya memodifikasi file `main.html` dengan Menambahkan judul, nama aplikasi, nama mahasiswa, kelas, foto, juga deskripsi produk yang diambil dari variabel di `views.py`.
- Setelah selesai, saya melakukan push ke PWS dengan perintah berikut:
```bash
   git push pws main:master
```
- Setelah berhasil, websitenya bisa diakses di http://maira-shasmeen-shtoree.pbp.cs.ui.ac.id


3. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html :
```
+----------------------+
| Client (Browser) |
+----------------------+
↓
+----------------------+
| Request (URL: /) |
+----------------------+
↓
+----------------------+
| urls.py (Mencari path '') |
+----------------------+
↓
+----------------------+
| views.py (Fungsi 'show_main' dipanggil) |
+----------------------+
↓
+----------------------+
| models.py |
+----------------------+
↓
+----------------------+
| views.py (Data dikirim ke template) |
+----------------------+
↓
+----------------------+
| HTML Template (main.html) (Menampilkan data produk) |
+----------------------+
↓
+----------------------+
| Response (Halaman web yang berisi informasi) |
+----------------------+
```
- urls.py: Berfungsi untuk memetakan URL yang diminta oleh pemgguna ke fungsi view yang sesuai.
- views.py: Mengambil data dari model (database) dan menyiapkannya untuk ditampilkan di template.
- models.py: Berisi definisi struktur data dan logika yang terkait dengan database.
- HTML Template: Digunakan untuk menampilkan data yang dikirim oleh view dalam bentuk yang bisa dilihat oleh pengguna.

4. Jelaskan fungsi git dalam pengembangan perangkat lunak!
- Setiap perubahan yang dilakukan di kode bisa dilacak, jadi memudahkan kita mengetahui siapa yang mengubah apa.
- Dengan Git, kita bisa bekerja bersama dengan tim dalam satu proyek, menggabungkan kode yang dibuat masing-masing anggota.
- Jika ada kesalahan, kita bisa kembali ke versi kode sebelumnya.
- Bisa membuat cabang (branch) untuk mencoba fitur baru tanpa mengganggu kode utama.

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
- Karena Django ini mudah dipahami, dokumentasonya lengkap dan bisa diikuti. Selain itu Django memiliki banyak fitur jadi kita bisa fokus pada logika aplikasi tanpa harus memikirkan hal-hal dasar. Lalu, Django mendorong kita untuk menulis kode yang bersih dan tidak berulang.

6. Mengapa model pada Django disebut sebagai ORM?
- ORM (Object Relational Mapping) adalah cara Django menghubungkan kode Python dengan database. Dengan ORM Kita bisa berinteraksi dengan database menggunakan objek Python, tanpa perlu menulis SQL yang rumit. Model di Django mewakili tabel di database. Misalnya, model Product akan menjadi tabel di database yang menyimpan produk-produk. ORM memudahkan kita melakukan operasi seperti membuat, membaca, memperbarui, dan menghapus data di database menggunakan kode Python

# Tugas 3 PBP

 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform? :


 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML? :


 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut? :


 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang? :


 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). :


![alt text](<main/images/Screenshot 2024-09-17 at 18.26.03.png>)
![alt text](<main/images/Screenshot 2024-09-17 at 18.25.09.png>)
![alt text](<main/images/Screenshot 2024-09-17 at 18.26.46.png>)
![alt text](<main/images/Screenshot 2024-09-17 at 18.26.52.png>)