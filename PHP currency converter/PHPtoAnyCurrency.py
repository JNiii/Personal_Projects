# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PHPtoAnyCurrency.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from ScrapeRate import Scrap




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(260, 280)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(260, 280))
        MainWindow.setMaximumSize(QtCore.QSize(260, 280))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.input_num = QtWidgets.QLineEdit(self.centralwidget)
        self.input_num.setGeometry(QtCore.QRect(10, 10, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        self.input_num.setFont(font)
        self.input_num.setMaxLength(10)
        self.input_num.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.input_num.setObjectName("input_num")
        self.initial_curr = QtWidgets.QComboBox(self.centralwidget)
        self.initial_curr.setGeometry(QtCore.QRect(80, 50, 101, 21))
        self.initial_curr.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.initial_curr.setObjectName("initial_curr")
        self.initial_curr.addItem("")
        self.initial_curr.addItem("")
        self.final_curr = QtWidgets.QComboBox(self.centralwidget)
        self.final_curr.setGeometry(QtCore.QRect(80, 120, 101, 21))
        self.final_curr.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.final_curr.setObjectName("final_curr")
        self.final_curr.addItem("")
        self.final_curr.addItem("")
        self.final_curr.addItem("")
        self.final_curr.addItem("")
        self.final_curr.addItem("")
        self.final_curr.addItem("")
        self.final_curr.addItem("")
        self.final_curr.addItem("")
        self.final_curr.addItem("")
        self.final_curr.addItem("")
        self.rate = QtWidgets.QLabel(self.centralwidget)
        self.rate.setGeometry(QtCore.QRect(10, 80, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        self.rate.setFont(font)
        self.rate.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rate.setFrameShadow(QtWidgets.QFrame.Plain)
        self.rate.setLineWidth(2)
        self.rate.setText("")
        self.rate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rate.setOpenExternalLinks(False)
        self.rate.setObjectName("rate")
        self.convert = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.conv_data())
        self.convert.setGeometry(QtCore.QRect(80, 180, 101, 31))
        self.convert.setObjectName("convert")
        self.out_conv = QtWidgets.QLabel(self.centralwidget)
        self.out_conv.setGeometry(QtCore.QRect(10, 150, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        self.out_conv.setFont(font)
        self.out_conv.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.out_conv.setFrameShadow(QtWidgets.QFrame.Plain)
        self.out_conv.setLineWidth(2)
        self.out_conv.setText("")
        self.out_conv.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.out_conv.setOpenExternalLinks(False)
        self.out_conv.setObjectName("out_conv")
        self.clr = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.clear())
        self.clr.setGeometry(QtCore.QRect(80, 220, 101, 31))
        self.clr.setObjectName("clr")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 260, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        initial = Scrap('https://www.bpi.com.ph/forex/rates')
        initial.get_data()
        self.exchange_rate = [initial.php_buy, initial.php_sell]
        self.num = 0

    def clear(self):
        self.input_num.setText('')
        self.rate.setText('')
        self.out_conv.setText('')

    def conv_data(self):
        self.check_data()
        if self.initial_curr.currentText() == 'PHP - Buy':
            self.ex_outcurr(0)
        else:
            self.ex_outcurr(1)
        self.convert_now()

    def check_data(self):
        try:
            self.num = float(self.input_num.text())
        except:
            self.rate.setText('Invalid input.')
            
    def ex_outcurr(self, n):
        if self.final_curr.currentText() == 'USD':
            self.rate.setText(str(self.exchange_rate[n]['USDollar']))
        elif self.final_curr.currentText() == 'EUR':
            self.rate.setText(str(self.exchange_rate[n]['Euro']))
        elif self.final_curr.currentText() == 'JPY':
            self.rate.setText(str(self.exchange_rate[n]['JapaneseYen']))
        elif self.final_curr.currentText() == 'HKD':
            self.rate.setText(str(self.exchange_rate[n]['HongKongDollar']))
        elif self.final_curr.currentText() == 'AUD':
            self.rate.setText(str(self.exchange_rate[n]['AustralianDollar']))
        elif self.final_curr.currentText() == 'SGD':
            self.rate.setText(str(self.exchange_rate[n]['SingaporeanDollar']))
        elif self.final_curr.currentText() == 'CAD':
            self.rate.setText(str(self.exchange_rate[n]['CanadianDollar']))
        elif self.final_curr.currentText() == 'GBP':
            self.rate.setText(str(self.exchange_rate[n]['BritishPound']))
        elif self.final_curr.currentText() == 'CHF':
            self.rate.setText(str(self.exchange_rate[n]['SwissFranc']))
        else:
            self.rate.setText(str(self.exchange_rate[n]['ChineseYuan']))
    
    def convert_now(self):
        output = round(self.num / float(self.rate.text()), 2)
        self.out_conv.setText(str(output))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PHPtoAnyCurrency"))
        self.initial_curr.setItemText(0, _translate("MainWindow", "PHP - Buy"))
        self.initial_curr.setItemText(1, _translate("MainWindow", "PHP - Sell"))
        self.final_curr.setItemText(0, _translate("MainWindow", "USD"))
        self.final_curr.setItemText(1, _translate("MainWindow", "EUR"))
        self.final_curr.setItemText(2, _translate("MainWindow", "JPY"))
        self.final_curr.setItemText(3, _translate("MainWindow", "HKD"))
        self.final_curr.setItemText(4, _translate("MainWindow", "AUD"))
        self.final_curr.setItemText(5, _translate("MainWindow", "SGD"))
        self.final_curr.setItemText(6, _translate("MainWindow", "CAD"))
        self.final_curr.setItemText(7, _translate("MainWindow", "GBP"))
        self.final_curr.setItemText(8, _translate("MainWindow", "CHF"))
        self.final_curr.setItemText(9, _translate("MainWindow", "CNY"))
        self.convert.setText(_translate("MainWindow", "Convert"))
        self.clr.setText(_translate("MainWindow", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
