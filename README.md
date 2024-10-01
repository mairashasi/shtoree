**Maira Shasmeen Mazaya 2306245724**

# Tugas 2 PBP

 **1. Tautan menuju aplikasi PWS = http://maira-shasmeen-shtoree.pbp.cs.ui.ac.id**

 **2. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step :**
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
 - Dilanjutkan dengan membuka PWS untuk membuat project baru. Saya memodifikasi file settings.py dengan menambahkan URL deployment PWS saya (maira-shasmeen-shtoree.pbp.cs.ui.ac.id) dan melakukan langkah-langkah deployment PWS seperti yang diajarkan di tutorial.
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
  - Setelah itu, saya memodifikasi file `main.html` dengan Menambahkan judul, nama aplikasi, nama mahasiswa, kelas, foto,  juga deskripsi produk yang diambil dari variabel di `views.py`.
 - Setelah selesai, saya melakukan push ke PWS dengan perintah berikut:
 ```bash
   git push pws main:master
 ```
 - Setelah berhasil, websitenya bisa diakses di http://maira-shasmeen-shtoree.pbp.cs.ui.ac.id


 **3. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html :**
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

 **4. Jelaskan fungsi git dalam pengembangan perangkat lunak! :**
 - Setiap perubahan yang dilakukan di kode bisa dilacak, jadi memudahkan kita mengetahui siapa yang mengubah apa.
 - Dengan Git, kita bisa bekerja bersama dengan tim dalam satu proyek, menggabungkan kode yang dibuat masing-masing anggota.
 - Jika ada kesalahan, kita bisa kembali ke versi kode sebelumnya.
 - Bisa membuat cabang (branch) untuk mencoba fitur baru tanpa mengganggu kode utama.

 **5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak? :**
 - Karena Django ini mudah dipahami, dokumentasonya lengkap dan bisa diikuti. Selain itu Django memiliki banyak fitur jadi kita bisa fokus pada logika aplikasi tanpa harus memikirkan hal-hal dasar. LalU Django mendorong kita untuk menulis kode yang bersih dan tidak berulang. :**

 **6. Mengapa model pada Django disebut sebagai ORM? :**
 - ORM (Object Relational Mapping) adalah cara Django menghubungkan kode python dengan database. Dengan ORM Kita bisa berinteraksi dengan database menggunakan objek python, tanpa perlu menulis SQL yang rumit. Model di Django mewakili tabel di database. Misalnya, model Product akan menjadi tabel di database yang menyimpan produk-produk. ORM memudahkan kita melakukan operasi seperti membuat, membaca, memperbarui, dan menghapus data di database menggunakan kode python

# Tugas 3 PBP

 **1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform? :**
 - Data delivery sangat penting dalam pengimplementasian platform karena memastikan data dapat ditransfer dengan lancar dan efisien antar komponen platform, seperti antara frontend dan backend, atau antar microservices. Ini memungkinkan informasi dapat diakses secara real time, meningkatkan performa dan pengalaman pengguna. Selain itu data delivery juga mendukung skalabilitas, keamanan, serta mempermudah analisis data yang krusial dalam memastikan platform dapat berkembang sesuai kebutuhan.

 **2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML? :**
 - JSON lebih populer dibandingkan XML karena formatnya lebih sederhana dan mudah dibaca. JSON juga lebih cepat dalam parsing data dan memiliki ukuran file yang lebih kecil sehingga lebih efisien untuk digunakan dalam aplikasi web dan API. Selain itu JSON lebih fleksibel karena mendukung banyak tipe data dengan struktur yang mudah dipahami oleh hampir semua bahasa pemrograman. Sementara XML lebih cocok untuk menangani data kompleks, namun JSON lebih banyak digunakan karena kesederhanaannya dan kemampuannya dalam mempercepat transmisi data.

 **3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut? :**
 - Method is_valid() di Django sangat membantu untuk memastikan data yang dimasukkan ke form sudah benar. Dengan is_valid(), kita bisa memeriksa apakah semua field telah diisi dengan benar dan menampilkan pesan error jika ada yang salah. Ini penting karena mencegah data yang tidak sesuai atau berpotensi berbahaya masuk ke sistem kita, sehingga kita bisa menjaga keamanan dan kualitas data yang masuk.


 **4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang? :**
 - csrf_token adalah cara Django untuk melindungi aplikasi dari serangan yang memungkinkan penyerang mengirim permintaan berbahaya atas nama pengguna yang sudah login. Jika kita tidak menggunakan csrf_token maka penyerang bisa memanfaatkan kelemahan ini untuk mengirimkan permintaan palsu dan mengambil tindakan atas nama pengguna, seperti mengubah data atau melakukan tindakan yang tidak diinginkan. Dengan menambahkan csrf_token kita bisa memastikan bahwa setiap permintaan form berasal dari pengguna yang benarbenar mengirimnya, bukan dari sumber yang berbahaya.

 **5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). :**
 - Pertama saya buat base.html yang berisi kerangka css untuk mendesain komponen website. Base ini akan dijadikan dasar untuk semua tampilan lainnya. Saya juga melakukan modifikasi di main.html (mengedit design serta menyesuaikan dengan base.html) dan settings.py tepatnya di bagian TEMPLATES, saya menambahkan :       
 ```bash
 'DIRS': [BASE_DIR / 'templates'], 
 ```
 untuk memastikan konfigurasi base.html terdeteksi sebagai berkas template.
 - Setelah itu, saya memodifikasi models.py dan mengimport uuid. Dimodifikasi menjadi:
 ```bash
 class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    name = models.CharField(max_length=255)  
    price = models.IntegerField()  
    feedback = models.TextField()  
    rating = models.IntegerField(default=0)  
 ``` 
 dan menjalankan perintah migrate.
 - Langkah berikutnya adalah membuat form dengan membuat file forms.py yang mendefinisikan model Product beserta fieldnya seperti name, price, feedback, dan rating. Setelah itu, saya memodifikasi views.py dengan mengimpor ProductForm dan Product, serta menambahkan fungsi create_product_rating yang menggunakan form ini untuk menambahkan rating produk.
 - Lalu saya memodifikasi fungsi show_main di views.py untuk mengambil semua data produk yang tersimpan di database dengan menggunakan Product.objects.all(). Kemudian saya menambahkan data ini ke context dalam bentuk product_rating agar bisa ditampilkan di template.
 - Selanjutnya, saya memodifikasi urls.py dengan mengimpor fungsi create_product_entry dari views.py dan menambahkan path baru di urlpatterns seperti path('create-product-rating', create_product_rating, name='create_product_rating').
 - Lalu saya membuat file create_product_rating.html di dalam folder main/templates yang berisi form untuk menambah raating produk. Form ini memungkinkan pengguna memasukkan data produk yang kemudian akan ditampilkan di halaman utama.
 - Di dalam main.html, saya menambahkan kode untuk menampilkan produkproduk yang diinput ke dalam database. Produk-produk ini ditampilkan di dalam box deskripsi, sesuai dengan data yang ada di database.
 - Kemudian saya menambahkan fungsi show_xml di views.py, yang gunain HttpResponse dan Serializer untuk mengembalikan data produk dalam format XML. Fungsi ini ditambahkan ke urls.py dengan path yang sesuai.
 - Langkah yang sama juga dilakukan untuk menampilkan data dalam format JSON. Saya membuat fungsi show_json di views.py dan menambahkan path-nya di urls.py.
 - Lalu saya menambahkan dua fungsi baru lagi yaitu show_xml_by_id dan show_json_by_id, yang menerima parameter ID untuk mengembalikan data spesifik berdasarkan ID dalam format XML dan JSON. Saya juga menambahkan path untuk kedua fungsi ini di urls.py.
 - Disini saya sudah memiliki lima fungsi baru di views.py: create_product_rating, show_xml, show_json, show_xml_by_id, dan show_json_by_id, serta path URL baru di urls.py. Sehingga sekarang sudah bisa menerima input produk baru melalui form, menampilkan data di halaman utama, serta menyediakan data dalam format XML dan JSON, baik untuk seluruh produk maupun berdasarkan ID.

**Screenshot akses URL pada Postman**
- XML :
![XML](./main/images/XML.png)
- JSON :
![JSON](./main/images/JSON.png)
- XML by ID :
![XML by ID](./main/images/XMLID.png)
 JSON by ID :
![JSON by ID](./main/images/JSONID.png)

# Tugas 4 PBP
 **1. Apa perbedaan antara HttpResponseRedirect() dan redirect() :**
 - Perbedaannya adalah HttpResponseRedirect() itu fungsi yang perlu secara manual diarahkan ke URL, jadi harus memasukkan URL nya lengkap secara langsung. Sedangkan jika menggunakan redirect() bisa lebih fleksibel karena dia bisa menerima URL, nama view, atau instance model sebagai argumen, dan nanti Django yang akan menyelesaikan URLnya secara otomatis. Intinnya redirect() lebih mudah dan fleksibel, sementara HttpResponseRedirect() butuh URL secara langsung.
 
 **2. Jelaskan cara kerja penghubungan model Product dengan User! :**
- Untuk menghubungkan model Product (produk) dengan User (pengguna), kita menggunakan ForeignKey. Ini berarti bahwa setiap produk terhubung ke satu pengguna. Dengan kata lain satu pengguna bisa memiliki banyak produk, tetapi satu produk hanya dimiliki oleh satu pengguna.

 **3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut. :**
- Authentication adalah proses memverifikasi identitas pengguna, yaitu memastikan bahwa pengguna yang mengklaim identitas tertentu benar-benar adalah orang yang dimaksud. Misalnya, saat pengguna memasukkan username dan password, sistem memeriksa apakah kombinasi ini valid.
- Authorization adalah proses memeriksa apakah pengguna yang sudah masuk (login) diizinkan untuk mengakses fitur tertentu. Misalnya, setelah login, pengguna hanya bisa mengakses halaman yang diizinkan untuknya.
- Saat pengguna login, Django akan memverifikasi username dan password yang diberikan. Jika valid, Django akan mengotentikasi pengguna dan mencatat status login mereka, yang memungkinkan pengguna tersebut mengakses area yang dilindungi otorisasi.
- Implementasi di Django:
  - Authentication: Gunakan fungsi authenticate() dan login() untuk memeriksa username dan password. Jika cocok, pengguna bisa login.
  - Authorization: Django menggunakan @login_required untuk membatasi halaman tertentu hanya bagi pengguna yang sudah login.

 **4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan? :**
- Django menggunakan session untuk mengingat pengguna. Setelah login, Django membuat session ID dan mengirimkannya ke browser sebagai cookie. Saat pengguna kembali ke situs, session ID tersebut dikirim kembali ke server untuk mengidentifikasi bahwa pengguna sudah login.
- Cara kerja:
  - Setelah login, Django menyimpan informasi sesi di server.
  - Session ID dikirim ke browser pengguna sebagai cookie.
  - Setiap kali pengguna mengunjungi halaman lain, session ID ini membantu Django mengenali pengguna tersebut.
- Kegunaan lain dari cookies:
  - Menyimpan preferensi pengguna: Misalnya, bahasa yang dipilih, atau tema situs.
  - Menyimpan data sementara: Seperti status keranjang belanja dalam e-commerce.
  - Pelacakan aktivitas: Digunakan untuk pelacakan aktivitas pengguna di situs (misalnya, untuk iklan).
- Apakah semua cookies aman digunakan? Tidak semua cookies aman. Cookies bisa disalahgunakan jika tidak dienkripsi atau dilindungi dengan benar. Serangan seperti pencurian sesi (session hijacking) bisa terjadi jika cookies dicuri oleh pihak lain. Oleh karena itu, Django menerapkan keamanan cookies dengan menambahkan atribut seperti `HttpOnly` (Mencegah akses cookies dari JavaScript.) & `Secure` (Memastikan cookies hanya dikirim melalui koneksi HTTPS yang aman.)

 **5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). :**
- pertama, saya menambahkan import pada views.py :
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

- kedua, saya menambahkan fungsi register untuk menghasilkan formulir registrasi secara otomatis dan menghasilkan akun pengguna ketika data di-submit dari form.

- lalu, saya menambahkan berkas html baru yaitu register.html pada main/templates, menambahkan import fungsi yang tadi sudah dibuat (from main.views import register), dan menambahkan path url ke dalam urlpatterns

- keempat, saya membuat fungsi login, jadi di view.py ditambahin import lagi:
```bash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
```
serta nambahin fungsi login_user untuk mengautentikasi pengguna yang ingin login.

- lalu , saya menambahkan lagi berkas html baru yaitu login.html pada main/templates, menambahkan import fungsi yang tadi sudah dibuat (from main.views import login_user), dan menambahkan path url ke dalam urlpatterns

- keenam, saya membuat fungsi logout, jadi saya menambahkan import dulu di view.py:
```bash
from django.contrib.auth import logout
```
kemudian menambahkan fungsi logout_user(request) dan pada main.html ditambah sebuah kode:
```bash
<a href="{% url 'main:logout' %}">
  <button>Logout</button>
</a>
```
dan pada urls.py tambahkan import fungsi yang tadi sudah dibuat (from main.views import logout_user), dan menambahkan path url ke dalam urlpatterns

- ketujuh, saya buka lagi views.py dan nambahkan import login_required pada bagian paling atas. dan menambahlkan @login_required(login_url='/login') diatas def show_main(request).

- Lanjut saya mensetup cookies untuk melihat data, saya menambahkan import untuk HttpResponseRedirect, reverse, dan datetime di file views.py. Selanjutnya, saya memodifikasi fungsi login_user pada blok if form.is_valid(), yang bertugas untuk melakukan login terlebih dahulu, membuat respons, dan menambahkan cookie last_login ke dalam respons tersebut. Kemudian, saya menambahkan variabel 'last_login': request.COOKIES['last_login'] ke dalam context agar informasi cookie last_login bisa terlihat di web. Selain itu, saya juga memodifikasi fungsi logout_user untuk menghapus cookie last_login saat pengguna melakukan logout. Saya kemudian menambahkan kode terkait last_logindi main.html agar informasi cookie tersebut bisa ditampilkan di aplikasi web saya.

- Lalu, Untuk menghubungkan Model Product dengan User, saya mulai dengan import User ke dalam models.py. Kemudian, pada model product yang sudah ada, saya menambahkan baris kode seperti user = models.ForeignKey(User, on_delete=models.CASCADE) untuk menghubungkan setiap produk dengan satu pengguna melalui relasi. Setiap produk pasti terasosiasi dengan seorang pengguna.
Setelah itu, saya membuka views.py dan memodifikasi fungsi create_product_rating sesuai panduan tutorial. Perubahan ini dilakukan agar objek dari form bisa disimpan ke dalam akun pengguna yang sedan login.

- Saya juga memodifikasi nilai product_rating agar aplikasi hanya menampilkan objek produk yang terkait dengan pengguna yang sedang login, serta menambahkan ke dalam context 'name': request.user.username, untuk menampilkan nama pengguna yang sedang login.

- Setelah semua perubahan, saya menjalankan perintah makemigrations dan migrate sesuai langkah-langkah yang ada di tutorial. Terakhir, saya membuka settings.py untuk mengimpor os dan mengubah variabel DEBUG menjadi PRODUCTION = os.getenv("PRODUCTION", False) dan DEBUG = not PRODUCTION.

- Setelah semua selesai, baru saya edit untuk tampilan’’ html nnya.

# Tugas 5 PBP
 **1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut! :** 
 - Ketika ada beberapa aturan CSS selector yang diterapkan pada elemen yang sama, browser akan memilih aturan yang paling spesifik untuk diterapkan. Urutan prioritasnya adalah sebagai berikut: Pertama, Inline CSS, yaitu gaya yang langsung ditulis di dalam elemen HTML seperti `<div style="color: red;"></div>`, merupakan prioritas tertinggi. Kedua, ID Selector yang menggunakan ID elemen seperti `#my-id { color: blue; }`, memiliki prioritas tinggi karena ID sifatnya unik. Ketiga, Class Selector dan Pseudo-class yang menggunakan class atau pseudo-class seperti `.my-class { color: green; } atau :hover`. Dan keempat, Element Selector, yang langsung mengatur gaya untuk elemen HTML tertentu seperti `p { color: black; }` untuk semua elemen paragraf. 

 **2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design! :**
 - Responsive design adalah konsep penting dalam pengembangan web karena memungkinkan situs untuk menyesuaikan tampilannya dengan baik di berbagai ukuran layar, seperti ponsel, tablet, dan desktop. Hal ini penting karena semakin banyak orang yang mengakses internet melalui perangkat mobile, sehingga situs yang tidak responsif bisa terlihat berantakan dan sulit digunakan di layar kecil. Desain yang responsif juga meningkatkan pengalaman pengguna (user experience), karena situs menjadi lebih nyaman digunakan di berbagai perangkat. Selain itu, SEO juga terpengaruh, karena mesin pencari seperti Google memberikan peringkat lebih baik untuk situs yang responsif. Contoh aplikasi yang sudah menerapkan responsive design adalah Spotify, yang tampak rapi dan mudah digunakan di perangkat apa pun. Sebaliknya, beberapa situs lama yang belum diperbarui mungkin masih memiliki tampilan yang hanya bagus di desktop dan sulit digunakan di ponsel.

 **3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut! :**
 - Dalam CSS, margin, border, dan padding adalah tiga properti yang digunakan untuk mengatur jarak dan ruang di sekitar dan di dalam elemen HTML. Margin adalah jarak antara elemen dengan elemen lain di sekitarnya. Misalnya, jika sebuah elemen memiliki `margin: 20px;`, maka elemen tersebut akan memiliki jarak 20px dari elemen lain di sekitarnya. Border adalah garis yang mengelilingi elemen, yang berada di antara margin dan padding. Dengan `border: 2px solid black;`, elemen tersebut akan memiliki garis hitam di sekelilingnya. Padding adalah ruang di dalam elemen, yaitu jarak antara konten elemen dengan batas border-nya. Jika elemen memiliki `padding: 10px;`, maka konten elemen tersebut akan memiliki ruang 10px dari tepi border. Singkatnya, margin adalah ruang luar, border adalah bingkai, dan padding adalah bantalan gt di dalam elemen.

 **4. Jelaskan konsep flex box dan grid layout beserta kegunaannya! :** 
 - Flexbox adalah metode layout dalam CSS yang digunakan untuk menyusun elemen secara fleksibel dalam satu baris atau kolom. Flexbox sangat berguna ketika kamu ingin menyusun elemen dengan cara yang responsif, karena elemen bisa menyesuaikan diri dengan ruang yang tersedia. Misalnya, Flexbox sering digunakan untuk membuat navigasi horizontal atau kolom yang bisa beradaptasi dengan ukuran layar. Di sisi lain, Grid Layout adalah metode layout yang lebih kompleks dan digunakan untuk menyusun elemen dalam dua dimensi, yaitu baris dan kolom. Grid sangat berguna untuk tata letak halaman yang lebih rumit, seperti membuat halaman dengan sidebar, konten utama, dan footer yang diatur dalam beberapa kolom. Flexbox lebih cocok digunakan untuk tata letak yang sederhana dalam satu arah (horizontal atau vertikal), sedangkan Grid Layout lebih tepat untuk tata letak yang lebih kompleks dan melibatkan banyak elemen dalam beberapa baris dan kolom.
 - Flexbox dan Grid adalah dua alat yang sangat berguna untuk membangun layout web yang responsif dan rapi. Flexbox memberikan fleksibilitas dalam menyusun elemen secara horizontal atau vertikal, sementara Grid menawarkan kontrol penuh untuk menyusun elemen dalam bentuk baris dan kolom.

 **5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)! :**
 - Pertama, saya menambahkan fitur Edit Product Rating. Saya membuat fungsi edit_product_rating di views.py untuk mengambil data product rating berdasarkan ID dan menggunakan ProductForm untuk mengedit data tersebut. Setelah itu, saya menambahkan HttpResponseRedirect dan reverse untuk mengarahkan kembali ke halaman utama setelah form disimpan. Saya juga membuat file edit_product_rating.html dan menambahkan path URL di urls.py untuk mengakses fungsi edit ini. Selanjutnya, saya menambahkan tombol Edit di main.html agar pengguna bisa mengedit rating produk.
  - Kedua, saya menambahkan fitur delete product rating. Saya membuat fungsi delete_product_rating di views.py untuk menghapus rating produk berdasarkan ID dan menambahkan path URL di urls.py. Setelah itu, saya memodifikasi main.html dengan menambahkan tombol delete sehingga pengguna dapat menghapus data product rating.
  - Ketiga, saya menambahkan Navigation Bar. Saya membuat file navbar.html yang berisi link navigasi untuk "Home", "Description", "Categories", serta menambahkan tombol Logout. Saya memasukkan navbar ini ke dalam base.html agar muncul di semua halaman.
  - Keempat, saya mengatur Static Files. Saya mengkonfigurasi settings.py dengan menambahkan WhiteNoiseMiddleware untuk menangani file statis dan mengatur STATIC_URL, STATICFILES_DIRS, dan STATIC_ROOT.
  - Kelima, saya menambahkan Tailwind CSS untuk mengubah tampilan form di login.html, register.html, dan create_product_rating.html, sehingga desain menjadi lebih responsif juga modern.
  - Keenam, saya membuat Card untuk product rating. Saya membuat file card_rating.html untuk menampilkan setiap product rating dalam bentuk card, dengan tombol edit dan delete di setiap card. Saya juga membuat card_info.html yang isinya adalah nama mahasiswa, kelas, dan aplikasi.
  - Terakhir, saya mengintegrasikan semua komponen di dalam main.html, termasuk navbar, card untuk product rating, card info, dan tombol edit serta delete. Ini memastikan semua fitur berfungsi dengan baik dan tampil secara terintegrasi di aplikasi. Serta juga mengedit-edit lagi html hingga finalll.