import sys


from PyQt5 import QtWidgets,QtGui

def Pencere():
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()
    etiket  = QtWidgets.QLabel(pencere)
    image = QtWidgets.QLabel(pencere)
    buton = QtWidgets.QPushButton(pencere)

    pencere.setGeometry(200,200,500,800)
    pencere.setWindowTitle("Merhaba Dünya")

    etiket.setText("Mehaba Dünya")
    etiket.move(50,100)

    image.move(75,210)
    image.setPixmap(QtGui.QPixmap("Images/logo.png"))

    buton.setText("Click It!!!")
    buton.move(300,100)
    pencere.show()
    sys.exit(app.exec())

Pencere()