import sys
from PySide6.QtWidgets import QApplication, QPushButton

# Membuat instance aplikasi
app = QApplication(sys.argv)

# Membuat tombol
button = QPushButton("Klik Saya")

# Menampilkan tombol
button.show()

# Menjalankan loop aplikasi
sys.exit(app.exec())