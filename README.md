Nama Anggota (tercelup) :
Rahmad Sitanala Putra Baladiah ( 2265061002 ) 
Irham Dinata ( 2115061129 ) 
M. Farel Ghifary Suja (2255061021)

1. Pendahuluan
Laporan ini disusun sebagai hasil kegiatan Quality Assurance (QA) terhadap website Joox. Pengujian dilakukan untuk memastikan bahwa seluruh fitur yang ada pada platform berjalan sesuai dengan spesifikasi yang ditentukan, tanpa adanya bug yang signifikan, serta dapat memberikan pengalaman pengguna yang optimal. Kegiatan QA ini melibatkan pengujian berbagai elemen, termasuk performa, aksesibilitas, kompatibilitas perangkat, dan fungsionalitas fitur utama seperti login, pemutaran lagu, pencarian, serta langganan premium.
Proses pengujian dilakukan dengan menggunakan beberapa pendekatan, termasuk pengujian manual dan otomatis untuk memastikan bahwa hasil yang didapatkan akurat dan dapat diandalkan. Selain itu, pengujian dilakukan pada berbagai perangkat, baik mobile maupun desktop, untuk mengevaluasi responsivitas tampilan dan interaksi pengguna pada berbagai platform. Evaluasi juga mencakup pengujian pada browser yang berbeda untuk memastikan tampilan dan fungsi tetap konsisten di seluruh platform.
Hasil dari pengujian ini akan memberikan wawasan yang mendalam mengenai kinerja website Joox serta area yang perlu diperbaiki untuk meningkatkan kepuasan pengguna dan memastikan layanan yang lebih baik lagi. Laporan ini juga bertujuan untuk memberikan rekomendasi terkait perbaikan atau optimasi yang dapat dilakukan untuk meningkatkan kualitas keseluruhan platform.

2. Tujuan Pengujian
Tujuan utama dari pengujian ini adalah untuk:
- Memastikan fungsi-fungsi utama seperti login, pemutaran lagu, dan langganan premium berjalan baik
- Memastikan website kompatibel di berbagai browser dan perangkat
- Menilai kinerja (performance) dan responsivitas web
- Mengidentifikasi dan mendokumentasikan bug atau error

3. Ruang Lingkup Pengujian
Pengujian mencakup fitur login, browsing musik, pemutaran lagu, langganan premium, pencarian lagu, dan responsivitas. Pengujian dilakukan pada:
- Desktop (Windows 10)
- Mobile (Android dan iOS)
- Browser: Chrome, Firefox, Safari

4. Strategi Pengujian
Pendekatan pengujian meliputi:
- Manual testing untuk fungsionalitas dasar
- Automated testing untuk login dan validasi halaman
- Exploratory testing untuk menemukan bug non-standar
- Compatibility testing pada berbagai browser
- Responsiveness testing pada berbagai resolusi layar
- Performance testing secara terbatas pada waktu akses dan loading

5. Rencana Pengujian (Test Plan)
Jadwal pengujian:
Hari 1: Fitur login, registrasi, validasi
Hari 2: Pemutaran lagu, pencarian, dan UI responsiveness
Hari 3: Langganan premium, kompatibilitas, dan pengujian akhir

6. Lingkungan Pengujian
- Sistem Operasi: Windows 10, Android 13, iOS 17
- Browser: Chrome v113, Firefox v102, Safari iOS
- Koneksi Internet: WiFi 10 Mbps
- Alat Bantu: Chrome DevTools, Selenium, Lighthouse

7. Test Cases dan Eksekusi
TC01 - Login dengan akun valid
Langkah: Input user dan pass, klik login
Hasil Diharapkan: Dashboard muncul
Hasil Aktual: PASS


TC02 - Login dengan akun tidak valid
Langkah: Input data salah, klik login
Hasil Diharapkan: Error message tampil
Hasil Aktual: PASS


TC03 - Streaming lagu
Langkah: Klik lagu dari homepage
Hasil Diharapkan: Lagu diputar
Hasil Aktual: PASS


TC04 - Pencarian lagu
Langkah: Cari “Lagu A” di search bar
Hasil Diharapkan: Lagu A muncul
Hasil Aktual: PASS


TC05 - Langganan premium
Langkah: Bayar via kartu, konfirmasi
Hasil Diharapkan: Akun jadi premium
Hasil Aktual: PASS


TC06 - Cek responsivitas mobile
Langkah: Akses dari ponsel
Hasil Diharapkan: Layout menyesuaikan
Hasil Aktual: PASS


TC07 - Cek UI browser Firefox
Langkah: Buka di Firefox
Hasil Diharapkan: Layout tetap rapi
Hasil Aktual: PASS


8. Script Otomatisasi 
Login (Valid)

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.joox.com/id/login")
driver.find_element('id', 'username').send_keys("test_user")
driver.find_element('id', 'password').send_keys("test_pass")
driver.find_element('id', 'login-button').click()
assert "dashboard" in driver.current_url
driver.quit()

Skrip ini dirancang untuk mengakses halaman login Joox, mengisi informasi login (username dan password), dan mencoba masuk ke dashboard.

Pemutaran Lagu

driver.get("https://www.joox.com/id")
search_box = driver.find_element('name', 'search')
search_box.send_keys("Lagu Favorit")
search_box.submit()
driver.find_element('xpath', '//div[contains(@class,"song-item")][1]').click()
play_button = driver.find_element('class name', 'play-btn')
play_button.click()
assert "playing" in driver.page_source

Pencarian Lagu: Skrip mencari lagu tertentu di Joox dengan kata kunci "Lagu Favorit".
Pemutaran Lagu: Memilih lagu pertama dari hasil pencarian dan memutarnya.
Memvalidasi Pemutaran: Memastikan lagu sedang diputar dengan memeriksa keberadaan indikator seperti kata "playing" pada sumber halaman (HTML).

Langganan Premium

driver.get("https://www.joox.com/id/vip")
driver.find_element('id', 'subscribe-button').click()
driver.find_element('id', 'credit-card-number').send_keys("4111111111111111")
driver.find_element('id', 'expiry-date').send_keys("12/30")
driver.find_element('id', 'cvv').send_keys("123")
driver.find_element('id', 'confirm-payment').click()
assert "Premium Member" in driver.page_source

Skrip ini bertujuan untuk mengotomatisasi proses langganan vip di platform Joox, mulai dari mengklik tombol langganan hingga menyelesaikan pembayaran menggunakan informasi kartu kredit.
Responsivitas Mobile (iPhone X Emulation)

from selenium.webdriver.chrome.options import Options

mobile_emulation = { "deviceName": "iPhone X" }
chrome_options = Options()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.joox.com/id")
assert "Joox" in driver.title
driver.quit()

Skrip ini bertujuan untuk mengotomatisasi pengujian akses halaman utama Joox dalam mode tampilan seluler dengan emulasi perangkat iPhone X. Dengan menggunakan fitur mobile emulation pada Selenium, skrip ini memastikan bahwa halaman utama Joox dapat diakses dengan benar pada perangkat seluler, memvalidasi keberadaan elemen utama seperti judul halaman.

Pencarian Lagu

driver.get("https://www.joox.com/id")
search_box = driver.find_element('name', 'search')
search_box.send_keys("Dewa 19")
search_box.submit()
assert "Dewa 19" in driver.page_source
Skrip ini bertujuan untuk mengotomatisasi proses pencarian artis atau lagu "Dewa 19" di platform Joox, serta memvalidasi bahwa hasil pencarian yang relevan ditampilkan dengan memeriksa keberadaan teks "Dewa 19" dalam sumber halaman.

9. Bug yang Ditemukan
Selama pengujian, tidak ditemukan bug kritikal. Namun, ditemukan satu minor issue:
- Judul lagu kadang tidak muncul sempurna saat diakses dari Safari iOS.

10. Performance 

Mobile:
Performance: 54 (Skor performa rendah): Ini menunjukkan bahwa situs/aplikasi mengalami masalah dalam hal kecepatan atau kinerja pada perangkat mobile, dan perlu dioptimalkan agar pengguna tidak mengalami keterlambatan atau kegagalan saat mengaksesnya.


Accessibility: 85 (Skor aksesibilitas cukup baik): Meskipun skor ini tergolong baik, masih ada ruang untuk meningkatkan aksesibilitas agar lebih inklusif bagi semua pengguna, termasuk mereka yang memiliki disabilitas.


Best Practices: 100 (Skor terbaik): Ini menunjukkan bahwa aplikasi atau situs mematuhi praktik terbaik untuk pengembangan dan penggunaannya pada mobile, yang sangat baik.


SEO: 92 (SEO yang sangat baik): Situs atau aplikasi ini dioptimalkan dengan baik untuk mesin pencari, yang akan membantu lebih banyak orang menemukannya.


Desktop:
Performance: 62 (Skor performa moderat): Skor ini lebih tinggi dari versi mobile, yang menunjukkan bahwa performa desktop situs/aplikasi lebih baik. Namun, masih ada potensi untuk meningkatkan kecepatannya.


Accessibility: 82 (Skor aksesibilitas cukup baik): Di desktop, aksesibilitas juga cukup baik, tetapi ada ruang untuk perbaikan agar lebih ramah pengguna.


Best Practices: 100 (Skor terbaik): Sama seperti pada perangkat mobile, situs/aplikasi ini mengikuti praktik terbaik di desktop, yang sangat positif.


SEO: 77 (Skor SEO cukup baik): SEO desktop sedikit lebih rendah dibandingkan mobile, dan bisa lebih dioptimalkan untuk hasil pencarian yang lebih baik.

11. Kesimpulan
Semua fitur utama berhasil diuji dengan hasil memuaskan. Web Joox terbukti:
- Stabil dan fungsional di semua perangkat utama
- Responsif di berbagai ukuran layar
- Tidak ditemukan bug kritikal