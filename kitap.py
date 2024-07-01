import sqlite3
from datetime import datetime



def veritabani_olustur():
    conn = sqlite3.connect('kitaplar.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS kitaplar
                      (id INTEGER PRIMARY KEY,
                       kitap_adi TEXT,
                       kitap_barkod TEXT UNIQUE,
                       kitap_stok INTEGER,
                       kayit_tarihi TEXT)''')
    conn.commit()
    conn.close()

def guncelle_veritabani_semasi():
    conn = sqlite3.connect('kitaplar.db')
    cursor = conn.cursor()
    try:
        cursor.execute("ALTER TABLE kitaplar ADD COLUMN kayit_tarihi TEXT")
        print("Veritabanı şeması güncellendi: kayit_tarihi sütunu eklendi.")
    except sqlite3.OperationalError:
        print("kayit_tarihi sütunu zaten mevcut.")
    conn.commit()
    conn.close()

def kitap_ekle(kitap_adi, kitap_barkod, kitap_stok):
    conn = sqlite3.connect('kitaplar.db')
    cursor = conn.cursor()
    kayit_tarihi = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        cursor.execute("INSERT INTO kitaplar (kitap_adi, kitap_barkod, kitap_stok, kayit_tarihi) VALUES (?, ?, ?, ?)",
                       (kitap_adi, kitap_barkod, kitap_stok, kayit_tarihi))
        conn.commit()
        print("Kitap başarıyla eklendi.")
    except sqlite3.Error as e:
        print(f"Veri eklerken bir hata oluştu: {e}")
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
            print(f"ID: {kitap[0]}, Kitap Adı: {kitap[1]}, Barkod: {kitap[2]}, Stok: {kitap[3]}, Kayıt Tarihi: {kitap[4]}")

def kitap_ara(barkod):
    conn = sqlite3.connect('kitaplar.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM kitaplar WHERE kitap_barkod = ?", (barkod,))
    kitap = cursor.fetchone()
    conn.close()
    
    if kitap:
        print(f"ID: {kitap[0]}, Kitap Adı: {kitap[1]}, Barkod: {kitap[2]}, Stok: {kitap[3]}, Kayıt Tarihi: {kitap[4]}")
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

def ana_menu():
    while True:
        print("\n1. Kitap Ekle")
        print("2. Kitapları Listele")
        print("3. Kitap Ara")
        print("4. Tüm Verileri Sil")
        print("5. Seçili Veriyi Sil")
        print("6. Çıkış")
        secim = input("Lütfen bir seçenek girin (1-6): ")
        
        if secim == '1':
            kitap_adi = input("Kitap adı: ")
            kitap_barkod = input("Kitap barkodu: ")
            kitap_stok = int(input("Kitap stok adedi: "))
            kitap_ekle(kitap_adi, kitap_barkod, kitap_stok)
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
        elif secim == '6':
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    veritabani_olustur()
    guncelle_veritabani_semasi()
    ana_menu()