# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'analizador.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QStatusBar, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(70, 90, 901, 461))
        self.widget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(14, 8, 73, 255), stop:0.36 rgba(28, 17, 145, 255), stop:0.6 rgba(126, 14, 81, 255), stop:0.75 rgba(234, 11, 11, 255), stop:0.79 rgba(244, 70, 5, 255), stop:0.86 rgba(255, 136, 0, 255), stop:0.935 rgba(239, 236, 55, 255));")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QRect(70, -1, 581, 91))
        self.groupBox.setStyleSheet(u"background-color: rgb(239, 236, 55);")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 58, 15))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(190, 20, 91, 16))
        self.textEdit_Amplitud = QTextEdit(self.groupBox)
        self.textEdit_Amplitud.setObjectName(u"textEdit_Amplitud")
        self.textEdit_Amplitud.setGeometry(QRect(10, 40, 171, 21))
        self.textEdit_Amplitud.setStyleSheet(u"background-color: rgb(235, 232, 77);\n"
"color:rgb(0, 0, 0);")
        self.textEdit = QTextEdit(self.groupBox)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(200, 40, 171, 21))
        self.textEdit.setStyleSheet(u"background-color: rgb(235, 232, 77);\n"
"color:rgb(0, 0, 0)")
        self.pushButton_Actualizar = QPushButton(self.groupBox)
        self.pushButton_Actualizar.setObjectName(u"pushButton_Actualizar")
        self.pushButton_Actualizar.setGeometry(QRect(10, 60, 361, 23))
        self.pushButton_Actualizar.setStyleSheet(u"background-color: rgb(235, 232, 77);\n"
"color: rgb(0, 0, 0);")
        self.radioButton_negro = QRadioButton(self.groupBox)
        self.radioButton_negro.setObjectName(u"radioButton_negro")
        self.radioButton_negro.setGeometry(QRect(380, 20, 98, 20))
        self.radioButton_rojo = QRadioButton(self.groupBox)
        self.radioButton_rojo.setObjectName(u"radioButton_rojo")
        self.radioButton_rojo.setGeometry(QRect(380, 40, 98, 20))
        self.radioButton_verde = QRadioButton(self.groupBox)
        self.radioButton_verde.setObjectName(u"radioButton_verde")
        self.radioButton_verde.setGeometry(QRect(380, 60, 98, 20))
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(650, 0, 321, 91))
        self.groupBox_2.setStyleSheet(u"background-color: rgb(236, 233, 54);")
        self.textEdit_2 = QTextEdit(self.groupBox_2)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(20, 40, 104, 21))
        self.lineEdit_resultado = QLineEdit(self.groupBox_2)
        self.lineEdit_resultado.setObjectName(u"lineEdit_resultado")
        self.lineEdit_resultado.setGeometry(QRect(140, 60, 113, 22))
        self.pushButton_actualizarcalculo = QPushButton(self.groupBox_2)
        self.pushButton_actualizarcalculo.setObjectName(u"pushButton_actualizarcalculo")
        self.pushButton_actualizarcalculo.setGeometry(QRect(30, 60, 84, 23))
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 20, 58, 15))
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(150, 20, 131, 31))
        font = QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(Qt.TextFormat.RichText)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1024, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Parametros de Se\u00f1al", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Amplitud", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Frecuencia[Hz]", None))
        self.pushButton_Actualizar.setText(QCoreApplication.translate("MainWindow", u"Actualizar Gr\u00e1fico", None))
        self.radioButton_negro.setText(QCoreApplication.translate("MainWindow", u"Negro", None))
        self.radioButton_rojo.setText(QCoreApplication.translate("MainWindow", u"Rojo", None))
        self.radioButton_verde.setText(QCoreApplication.translate("MainWindow", u"Verde", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Evaluaci\u00f3n de la Se\u00f1al", None))
        self.pushButton_actualizarcalculo.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Tiempo(t)", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"y(t)=A sin(2pift)", None))
    # retranslateUi

