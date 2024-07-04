def kitap_duzenle(barkod):
    conn = sqlite3.connect('kitaplar.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM kitaplar WHERE kitap_barkod = ?", (barkod,))
    kitap = cursor.fetchone()
    
    if kitap:
        print(f"Mevcut Bilgiler: Kitap Adı: {kitap[1]}, Yazar: {kitap[2]}, Stok: {kitap[4]}")
        yeni_ad = input("Yeni Kitap Adı (değiştirmemek için boş bırakın): ") or kitap[1]
        yeni_yazar = input("Yeni Yazar (değiştirmemek için boş bırakın): ") or kitap[2]
        yeni_stok = input("Yeni Stok Adedi (değiştirmemek için boş bırakın): ") or kitap[4]
        
        try:
            cursor.execute("UPDATE kitaplar SET kitap_adi = ?, kitap_yazar = ?, kitap_stok = ? WHERE kitap_barkod = ?",
                           (yeni_ad, yeni_yazar, yeni_stok, barkod))
            conn.commit()
            print("Kitap bilgileri güncellendi.")
        except sqlite3.Error as e:
            print(f"Güncelleme sırasında bir hata oluştu: {e}")
    else:
        print("Bu barkoda sahip kitap bulunamadı.")
    
    conn.close()

# Ana menüye yeni seçenek ekleyelim
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