import sys

from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()
    def init_ui(self):
        self.YaziAlani = QtWidgets.QLineEdit()
        self.Temizle = QtWidgets.QPushButton("Temizle")
        self.Yazdir = QtWidgets.QPushButton("Yazdir")

        vBox = QtWidgets.QVBoxLayout()

        vBox.addWidget(self.YaziAlani)
        vBox.addWidget(self.Temizle)
        vBox.addWidget(self.Yazdir)
        vBox.addStretch()

        self.setLayout(vBox)

        self.Temizle.clicked.connect(self.click)
        self.Yazdir.clicked.connect(self.click)

        self.show()

    def click(self):
        sender = self.sender()

        if sender.text() == "Temizle":
            self.YaziAlani.clear()
        else:
            print(self.YaziAlani.text())

app = QtWidgets.QApplication(sys.argv)

window = Window()

sys.exit(app.exec())