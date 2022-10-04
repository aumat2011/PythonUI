import sys

from PyQt5 import QtWidgets

def Window():
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()
    pencere.setGeometry(200, 200, 500, 800)
    pencere.setWindowTitle("A.U.M.G.F.R.S")
    pencere.setGeometry(200,200,500,800)

    okay = QtWidgets.QPushButton("Tamam")
    cancel = QtWidgets.QPushButton("İptal")

    h_box = QtWidgets.QHBoxLayout()

    h_box.addStretch()
    h_box.addWidget(okay)
    h_box.addWidget(cancel)

    v_box = QtWidgets.QVBoxLayout()

    v_box.addStretch()
    v_box.addLayout(h_box)

    pencere.setLayout(v_box)
    pencere.show()
    sys.exit(app.exec())

Window()
