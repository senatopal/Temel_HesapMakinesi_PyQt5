from PyQt5.QtWidgets import *
from hesapMakinesi import HesapMakinesi

app=QApplication([])
pencere=HesapMakinesi()
pencere.show()
app.exec_()