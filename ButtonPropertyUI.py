import sys

from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.YaziAlani = QtWidgets.QLabel("Bana henüz tıklanmadı")
        self.Button = QtWidgets.QPushButton("Click It")
        self.Counter = 0

        vBox = QtWidgets.QVBoxLayout()

        vBox.addWidget(self.YaziAlani)
        vBox.addWidget(self.Button)
        vBox.addStretch()

        hBox = QtWidgets.QHBoxLayout()

        hBox.addStretch()
        hBox.addLayout(vBox)
        hBox.addStretch()

        self.setLayout(hBox)

        self.Button.clicked.connect(self.click)

        self.show()

    def click(self):
        self.Counter += 1
        self.YaziAlani.setText("Buttona " + str(self.Counter) + " kadar tıklandı.")

app = QtWidgets.QApplication(sys.argv)
window = Window()
sys.exit(app.exec())
