import random
import string

import pyperclip
from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QMessageBox

from ui_mainwindow import Ui_MainWindow


class PasswordGenerator(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.generate_password()
        self.actionQuit.triggered.connect(self.quit)
        self.actionAbout.triggered.connect(self.about)
        self.checkbox_list = [self.uppercase_checkbox, self.lowercase_checkbox, self.numbers_checkbox, self.special_checkbox]

        self.uppercase_checkbox.stateChanged.connect(self.uppercase)
        self.lowercase_checkbox.stateChanged.connect(self.lowercase)
        self.numbers_checkbox.stateChanged.connect(self.numbers)
        self.special_checkbox.stateChanged.connect(self.special_characters)

        self.length_slider.sliderMoved.connect(self.set_spinbox)
        self.length_slider.sliderMoved.connect(self.generate_password)
        self.length_spinbox.valueChanged.connect(self.set_slider)
        self.length_spinbox.valueChanged.connect(self.generate_password)

        for checkbox in self.checkbox_list:
            checkbox.stateChanged.connect(self.generate_password)

        self.generate_button.clicked.connect(self.generate_password)
        self.copy_button.clicked.connect(self.copy_to_clipboard)
        self.clear_button.clicked.connect(self.clear_clipboard)
        self.hide_show_button.clicked.connect(self.toggle_visible)

    def generate_password(self):
        try:
            password_characters = self.uppercase() + self.lowercase() + self.numbers() + self.special_characters()
            password = ''.join(random.choice(password_characters) for _ in range(self.length_spinbox.value()))
            self.generated_pass_lineedit.setText(password)
        except IndexError:
            QMessageBox.warning(self, 'Password Generator', 'Password cannot be empty spaces.')

    def copy_to_clipboard(self):
        pyperclip.copy(self.generated_pass_lineedit.text())

    @staticmethod
    def clear_clipboard():
        pyperclip.copy('')

    def toggle_visible(self):
        echo = self.generated_pass_lineedit.echoMode()
        if echo == QtWidgets.QLineEdit.EchoMode.Password:
            self.generated_pass_lineedit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        else:
            self.generated_pass_lineedit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

    def quit(self):
        self.close()

    def about(self):
        QMessageBox.information(self, 'Password Generator', '\nA simple password generator for creating strong '
                                                            'passwords in just a few clicks.\n\n'
                                                            'Tips on password security:\n\n'
                                                            '- Do NOT use information related to you in your '
                                                            'password.\n'
                                                            '- Do NOT reuse the same password for multiple websites.\n'
                                                            '- Do NOT save your passwords anywhere with the exception '
                                                            'of password managers.\n'
                                                            '- NEVER share your passwords via email or text.\n'
                                                            '- Update your passwords every three months.\n')

    def uppercase(self):
        if self.uppercase_checkbox.isChecked():
            return string.ascii_uppercase
        else:
            return ''

    def lowercase(self):
        if self.lowercase_checkbox.isChecked():
            return string.ascii_lowercase
        else:
            return ''

    def numbers(self):
        if self.numbers_checkbox.isChecked():
            return string.digits
        else:
            return ''

    def special_characters(self):
        if self.special_checkbox.isChecked():
            return string.punctuation
        else:
            return ''

    def set_spinbox(self):
        length = self.length_slider.value()
        self.length_spinbox.setValue(length)

    def set_slider(self):
        length = self.length_spinbox.value()
        self.length_slider.setSliderPosition(length)
