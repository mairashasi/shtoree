1. Tautan menuju aplikasi PWS = http://maira-shasmeen-shtoree.pbp.cs.ui.ac.id

2. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step :
- Pertama, 

3. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html :
- 
Client (Browser)
    ↓
Request (URL: /products/)
    ↓
urls.py (Mencari path 'products/')
    ↓
views.py (Fungsi 'show_products' dipanggil)
    ↓
models.py (Mengambil data dari database menggunakan Product.objects.all())
    ↓
views.py (Data dikirim ke template)
    ↓
HTML Template (products.html) (Menampilkan data produk)
    ↓
Response (Halaman web yang berisi daftar produk)
- urls.py: Berfungsi untuk memetakan URL yang diminta oleh client ke fungsi view yang sesuai.
- views.py: Mengambil data dari model (database) dan menyiapkannya untuk ditampilkan di template.
- models.py: Berisi definisi struktur data (model) dan logika yang terkait dengan database. Dalam contoh ini, model Product digunakan untuk menyimpan informasi produk.
- HTML Template: Digunakan untuk menampilkan data yang dikirim oleh view dalam bentuk yang bisa dilihat oleh pengguna (misalnya, daftar produk di halaman).

4. Jelaskan fungsi git dalam pengembangan perangkat lunak!
- Setiap perubahan yang dilakukan di kode bisa dilacak, sehingga memudahkan kita mengetahui siapa yang mengubah apa.
- Dengan Git, kita bisa bekerja bersama dengan tim dalam satu proyek, menggabungkan (merge) kode yang dibuat masing-masing anggota.
- Jika ada kesalahan, kita bisa kembali ke versi kode sebelumnya.
- Bisa membuat cabang (branch) untuk mencoba fitur baru tanpa mengganggu kode utama.

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
- Karena Django ini mudah dipahami, dokumentasonya lengkap dan bisa diikuti. Selain itu Django sudah memiliki banyak fitur jadi kita bisa fokus pada logika aplikasi tanpa harus memikirkan hal-hal dasar. Lalu, Django mendorong kita untuk menulis kode yang bersih dan tidak berulang, mengikuti prinsip DRY (Don't Repeat Yourself).

6. Mengapa model pada Django disebut sebagai ORM?
- ORM (Object-Relational Mapping) adalah cara Django menghubungkan kode Python dengan database. Dengan ORM:
Kita bisa berinteraksi dengan database menggunakan objek Python, tanpa perlu menulis SQL yang rumit.
Model di Django mewakili tabel di database. Misalnya, model Product akan menjadi tabel di database yang menyimpan produk-produk.
ORM memudahkan kita melakukan operasi seperti membuat, membaca, memperbarui, dan menghapus data di database menggunakan kode Python