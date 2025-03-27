# Kitap Stok Takip Sistemi

Kitap Stok Takip Sistemi, Python kullanılarak geliştirilmiş, kitapların veritabanı üzerinden takip edilebildiği, ekleme, listeleme, arama, güncelleme ve silme işlemlerinin gerçekleştirilebildiği bir uygulamadır. Uygulama ayrıca Excel dosyalarıyla veri içe ve dışa aktarımını destekler.

## Özellikler

- **Kitap Ekleme:** Kitap adı, yazar, barkod ve stok bilgilerini girerek yeni kayıt ekleme.
- **Kitap Listeleme:** Veritabanındaki kitapların liste halinde görüntülenmesi.
- **Kitap Arama:** Belirli bir barkod girilerek kitap arama.
- **Kitap Güncelleme:** Seçili kitabın bilgilerini güncelleme.
- **Kitap Silme:** Seçili kitabı veya tüm kayıtları silme.
- **Excel Entegrasyonu:** Excel dosyalarından veri içe aktarımı ve veritabanındaki verilerin Excel'e aktarılması.
- **Grafiksel Kullanıcı Arayüzü:** PyQt5 kullanılarak modern ve kullanıcı dostu bir arayüz sağlanmıştır.
- **Komut Satırı Arayüzü:** `kitap_stok.py` modülü üzerinden konsol tabanlı menü ile de işlem yapma imkanı.

## Gereksinimler

- **Python 3.x** (Önerilen: Python 3.7+)
- **PyQt5:** Grafiksel arayüz oluşturmak için  
  `pip install PyQt5`
- **pandas:** Excel işlemleri ve veri manipülasyonu için  
  `pip install pandas`
- **openpyxl:** Excel dosyalarıyla çalışmak için  
  `pip install openpyxl`
- **SQLite:** Python’un standart kütüphanesi içinde bulunan `sqlite3` modülü kullanılır

## Kurulum Adımları

1. **Projeyi İndirin:**

   GitHub deposunu klonlayarak proje dizinine geçin:
   ```bash
   git clone https://github.com/osmanesad/kitap_stok_takip_py.git
   cd kitap_stok_takip_py
Sanal Ortam Oluşturma (Opsiyonel):

2. **Projeye özel bir sanal ortam oluşturmak için:**

```bash
python -m venv venv
Linux/Mac:

```bash
source venv/bin/activate
Windows:

```bash
venv\Scripts\activate

3. **Gerekli Paketleri Yükleyin:**

Eğer proje kök dizininde requirements.txt dosyası varsa:

`pip install -r requirements.txt

Aksi halde, aşağıdaki komutlarla bağımlılıkları yükleyin:

`pip install PyQt5 pandas openpyxl

4. **Kullanım**

Grafiksel Arayüz (GUI)

Grafiksel kullanıcı arayüzü ile çalıştırmak için:

`python gui.py

Uygulama açıldığında, kitap ekleme için gerekli alanlar (Kitap Adı, Yazar, Barkod, Stok) ve ilgili butonlar yer alır.

Liste, arama, düzenleme, silme ve Excel işlemleri için ayrı butonlar mevcuttur.

Tüm işlemler, PyQt5 tabanlı modern ve kullanıcı dostu bir arayüz üzerinden gerçekleştirilir.

5. **Komut Satırı Arayüzü**

Alternatif olarak, konsol tabanlı menü üzerinden işlem yapmak için:

`python kitap_stok.py

Komut satırı arayüzünde menü seçenekleri ile kitap ekleme, listeleme, arama, güncelleme, silme, Excel'e aktarma ve içe aktarma işlemleri yapılabilir.

Menüde listelenen numaralı seçeneklerden istediklerinizi seçerek işlemlerinizi gerçekleştirebilirsiniz.

6. **Veritabanı**

Uygulama, proje dizininde kitaplar.db adında bir SQLite veritabanı dosyası oluşturur.

Veritabanı ilk çalıştırmada kitaplar adında bir tablo oluşturur. Bu tablo; kitap adı, yazar, barkod, stok, kayıt tarihi ve (opsiyonel) güncelleme tarihi sütunlarını içerir.

7. **Excel Entegrasyonu**
Verileri İçe Aktarma: Belirtilen Excel dosyasındaki verileri veritabanına aktarır.

Verileri Excel'e Aktarma: Veritabanındaki tüm kayıtları belirtilen Excel dosyasına yazar.

Excel işlemleri için pandas ve openpyxl kütüphaneleri kullanılır.

8. **Sorun Giderme**

Bağımlılık Hataları:
Gerekli paketlerin yüklendiğinden emin olun (pip install PyQt5 pandas openpyxl).

Veritabanı Hataları:
Eğer veritabanı dosyasında sorun yaşıyorsanız, dosyayı silip uygulamayı yeniden çalıştırmayı deneyin.

Excel İşlemleri:
Excel içe/dışa aktarma işlemleri sırasında hata alırsanız, dosya adının ve formatının doğru olduğundan emin olun.

9. **Katkıda Bulunma**
Herhangi bir hata bildirimi, geliştirme önerisi veya katkıda bulunmak için lütfen GitHub üzerinden issue açın veya pull request gönderin.
