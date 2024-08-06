# kitap_stok_takip_py
 Paython ile kitap stok takibi yapabileceğmiz basit bir veritabanı yapıyoruz.

 ### Çalışan İşlemler
 
 #### 1- Kitap Ekle
 #### 2- Kitaplari Listele
 #### 3- Kitap Ara(Barkoda göre)
 #### 4- Tüm verileri sil(Bir hata alınca böyle bir şey ekleme gereği duydum.)
 #### 5- Seçili veriyi sil (barkod'a göre)

 ### Eklemeyi Planladıklarım:

 #### 1- Yazar Adi
 ###### Güncellemeyle Eklendi (03.07.24)
 #### 2- Veri Güncelle
 ###### Üzerinde çalışılıyor
 ###### Şuan için kullanılabilir, tarih bilgisi üzerinde düşünülüyor.(05.07.24)
 #### 3- Excel'e aktar
 ###### Şuan için bu seçnek çalışıyor. Test aşamasında. (06.07.2024)
 #### 4- Excel'e aktarılmış bir veriyi ya da Excel tablosunu veritabanına aktarma.
 ###### Bu işlem sayesinde büyük verileri yani tabloları kolay bir şekilde vt'ye aktarılabilir. (Planlanan. Aktif değil.)
 ###### Yukarıdaki fikri uygulamaya koyduk. Şuan için test aşamasında ama çalışıyor. Yapılması gerekenleri aşağıda belirtiyorum. (26.07.2024) <-- Güncelleme Yapıldı -->

 ## Excel dosyasından veritabanına veri eklemek için yapılması gerekenler.

 #### Exdel veritabanına veri aktarmak için öncelikle bazı kurulumları yenilememiz gerecek.
 #### 1- pip install openpyxl [Bu eklentiyi kuruyoruz, mevcutsa güncelliyoruz.]
 #### 2- pip install pandas [Bu eklentiyi kuruyoruz, mevcutsa güncelliyoruz.]
 #### 3- Excel dosyamızının uzantısı .xlsx olacak.
 #### 4- Excel dosyamızın konumu python dosyalarımızın içinde yani ana klasörümüzde yer alacak.
 #### 5- Excel dosyamızdaki sütun başlıklarımız veritabanı başlıklarıyla aynı olmalı.
 ##### [kitap_adi, kitap_yazar, kitap_barkod, kitap_stok, kayit_tarihi] şeklinde.
 #### 6- Tarih-saat sütunu şimdilik boş kalmalı. Veritabanıyla uyum sorunu için güncelleme yapılacak.
 #### 7- Excel dosyasının adı mevcut veritabanı excel dosyasıyla aynı olmasın. Her seferinde farklı isimle kayıt alın.

 # --> Yeni Güncelleme
 
## Uygulamaya arayüz kazandırmak için kurulması gereken paketler. (07.08.2024)

### Python ile yazdığımız bu programı artık terminal ekranında işlem yapmadan Windwos ve Mac işletim sistemlerinde çalıştırabileceğiniz bir arayüz geliştiriyorum.
### Arayüzü başlatmak için IDE'nizde "gui.py" dosyasından çalıştırısanız program yeni bir pencerede açılacaktır.
### Terminal ekranında çalışmak için "kitap_stok.py" dosyasıyla çalışmaya devam edebilirsiniz.

 #### 1- pip install PyQt5
 #### 2- pip install pyinstaller
 #### 3- pyinstaller --onefile --windowed gui.py
 #### 4- Python versiyonunuzun güncel olduğundan emin olun.
 #### 5- Kullandığınız IDE'nin güncel olduğundan ve kurulu paketlerinizin güncel olduğundan emin olun.




 
 
