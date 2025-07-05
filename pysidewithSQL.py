import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, QMessageBox
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Database setup
engine = create_engine('sqlite:///students.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    nim = Column(String)
    hobby = Column(String)

Base.metadata.create_all(engine)

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Aplikasi Input Data')
        self.setGeometry(100, 100, 300, 200)
        
        # Layout
        layout = QVBoxLayout()

        # Labels
        self.label = QLabel('Masukkan detail Anda:')
        layout.addWidget(self.label)

        # Input Fields
        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText('Nama')
        layout.addWidget(self.name_input)

        self.nim_input = QLineEdit(self)
        self.nim_input.setPlaceholderText('NIM')
        layout.addWidget(self.nim_input)

        self.hobby_input = QLineEdit(self)
        self.hobby_input.setPlaceholderText('Hobi')
        layout.addWidget(self.hobby_input)

        # Buttons
        submit_btn = QPushButton('Kirim', self)
        submit_btn.setStyleSheet("background-color: #82E0AA")
        submit_btn.clicked.connect(self.submit)
        layout.addWidget(submit_btn)

        reset_btn = QPushButton('Reset', self)
        reset_btn.setStyleSheet("background-color: #E9F5AA")
        reset_btn.clicked.connect(self.reset)
        layout.addWidget(reset_btn)

        self.setLayout(layout)

    def submit(self):
        name = self.name_input.text()
        nim = self.nim_input.text()
        hobby = self.hobby_input.text()

        if not name or not nim or not hobby:
            QMessageBox.warning(self, 'Input Error', 'Semua bidang harus diisi!')
        else:
            try:
                new_student = Student(name=name, nim=nim, hobby=hobby)
                session.add(new_student)
                session.commit()
                self.label.setText(f'Nama: {name}, NIM: {nim}, Hobi: {hobby}')
                QMessageBox.information(self, 'Success', 'Data berhasil disimpan ke database!')
            except Exception as e:
                QMessageBox.critical(self, 'Database Error', str(e))

    def reset(self):
        self.name_input.clear()
        self.nim_input.clear()
        self.hobby_input.clear()
        self.label.setText('Masukkan detail Anda:')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec())