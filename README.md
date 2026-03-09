# Kitap Stok Takip Sistemi | Book Stock Tracker

## TR - Kısa Bilgilendirme
Python tabanlı bu uygulama ile kitap stoklarını SQLite veritabanında takip edebilirsiniz.  
GUI (PyQt5) ve komut satırı arayüzü birlikte sunulur.

### Hızlı Özellikler
- Kitap ekleme, listeleme, arama, düzenleme, silme
- Barkod bazlı tekilleştirme
- Excel içe aktarma (`.xlsx`) ve dışa aktarma
- Kayıt ve güncelleme tarihi takibi

### Hızlı Kurulum
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Çalıştırma
```bash
python gui.py          # Grafik arayüz
python kitap_stok.py   # Komut satırı menüsü
python test.py         # Bağımlılık kontrolü
```

## EN - Quick Info
This Python app tracks book inventory in an SQLite database.  
It provides both a PyQt5 GUI and a CLI menu.

### Quick Features
- Add, list, search, update, delete books
- Barcode-based unique records
- Excel import/export (`.xlsx`)
- Created/updated timestamp tracking

### Quick Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Run
```bash
python gui.py          # GUI
python kitap_stok.py   # CLI menu
python test.py         # Dependency check
```
