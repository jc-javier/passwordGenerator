from PySide6.QtWidgets import QApplication
from mainwindow import PasswordGenerator

app = QApplication()

password_generator = PasswordGenerator()
password_generator.show()

app.exec()
