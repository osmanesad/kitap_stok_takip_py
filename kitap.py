import sqlite3
from datetime import datetime



def veritabani_olustur():
    conn = sqlite3.connect('kitaplar.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS kitaplar
                      (id INTEGER PRIMARY KEY,
                       kitap_adi TEXT,
                       kitap_yazar TEXT,
                       kitap_barkod TEXT UNIQUE,
                       kitap_stok INTEGER,
                       guncelleme_tarihi TEXT,
                       kayit_tarihi TEXT)''')
    conn.commit()
    conn.close()

def guncelle_veritabani_semasi():
    conn = sqlite3.connect('kitaplar.db')
    cursor = conn.cursor()
    try:
        cursor.execute("ALTER TABLE kitaplar ADD COLUMN guncelleme_tarihi TEXT")
        print("Veritabanı şeması güncellendi: guncelleme_tarihi sütunu eklendi.")
    except sqlite3.OperationalError:
       print("Veritabanı bağlantısı başarılı.") #kayit_tarihi sütünü hatasını yakalamak için.
    conn.commit()
    conn.close()

def kitap_ekle(kitap_adi, kitap_yazar, kitap_barkod, kitap_stok):
    conn = sqlite3.connect('kitaplar.db')
    cursor = conn.cursor()
    kayit_tarihi = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        cursor.execute("INSERT INTO kitaplar (kitap_adi, kitap_yazar, kitap_barkod, kitap_stok, kayit_tarihi, guncelleme_tarihi) VALUES (?, ?, ?, ?, ?, ?)",
                       (kitap_adi, kitap_yazar, kitap_barkod, kitap_stok, kayit_tarihi, None))
        conn.commit()
        print("Kitap başarıyla eklendi.")
    except sqlite3.Error as e:
        print("Bu barkod numarası zaten mevcut. Lütfen farklı bir barkod kullanın.")
        print(f"Hata kodu: {e}")
    finally:
        conn.close()

def kitaplari_listele():
    conn = sqlite3.connect('kitaplar.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM kitaplar")
    kitaplar = cursor.fetchall()
    conn.close()
    
    if len(kitaplar) == 0:
        print("Veritabanında kitap bulunamadı.")
    else:
        for kitap in kitaplar:
            print(f"\n >>ID: {kitap[0]}, \nKitap Adı: {kitap[1]}, \nKitap Yazarı: {kitap[2]}, \nBarkod: {kitap[3]}, \nStok: {kitap[4]}, \nKayıt Tarihi: {kitap[5]}, \nGüncelleme Tarihi: {kitap[6] if kitap[6] else '-'}\n")

def kitap_ara(barkod):
    conn = sqlite3.connect('kitaplar.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM kitaplar WHERE kitap_barkod = ?", (barkod,))
    kitap = cursor.fetchone()
    conn.close()
    
    if kitap:
        print(f"ID: {kitap[0]}, Kitap Adı: {kitap[1]}, Kitap Yazarı: {kitap[2]}, Barkod: {kitap[3]}, Stok: {kitap[4]}, Kayıt Tarihi: {kitap[5]}, Güncellenme Tarihi: {kitap[6] if kitap[6] else 'Yeni güncelleme yok.'}")
    else:
        print("Bu barkoda sahip kitap bulunamadı.")

def tum_verileri_sil():
    conn = sqlite3.connect('kitaplar.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM kitaplar")
    conn.commit()
    conn.close()
    print("Tüm veriler silindi.")

def secili_veriyi_sil(barkod):
    conn = sqlite3.connect('kitaplar.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM kitaplar WHERE kitap_barkod = ?", (barkod,))
    if cursor.rowcount > 0:
        print(f"Barkod numarası {barkod} olan kitap silindi.")
    else:
        print("Bu barkoda sahip kitap bulunamadı.")
    conn.commit()
    conn.close()

def kitap_duzenle(barkod):
    conn = sqlite3.connect('kitaplar.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM kitaplar WHERE kitap_barkod = ?", (barkod,))
    kitap = cursor.fetchone()
    
    if kitap:
        print(f"Mevcut Bilgiler: Kitap Adı: {kitap[1]}, Yazar: {kitap[2]}, Stok: {kitap[4]}, Eklenme Tarihi: {kitap[5]}, Son Güncelleme Tarihi: {kitap[6] if kitap[6] else 'Yeni güncelleme yok.'}")
        
        yeni_ad = input("Yeni Kitap Adı: ") or kitap[1]
        yeni_yazar = input("Yeni Yazar : ") or kitap[2]
        yeni_stok = input("Yeni Stok Adedi : ") or kitap[4]
        guncelleme_tarihi = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        
        
        try:
            cursor.execute("UPDATE kitaplar SET kitap_adi = ?, kitap_yazar = ?, kitap_stok = ?, guncelleme_tarihi = ? WHERE kitap_barkod = ?",
                           (yeni_ad, yeni_yazar, yeni_stok, guncelleme_tarihi, barkod))
            conn.commit()
            print("Kitap bilgileri güncellendi.")
            print(f"Güncellenme tarihi: {guncelleme_tarihi}")
        except sqlite3.Error as e:
            print(f"Güncelleme sırasında bir hata oluştu: {e}")
    else:
        print("Bu barkoda sahip kitap bulunamadı.")
    
    conn.close()


def ana_menu():
    while True:
        print("\n1. Kitap Ekle")
        print("2. Kitapları Listele")
        print("3. Kitap Ara")
        print("4. Tüm Verileri Sil")
        print("5. Seçili Veriyi Sil")
        print("6. Kitap Düzenle")  # Yeni eklenen seçenek
        print("7. Çıkış")
        secim = input("Lütfen bir seçenek girin (1-7): ")
        
        if secim == '1':
            kitap_adi = input("Kitap Adı: ")
            kitap_yazar = input("Kitap Yazarı: ")
            kitap_barkod = input("Kitap Barkodu: ")
            kitap_stok = int(input("Kitap Stok Adedi: "))
            kitap_ekle(kitap_adi, kitap_yazar, kitap_barkod, kitap_stok)
        elif secim == '2':
            kitaplari_listele()
        elif secim == '3':
            barkod = input("Aranacak kitabın barkodunu girin: ")
            kitap_ara(barkod)
        elif secim == '4':
            onay = input("Tüm verileri silmek istediğinizden emin misiniz? (E/H): ")
            if onay.lower() == 'e':
                tum_verileri_sil()
            else:
                print("İşlem iptal edildi.")
        elif secim == '5':
            barkod = input("Silinecek kitabın barkodunu girin: ")
            secili_veriyi_sil(barkod)
        elif secim == '6':  # Yeni eklenen seçenek
            barkod = input("Düzenlenecek kitabın barkodunu girin: ")
            kitap_duzenle(barkod)
        elif secim == '7':
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    veritabani_olustur()
    guncelle_veritabani_semasi()
    ana_menu()