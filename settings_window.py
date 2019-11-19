# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Settings_window(object):
    def setupUi(self, Settings_window):
        Settings_window.setObjectName("Settings_window")
        Settings_window.resize(528, 179)
        self.toolButton_unrar = QtWidgets.QToolButton(Settings_window)
        self.toolButton_unrar.setGeometry(QtCore.QRect(470, 50, 31, 31))
        self.toolButton_unrar.setObjectName("toolButton_unrar")
        self.label = QtWidgets.QLabel(Settings_window)
        self.label.setGeometry(QtCore.QRect(10, 20, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Settings_window)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 451, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Settings_window)
        self.pushButton.setGeometry(QtCore.QRect(300, 140, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setAutoDefault(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Settings_window)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 140, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Settings_window)
        QtCore.QMetaObject.connectSlotsByName(Settings_window)

    def retranslateUi(self, Settings_window):
        _translate = QtCore.QCoreApplication.translate
        Settings_window.setWindowTitle(_translate("Settings_window", "Settings"))
        self.toolButton_unrar.setText(_translate("Settings_window", "..."))
        self.label.setText(_translate("Settings_window", "Select unrar.exe path:"))
        self.label_2.setText(_translate("Settings_window", "Path"))
        self.pushButton.setText(_translate("Settings_window", "OK"))
        self.pushButton_2.setText(_translate("Settings_window", "Cancel"))


'''if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Settings_window = QtWidgets.QWidget()
    ui = Ui_Settings_window()
    ui.setupUi(Settings_window)
    Settings_window.show()
    sys.exit(app.exec_())'''
