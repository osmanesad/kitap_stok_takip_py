import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QTableWidget, QTableWidgetItem, QLineEdit, QLabel, QMessageBox,
    QFileDialog, QInputDialog, QDialog
)
import kitap_stok  # Veritabanı işlevlerini içeren modül

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kitap Stok Takip Sistemi")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Kitap Ekleme Bölümü
        add_layout = QHBoxLayout()
        self.kitap_adi_input = QLineEdit()
        self.yazar_input = QLineEdit()
        self.barkod_input = QLineEdit()
        self.stok_input = QLineEdit()

        add_layout.addWidget(QLabel("Kitap Adı:"))
        add_layout.addWidget(self.kitap_adi_input)
        add_layout.addWidget(QLabel("Yazar:"))
        add_layout.addWidget(self.yazar_input)
        add_layout.addWidget(QLabel("Barkod:"))
        add_layout.addWidget(self.barkod_input)
        add_layout.addWidget(QLabel("Stok:"))
        add_layout.addWidget(self.stok_input)

        add_button = QPushButton("Kitap Ekle")
        add_button.clicked.connect(self.add_book)
        add_layout.addWidget(add_button)
        layout.addLayout(add_layout)

        # Kitap Listesi Tablosu
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["ID", "Kitap Adı", "Yazar", "Barkod", "Stok", "Kayıt Tarihi"])
        # Sütun genişlikleri ile görsel iyileştirme
        self.table.setColumnWidth(0, 50)    # ID
        self.table.setColumnWidth(1, 200)   # Kitap Adı
        self.table.setColumnWidth(2, 150)   # Yazar
        self.table.setColumnWidth(3, 100)   # Barkod
        self.table.setColumnWidth(4, 70)    # Stok
        self.table.setColumnWidth(5, 150)   # Kayıt Tarihi
        layout.addWidget(self.table)

        # Diğer İşlem Butonları
        button_layout = QHBoxLayout()
        list_button = QPushButton("Kitapları Listele")
        list_button.clicked.connect(self.list_books)
        button_layout.addWidget(list_button)

        search_button = QPushButton("Kitap Ara")
        search_button.clicked.connect(self.search_book)
        button_layout.addWidget(search_button)

        edit_button = QPushButton("Seçili Kitabı Düzenle")
        edit_button.clicked.connect(self.edit_selected_book)
        button_layout.addWidget(edit_button)

        delete_button = QPushButton("Seçili Kitabı Sil")
        delete_button.clicked.connect(self.delete_selected_book)
        button_layout.addWidget(delete_button)

        export_button = QPushButton("Excel'e Aktar")
        export_button.clicked.connect(self.export_to_excel)
        button_layout.addWidget(export_button)

        import_button = QPushButton("Excel'den İçe Aktar")
        import_button.clicked.connect(self.import_from_excel)
        button_layout.addWidget(import_button)

        layout.addLayout(button_layout)

        self.list_books()  # Uygulama başladığında kitapları listele

    def add_book(self):
        kitap_adi = self.kitap_adi_input.text()
        yazar = self.yazar_input.text()
        barkod = self.barkod_input.text()
        stok = self.stok_input.text()

        if kitap_adi and yazar and barkod and stok:
            try:
                stok = int(stok)
                kitap_stok.kitap_ekle(kitap_adi, yazar, barkod, stok)
                self.list_books()
                self.clear_inputs()
                QMessageBox.information(self, "Başarılı", "Kitap başarıyla eklendi.")
            except ValueError:
                QMessageBox.warning(self, "Uyarı", "Stok bilgisi bir sayı olmalıdır.")
            except Exception as e:
                QMessageBox.critical(self, "Hata", f"Kitap eklenirken hata oluştu: {e}")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen tüm alanları doldurun.")

    def list_books(self):
        try:
            books = kitap_stok.kitaplari_listele(return_data=True)
            self.table.setRowCount(len(books))
            for row, book in enumerate(books):
                for col, item in enumerate(book):
                    self.table.setItem(row, col, QTableWidgetItem(str(item)))
        except Exception as e:
            QMessageBox.critical(self, "Hata", f"Kitaplar listelenirken hata oluştu: {e}")

    def search_book(self):
        barkod, ok = QInputDialog.getText(self, "Kitap Ara", "Barkod:")
        if ok and barkod:
            try:
                book = kitap_stok.kitap_ara(barkod, return_data=True)
                if book:
                    QMessageBox.information(
                        self, "Kitap Bulundu",
                        f"ID: {book[0]}\nKitap Adı: {book[1]}\nYazar: {book[2]}\nBarkod: {book[3]}\nStok: {book[4]}\nKayıt Tarihi: {book[5]}"
                    )
                else:
                    QMessageBox.warning(self, "Uyarı", "Kitap bulunamadı.")
            except Exception as e:
                QMessageBox.critical(self, "Hata", f"Arama yapılırken hata oluştu: {e}")

    def edit_selected_book(self):
        selected_items = self.table.selectedItems()
        if selected_items:
            row = selected_items[0].row()
            barkod = self.table.item(row, 3).text()

            # Mevcut bilgileri al
            current_book = kitap_stok.kitap_ara(barkod, return_data=True)
            if current_book:
                # Ayrı düzenleme penceresi (dialog) oluşturuluyor.
                dialog = EditBookDialog(current_book, self)
                if dialog.exec_() == QDialog.Accepted:
                    new_adi, new_yazar, new_stok = dialog.get_data()
                    try:
                        kitap_stok.kitap_duzenle(barkod, new_adi, new_yazar, new_stok)
                        self.list_books()
                        QMessageBox.information(self, "Başarılı", "Kitap bilgileri güncellendi.")
                    except Exception as e:
                        QMessageBox.critical(self, "Hata", f"Güncelleme sırasında hata oluştu: {e}")
            else:
                QMessageBox.warning(self, "Uyarı", "Bu barkoda sahip kitap bulunamadı.")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen düzenlemek için bir kitap seçin.")

    def delete_selected_book(self):
        selected_items = self.table.selectedItems()
        if selected_items:
            row = selected_items[0].row()
            barkod = self.table.item(row, 3).text()
            reply = QMessageBox.question(
                self, "Silme Onayı",
                f"Barkodu {barkod} olan kitabı silmek istediğinizden emin misiniz?",
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No
            )
            if reply == QMessageBox.Yes:
                try:
                    kitap_stok.secili_veriyi_sil(barkod)
                    self.list_books()
                except Exception as e:
                    QMessageBox.critical(self, "Hata", f"Silme sırasında hata oluştu: {e}")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen silinecek bir kitap seçin.")

    def export_to_excel(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Excel Dosyası Kaydet", "", "Excel Files (*.xlsx *.xls)")
        if file_name:
            try:
                kitap_stok.verileri_excele_aktar(file_name)
                QMessageBox.information(self, "Başarılı", "Veriler başarıyla Excel'e aktarıldı.")
            except Exception as e:
                QMessageBox.critical(self, "Hata", f"Excel'e aktarım sırasında hata oluştu: {e}")

    def import_from_excel(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Excel Dosyası Seç", "", "Excel Files (*.xlsx *.xls)")
        if file_name:
            try:
                kitap_stok.excel_to_database(file_name)
                self.list_books()
                QMessageBox.information(self, "Başarılı", "Veriler başarıyla içe aktarıldı.")
            except Exception as e:
                QMessageBox.critical(self, "Hata", f"Excel'den içe aktarım sırasında hata oluştu: {e}")

    def clear_inputs(self):
        self.kitap_adi_input.clear()
        self.yazar_input.clear()
        self.barkod_input.clear()
        self.stok_input.clear()

class EditBookDialog(QDialog):
    def __init__(self, book, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Kitap Düzenle")
        self.book = book  # book; kitap_stok modülünden alınan tuple (ID, Ad, Yazar, Barkod, Stok, Kayıt Tarihi)
        layout = QVBoxLayout(self)

        # Kitap Adı
        h_layout1 = QHBoxLayout()
        h_layout1.addWidget(QLabel("Kitap Adı:"))
        self.name_input = QLineEdit(self)
        self.name_input.setText(book[1])
        h_layout1.addWidget(self.name_input)
        layout.addLayout(h_layout1)

        # Yazar
        h_layout2 = QHBoxLayout()
        h_layout2.addWidget(QLabel("Yazar:"))
        self.author_input = QLineEdit(self)
        self.author_input.setText(book[2])
        h_layout2.addWidget(self.author_input)
        layout.addLayout(h_layout2)

        # Stok
        h_layout3 = QHBoxLayout()
        h_layout3.addWidget(QLabel("Stok:"))
        self.stock_input = QLineEdit(self)
        self.stock_input.setText(str(book[4]))
        h_layout3.addWidget(self.stock_input)
        layout.addLayout(h_layout3)

        # Butonlar
        button_layout = QHBoxLayout()
        save_button = QPushButton("Kaydet", self)
        save_button.clicked.connect(self.save)
        cancel_button = QPushButton("İptal", self)
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(save_button)
        button_layout.addWidget(cancel_button)
        layout.addLayout(button_layout)

    def save(self):
        # Stok bilgisinin sayı olduğundan emin olalım
        try:
            int(self.stock_input.text())
            self.accept()
        except ValueError:
            QMessageBox.warning(self, "Uyarı", "Stok bilgisi bir sayı olmalıdır.")

    def get_data(self):
        return (
            self.name_input.text(),
            self.author_input.text(),
            int(self.stock_input.text())
        )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
