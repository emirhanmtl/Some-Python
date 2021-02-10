import sys

from PyQt5 import QtWidgets,QtGui

def Pencere():

    app = QtWidgets.QApplication(sys.argv)

    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt Ders 2")

    etiket1 = QtWidgets.QLabel(pencere)
    etiket2 = QtWidgets.QLabel(pencere)

    etiket2.setPixmap(QtGui.QPixmap("python.png"))
    etiket1.setText("Burası bir yazıdır.")

    etiket1.move(210,30)
    etiket2.move(70,200)

    pencere.setGeometry(100,100,500,500)

    pencere.show()

    sys.exit(app.exec_())

Pencere()