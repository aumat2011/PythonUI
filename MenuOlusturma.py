import sys

from PyQt5.QtWidgets import QApplication,QAction,qApp,QMainWindow

class Menu(QMainWindow):

    def __init__(self):
        super().__init__()
        menubar = self.menuBar()

        dosya = menubar.addMenu("Dosya")
        duzenle = menubar.addMenu("Düzenle")

        dosya_ac = QAction("Dosya Aç",self)
        dosya_ac.setShortcut("Ctrl+O")

        dosya_kaydet = QAction("Dosya Kaydet",self)
        dosya_kaydet.setShortcut("Ctrl+O")

        cikis = QAction("Çıkış")
        cikis.setShortcut("Çtrl+Q")

        self.setWindowTitle("Menüler")

        self.show()

app = QApplication(sys.argv)

menu = Menu()

sys.exit(app.exec_())