from PyQt5.QtWidgets import *
from hesapMakinesi_python import Ui_Form

class HesapMakinesi(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.expression = ''
        self.pushButton_0.clicked.connect(lambda: self.yerlestir('0'))
        self.pushButton_1.clicked.connect(lambda: self.yerlestir('1'))
        self.pushButton_2.clicked.connect(lambda: self.yerlestir('2'))
        self.pushButton_3.clicked.connect(lambda: self.yerlestir('3'))
        self.pushButton_4.clicked.connect(lambda: self.yerlestir('4'))
        self.pushButton_5.clicked.connect(lambda: self.yerlestir('5'))
        self.pushButton_6.clicked.connect(lambda: self.yerlestir('6'))
        self.pushButton_7.clicked.connect(lambda: self.yerlestir('7'))
        self.pushButton_8.clicked.connect(lambda: self.yerlestir('8'))
        self.pushButton_9.clicked.connect(lambda: self.yerlestir('9'))
        self.pushButton_ekle.clicked.connect(lambda: self.yerlestir('+'))
        self.pushButton_cikar.clicked.connect(lambda: self.operator('-'))
        self.pushButton_carpma.clicked.connect(lambda: self.operator('*'))
        self.pushButton_bol.clicked.connect(lambda: self.operator('/'))
        self.pushButton_nokta.clicked.connect(lambda: self.yerlestir('.'))
        self.pushButton_sifirla.clicked.connect(self.sifirla)
        self.pushButton_yuzde.clicked.connect(self.yuzde)
        self.pushButton_karekok.clicked.connect(self.karekok)
        self.pushButton_esittir.clicked.connect(self.esittir)
        self.pushButton_arti.clicked.connect(self.isaret)  # İşaret değiştirme butonu

    def yerlestir(self, button_text):
        if self.label.text() == '0' or self.label.text() == 'Error':
            self.label.setText(button_text)
        else:
            self.label.setText(self.label.text() + button_text)

        self.expression += button_text

    def operator(self, operator):
            if self.expression[-1] in ['+', '-', '*', '/']:
                self.expression = self.expression[:-1]     # eğer herhangi bir operatör kullanıldıktan sonra tekrar operatör kullanılmak istenirse öncelikle son operatörü çıkarır daha sonra güncel operatörü ekleriz
            self.expression += operator
            self.label.setText(self.expression)

    def sifirla(self):
        self.label.setText('0')
        self.expression = ''

    def yuzde(self):
        try:
            result = eval(self.expression) / 100
            self.label.setText(str(result))
            self.expression = str(result)
        except Exception:
            self.label.setText('Error')
            self.expression = ''

    def karekok(self):
        try:
            result = eval(self.expression) ** 0.5
            self.label.setText(str(result))
            self.expression = str(result)
        except Exception:
            self.label.setText('Error')
            self.expression = ''

    def esittir(self):
        try:
            result = eval(self.expression)  # eval fonksiyonu işlem önceliğine göre sonucu vericek
            self.label.setText(str(result))
            self.expression = str(result)
            
        except Exception:
            self.label.setText('Error')
            self.expression = ''

    def isaret(self):
        current_text = self.label.text()
        if current_text != '0' and current_text != 'Error':
            if current_text[0] == '-':
                self.label.setText(current_text[1:])
            else:
                self.label.setText('-' + current_text)

            # İşlem sırasında da ifadeyi güncelleyelim
            if self.expression:
                if self.expression[-1] in ['+', '-', '*', '/']:
                    self.expression = self.expression[:-1]
                self.expression = '-' + self.expression

