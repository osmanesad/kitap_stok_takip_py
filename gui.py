import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QLineEdit, QLabel, QHBoxLayout, QMessageBox, QInputDialog, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

# Mevcut kitap_stok.py dosyanızı import edin
import kitap_stok

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
        layout.addWidget(self.table)

        # Diğer İşlem Butonları
        button_layout = QHBoxLayout()
        list_button = QPushButton("Kitapları Listele")
        list_button.clicked.connect(self.list_books)
        button_layout.addWidget(list_button)

        search_button = QPushButton("Kitap Ara")
        search_button.clicked.connect(self.search_book)
        button_layout.addWidget(search_button)

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
            kitap_stok.kitap_ekle(kitap_adi, yazar, barkod, int(stok))
            self.list_books()
            self.clear_inputs()
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen tüm alanları doldurun.")

    def list_books(self):
        books = kitap_stok.kitaplari_listele(return_data=True)
        self.table.setRowCount(len(books))
        for row, book in enumerate(books):
            for col, item in enumerate(book):
                self.table.setItem(row, col, QTableWidgetItem(str(item)))

    def search_book(self):
        barkod, ok = QInputDialog.getText(self, "Kitap Ara", "Barkod:")
        if ok and barkod:
            book = kitap_stok.kitap_ara(barkod, return_data=True)
            if book:
                QMessageBox.information(self, "Kitap Bulundu", f"ID: {book[0]}\nKitap Adı: {book[1]}\nYazar: {book[2]}\nBarkod: {book[3]}\nStok: {book[4]}\nKayıt Tarihi: {book[5]}")
            else:
                QMessageBox.warning(self, "Uyarı", "Kitap bulunamadı.")

    def delete_selected_book(self):
        selected_items = self.table.selectedItems()
        if selected_items:
            row = selected_items[0].row()
            barkod = self.table.item(row, 3).text()
            reply = QMessageBox.question(self, "Silme Onayı", f"Barkodu {barkod} olan kitabı silmek istediğinizden emin misiniz?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                kitap_stok.secili_veriyi_sil(barkod)
                self.list_books()
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen silinecek bir kitap seçin.")

    def export_to_excel(self):
        kitap_stok.verileri_excele_aktar()
        QMessageBox.information(self, "Bilgi", "Veriler başarıyla Excel'e aktarıldı.")

    def import_from_excel(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Excel Dosyası Seç", "", "Excel Files (*.xlsx *.xls)")
        if file_name:
            kitap_stok.excel_to_database(file_name)
            self.list_books()

    def clear_inputs(self):
        self.kitap_adi_input.clear()
        self.yazar_input.clear()
        self.barkod_input.clear()
        self.stok_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())