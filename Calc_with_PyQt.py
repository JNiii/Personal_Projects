#Calculator using PyQt5 and QtDesigner


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(192, 258)
        MainWindow.setMinimumSize(QtCore.QSize(192, 258))
        MainWindow.setMaximumSize(QtCore.QSize(192, 258))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.seven = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.pressed('7'))
        self.seven.setGeometry(QtCore.QRect(0, 50, 51, 31))
        self.seven.setObjectName("seven")
        self.eight = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.pressed('8'))
        self.eight.setGeometry(QtCore.QRect(50, 50, 51, 31))
        self.eight.setObjectName("eight")
        self.nine = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.pressed('9'))
        self.nine.setGeometry(QtCore.QRect(100, 50, 51, 31))
        self.nine.setObjectName("nine")
        self.four = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.pressed('4'))
        self.four.setGeometry(QtCore.QRect(0, 80, 51, 31))
        self.four.setObjectName("four")
        self.five = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.pressed('5'))
        self.five.setGeometry(QtCore.QRect(50, 80, 51, 31))
        self.five.setObjectName("five")
        self.six = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.pressed('6'))
        self.six.setGeometry(QtCore.QRect(100, 80, 51, 31))
        self.six.setObjectName("six")
        self.one = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.pressed('1'))
        self.one.setGeometry(QtCore.QRect(0, 110, 51, 31))
        self.one.setObjectName("one")
        self.two = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.pressed('2'))
        self.two.setGeometry(QtCore.QRect(50, 110, 51, 31))
        self.two.setObjectName("two")
        self.three = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.pressed('3'))
        self.three.setGeometry(QtCore.QRect(100, 110, 51, 31))
        self.three.setObjectName("three")
        self.dot = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.pressed('.'))
        self.dot.setGeometry(QtCore.QRect(100, 140, 51, 31))
        self.dot.setObjectName("dot")
        self.zero = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.pressed('0'))
        self.zero.setGeometry(QtCore.QRect(0, 140, 101, 31))
        self.zero.setObjectName("zero")
        self.divide = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.div_it('/'))
        self.divide.setGeometry(QtCore.QRect(150, 50, 41, 31))
        self.divide.setObjectName("divide")
        self.multiply = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.mult_it('*'))
        self.multiply.setGeometry(QtCore.QRect(150, 80, 41, 31))
        self.multiply.setObjectName("multiply")
        self.subtract = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.sub_it('-'))
        self.subtract.setGeometry(QtCore.QRect(150, 110, 41, 31))
        self.subtract.setObjectName("subtract")
        self.add = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.add_it('+'))
        self.add.setGeometry(QtCore.QRect(150, 140, 41, 31))
        self.add.setObjectName("add")
        self.equals = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.equate())
        self.equals.setGeometry(QtCore.QRect(0, 170, 191, 31))
        self.equals.setObjectName("equals")
        self.clear = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.cleared())
        self.clear.setGeometry(QtCore.QRect(0, 200, 191, 31))
        self.clear.setObjectName("clear")
        self.output = QtWidgets.QLabel(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(0, 0, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.output.setFont(font)
        self.output.setToolTipDuration(1)
        self.output.setFrameShape(QtWidgets.QFrame.Box)
        self.output.setFrameShadow(QtWidgets.QFrame.Plain)
        self.output.setText("")
        self.output.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.output.setWordWrap(True)
        self.output.setObjectName("output")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 192, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.init_num = 0
        self.op = ''
<<<<<<< Updated upstream
        
=======

>>>>>>> Stashed changes
    def equate(self):
        try:
            self.output.setText(str(eval(str(self.init_num) + self.op + self.output.text())))
            if type(self.init_num) is int:
                self.init_num = int(self.output.text())
            else:
                self.init_num = round(float(self.output.text()), 2)
        except:
            self.output.setText('Error!')
        
    def cleared(self):
        self.init_num = 0
        self.op = ''
        self.output.setText('')

    def check_op(self, op):
        if op in '+-':
            self.init_num = 0
        else:
            self.init_num = 1

    def add_it(self, pressed):
        if self.init_num == 0:
            self.check_op(pressed)
            self.init_num += int(self.output.text())
            self.op = pressed
            self.output.setText('')
        else:
            self.op = pressed
            self.output.setText('')
        
    def sub_it(self, pressed):
        if self.init_num == 0:
            self.check_op(pressed)
            self.init_num -= int(self.output.text())
            self.op = pressed
            self.output.setText('')
        else:
            self.op = pressed
            self.output.setText('')
        
    def mult_it(self, pressed):
        if self.init_num == 0:
            self.check_op(pressed)
            self.init_num = float(self.output.text()) * self.init_num
            self.op = pressed
            self.output.setText('')
        else:
            self.op = pressed
            self.output.setText('')
        
    def div_it(self, pressed):
        if self.init_num == 0:
            self.check_op(pressed)
            self.init_num = float(self.output.text()) / self.init_num
            self.op = pressed
            self.output.setText('')
        else:
            self.op = pressed
            self.output.setText('')
                
    def pressed(self,pressed):
        if pressed == '.' and '.' in self.output.text():
            self.output.setText(self.output.text())
        else:
            self.output.setText(self.output.text() + pressed)
            

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.seven.setText(_translate("MainWindow", "7"))
        self.eight.setText(_translate("MainWindow", "8"))
        self.nine.setText(_translate("MainWindow", "9"))
        self.four.setText(_translate("MainWindow", "4"))
        self.five.setText(_translate("MainWindow", "5"))
        self.six.setText(_translate("MainWindow", "6"))
        self.one.setText(_translate("MainWindow", "1"))
        self.two.setText(_translate("MainWindow", "2"))
        self.three.setText(_translate("MainWindow", "3"))
        self.dot.setText(_translate("MainWindow", "."))
        self.zero.setText(_translate("MainWindow", "0"))
        self.divide.setText(_translate("MainWindow", "/"))
        self.multiply.setText(_translate("MainWindow", "*"))
        self.subtract.setText(_translate("MainWindow", "-"))
        self.add.setText(_translate("MainWindow", "+"))
        self.equals.setText(_translate("MainWindow", "Equals"))
        self.clear.setText(_translate("MainWindow", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())