# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSlider, QSpinBox, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(631, 253)
        MainWindow.setMinimumSize(QSize(631, 253))
        MainWindow.setMaximumSize(QSize(631, 253))
        icon = QIcon()
        icon.addFile(u":/locked_icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setInputMethodHints(Qt.ImhNone)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.include_groupbox = QGroupBox(self.centralwidget)
        self.include_groupbox.setObjectName(u"include_groupbox")
        self.include_groupbox.setGeometry(QRect(10, 10, 230, 211))
        self.layoutWidget = QWidget(self.include_groupbox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 30, 210, 169))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.uppercase_checkbox = QCheckBox(self.layoutWidget)
        self.uppercase_checkbox.setObjectName(u"uppercase_checkbox")
        font = QFont()
        font.setPointSize(10)
        self.uppercase_checkbox.setFont(font)
        self.uppercase_checkbox.setChecked(True)

        self.verticalLayout.addWidget(self.uppercase_checkbox)

        self.lowercase_checkbox = QCheckBox(self.layoutWidget)
        self.lowercase_checkbox.setObjectName(u"lowercase_checkbox")
        self.lowercase_checkbox.setFont(font)
        self.lowercase_checkbox.setChecked(True)

        self.verticalLayout.addWidget(self.lowercase_checkbox)

        self.numbers_checkbox = QCheckBox(self.layoutWidget)
        self.numbers_checkbox.setObjectName(u"numbers_checkbox")
        self.numbers_checkbox.setFont(font)
        self.numbers_checkbox.setChecked(True)

        self.verticalLayout.addWidget(self.numbers_checkbox)

        self.special_checkbox = QCheckBox(self.layoutWidget)
        self.special_checkbox.setObjectName(u"special_checkbox")
        self.special_checkbox.setFont(font)
        self.special_checkbox.setChecked(True)

        self.verticalLayout.addWidget(self.special_checkbox)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.length_spinbox = QSpinBox(self.layoutWidget)
        self.length_spinbox.setObjectName(u"length_spinbox")
        self.length_spinbox.setMinimumSize(QSize(40, 0))
        self.length_spinbox.setMaximumSize(QSize(40, 16777215))
        self.length_spinbox.setFrame(False)
        self.length_spinbox.setAlignment(Qt.AlignCenter)
        self.length_spinbox.setReadOnly(False)
        self.length_spinbox.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.length_spinbox.setProperty("showGroupSeparator", False)
        self.length_spinbox.setMinimum(12)
        self.length_spinbox.setMaximum(50)

        self.horizontalLayout.addWidget(self.length_spinbox)

        self.length_slider = QSlider(self.layoutWidget)
        self.length_slider.setObjectName(u"length_slider")
        self.length_slider.setMinimumSize(QSize(150, 0))
        self.length_slider.setMaximumSize(QSize(150, 16777215))
        font1 = QFont()
        font1.setPointSize(9)
        self.length_slider.setFont(font1)
        self.length_slider.setMouseTracking(True)
        self.length_slider.setStyleSheet(u"")
        self.length_slider.setInputMethodHints(Qt.ImhNone)
        self.length_slider.setMinimum(11)
        self.length_slider.setMaximum(51)
        self.length_slider.setPageStep(5)
        self.length_slider.setValue(12)
        self.length_slider.setSliderPosition(12)
        self.length_slider.setTracking(True)
        self.length_slider.setOrientation(Qt.Horizontal)
        self.length_slider.setInvertedAppearance(False)
        self.length_slider.setInvertedControls(False)
        self.length_slider.setTickPosition(QSlider.NoTicks)
        self.length_slider.setTickInterval(0)

        self.horizontalLayout.addWidget(self.length_slider, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(250, 60, 371, 112))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setSpacing(11)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.generated_pass_lineedit = QLineEdit(self.layoutWidget1)
        self.generated_pass_lineedit.setObjectName(u"generated_pass_lineedit")
        self.generated_pass_lineedit.setMinimumSize(QSize(0, 30))
        self.generated_pass_lineedit.setMaximumSize(QSize(370, 30))
        font2 = QFont()
        font2.setPointSize(14)
        self.generated_pass_lineedit.setFont(font2)
        self.generated_pass_lineedit.setMaxLength(50)
        self.generated_pass_lineedit.setFrame(False)
        self.generated_pass_lineedit.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.generated_pass_lineedit)

        self.generate_button = QPushButton(self.layoutWidget1)
        self.generate_button.setObjectName(u"generate_button")
        self.generate_button.setMinimumSize(QSize(0, 30))
        self.generate_button.setMaximumSize(QSize(370, 30))
        font3 = QFont()
        font3.setPointSize(11)
        self.generate_button.setFont(font3)

        self.verticalLayout_3.addWidget(self.generate_button)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.copy_button = QPushButton(self.layoutWidget1)
        self.copy_button.setObjectName(u"copy_button")

        self.horizontalLayout_2.addWidget(self.copy_button)

        self.clear_button = QPushButton(self.layoutWidget1)
        self.clear_button.setObjectName(u"clear_button")
        self.clear_button.setMinimumSize(QSize(0, 0))
        self.clear_button.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_2.addWidget(self.clear_button)

        self.hide_show_button = QPushButton(self.layoutWidget1)
        self.hide_show_button.setObjectName(u"hide_show_button")
        self.hide_show_button.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.hide_show_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 631, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuFile.addAction(self.actionQuit)
        self.menuAbout.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Password Generator", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
#if QT_CONFIG(shortcut)
        self.actionQuit.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.include_groupbox.setTitle(QCoreApplication.translate("MainWindow", u"Customize your password", None))
        self.uppercase_checkbox.setText(QCoreApplication.translate("MainWindow", u"UPPERCASE letters", None))
        self.lowercase_checkbox.setText(QCoreApplication.translate("MainWindow", u"lowercase letters", None))
        self.numbers_checkbox.setText(QCoreApplication.translate("MainWindow", u"Numbers", None))
        self.special_checkbox.setText(QCoreApplication.translate("MainWindow", u"Special characters", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Length", None))
        self.length_spinbox.setSuffix("")
        self.generated_pass_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Generated password...", None))
        self.generate_button.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.copy_button.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.clear_button.setText(QCoreApplication.translate("MainWindow", u"Clear Clipboard", None))
        self.hide_show_button.setText(QCoreApplication.translate("MainWindow", u"Hide/Show", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

