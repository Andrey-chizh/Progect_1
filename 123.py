import io
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget


catalog = {
            '1': ('Чесночный батон', '0', 150), '2': ('Лаваш армянский', '0', 190), '3': ('Тарталетки', '0', 30),
            '4': ('Хлеб кукурузный', '0', 100), '5': ('Хлеб ржаной', '0', 80), '6': ('Хлеб деревенский', '0', 100),
            '7': ('Торт Невские берега', '0', 280), '8': ('Пирожные Питерские', '0', 330),
            '9': ('Пирожное Картошка', '0', 230), '10': ('Торт тирамису', '0', 480),
            '11': ('Пирожное эклер', '0', 180), '12': ('Пирожное Kinder', '0', 55),
            '13': ('Бедро куриное', '0', 220), '14': ('Колбаса сырокопченая', '0', 160),
            '15': ('Сосиски молочные', '0', 110), '16': ('Колбаса варено-копченая', '0', 300),
            '17': ('Паштет куриный', '0', 30), '18': ('Фарш свино-говяжий', '0', 120),
            '19': ('Молоко 2,5%', '0', 80), '20': ('Сыр плавленый', '0', 40), '21': ('Сыр полутвердый', '0', 180),
            '22': ('Сметана 20%', '0', 90), '23': ('Сливочное масло', '0', 180), '24': ('Биойогурт 3,5%', '0', 35),
            '25': ('Щупальца кальмара', '0', 140), '26': ('Кальмар ', '0', 260), '27': ('Креветки', '0', 360),
            '28': ('Горбуша горячего копчения', '0', 280), '29': ('Сельдь слабосоленая', '0', 160),
            '30': ('Икра горбуши красная', '0', 620), '31': ('Огурцы', '0', 220),
            '32': ('Картофель', '0', 5), '33': ('Помидоры', '0', 100),
            '34': ('Перец', '0', 100), '35': ('Морковь', '0', 12), '36': ('Капуста белокочанная', '0', 120),
            }


class Glav_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Проект_глав.ui", self)
        self.back()

    def back(self):
        self.label.show()
        self.skip_btn.show()

        self.bread_btn.hide()
        self.conf_btn.hide()
        self.meat_btn.hide()
        self.milk_btn.hide()
        self.seaf_btn.hide()
        self.veg_btn.hide()
        self.bask_btn.hide()
        self.label_2.hide()
        self.back_btn.hide()
        self.skip_btn.clicked.connect(self.on)

    def on(self):
        self.Bask_W = Bask_W()
        self.Bread_W = Bread_W()
        self.Conf_W = Conf_W()
        self.Meat_W = Meat_W()
        self.Milk_W = Milk_W()
        self.Seaf_W = Seaf_W()
        self.Veg_W = Veg_W()

        self.label.hide()
        self.skip_btn.hide()

        self.back_btn.show()
        self.label_2.show()
        self.bask_btn.show()
        self.bread_btn.show()
        self.conf_btn.show()
        self.meat_btn.show()
        self.milk_btn.show()
        self.seaf_btn.show()
        self.veg_btn.show()

        self.bask_btn.clicked.connect(self.bask)
        self.back_btn.clicked.connect(self.back)
        self.bread_btn.clicked.connect(self.bread)
        self.conf_btn.clicked.connect(self.conf)
        self.meat_btn.clicked.connect(self.meat)
        self.milk_btn.clicked.connect(self.milk)
        self.seaf_btn.clicked.connect(self.seaf)
        self.veg_btn.clicked.connect(self.veg)

    def bask(self):
        self.Bask_W.show()
        self.hide()

    def bread(self):
        self.Bread_W.show()
        self.hide()

    def conf(self):
        self.Conf_W.show()
        self.hide()

    def meat(self):
        self.Meat_W.show()
        self.hide()

    def milk(self):
        self.Milk_W.show()
        self.hide()

    def seaf(self):
        self.Seaf_W.show()
        self.hide()

    def veg(self):
        self.Veg_W.show()
        self.hide()


class Bread_W(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Bread_W.ui", self)
        self.back_btn.clicked.connect(self.back)
        self.bask_btn.clicked.connect(self.bask)
        self.pl1_btn.clicked.connect(self.plus1, 1)
        self.min1_btn.clicked.connect(self.min1, 1)
        self.pl2_btn.clicked.connect(self.plus2, 2)
        self.min2_btn.clicked.connect(self.min2, 2)
        self.pl3_btn.clicked.connect(self.plus3, 3)
        self.min3_btn.clicked.connect(self.min3, 3)
        self.pl4_btn.clicked.connect(self.plus4, 4)
        self.min4_btn.clicked.connect(self.min4, 4)
        self.pl5_btn.clicked.connect(self.plus5, 5)
        self.min5_btn.clicked.connect(self.min5, 5)
        self.pl6_btn.clicked.connect(self.plus6, 6)
        self.min6_btn.clicked.connect(self.min6, 6)

    def back(self):
        self.hide()
        ex.show()

    def bask(self):
        ex.Bask_W.show()
        self.hide()

    def plus1(self, num):
        self.num_lbl1.setText(str(int(self.num_lbl1.text()) + 1))
        # недоработано(доработать добавление в корзину)

    def min1(self, num):
        if int(self.num_lbl1.text()) > 0:
            self.num_lbl1.setText(str(int(self.num_lbl1.text()) - 1))
        else:
            pass
        # недоработано(доработать добавление в корзину)

    def plus2(self, num):
        self.num_lbl2.setText(str(int(self.num_lbl2.text()) + 1))
        # недоработано(доработать добавление в корзину)

    def min2(self, num):
        if int(self.num_lbl2.text()) > 0:
            self.num_lbl2.setText(str(int(self.num_lbl2.text()) - 1))
        else:
            pass
        # недоработано(доработать добавление в корзину)

    def plus3(self, num):
        self.num_lbl3.setText(str(int(self.num_lbl3.text()) + 1))
        # недоработано(доработать добавление в корзину)

    def min3(self, num):
        if int(self.num_lbl3.text()) > 0:
            self.num_lbl3.setText(str(int(self.num_lbl3.text()) - 1))
        else:
            pass
        # недоработано(доработать добавление в корзину)

    def plus4(self, num):
        self.num_lbl4.setText(str(int(self.num_lbl4.text()) + 1))
        # недоработано(доработать добавление в корзину)

    def min4(self, num):
        if int(self.num_lbl4.text()) > 0:
            self.num_lbl4.setText(str(int(self.num_lbl4.text()) - 1))
        else:
            pass
        # недоработано(доработать добавление в корзину)

    def plus5(self, num):
        self.num_lbl5.setText(str(int(self.num_lbl5.text()) + 1))
        # недоработано(доработать добавление в корзину)

    def min5(self, num):
        if int(self.num_lbl5.text()) > 0:
            self.num_lbl5.setText(str(int(self.num_lbl5.text()) - 1))
        else:
            pass
        # недоработано(доработать добавление в корзину)

    def plus6(self, num):
        self.num_lbl6.setText(str(int(self.num_lbl6.text()) + 1))
        # недоработано(доработать добавление в корзину)

    def min6(self, num):
        if int(self.num_lbl6.text()) > 0:
            self.num_lbl6.setText(str(int(self.num_lbl6.text()) - 1))
        else:
            pass
        # недоработано(доработать добавление в корзину)


class Conf_W(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Conf_W.ui", self)
        self.back_btn.clicked.connect(self.back)
        self.bask_btn.clicked.connect(self.bask)
        self.pl1_btn.clicked.connect(self.plus1, 7)
        self.min1_btn.clicked.connect(self.min1, 7)
        self.pl2_btn.clicked.connect(self.plus2, 8)
        self.min2_btn.clicked.connect(self.min2, 8)
        self.pl3_btn.clicked.connect(self.plus3, 9)
        self.min3_btn.clicked.connect(self.min3, 9)
        self.pl4_btn.clicked.connect(self.plus4, 10)
        self.min4_btn.clicked.connect(self.min4, 10)
        self.pl5_btn.clicked.connect(self.plus5, 11)
        self.min5_btn.clicked.connect(self.min5, 11)
        self.pl6_btn.clicked.connect(self.plus6, 12)
        self.min6_btn.clicked.connect(self.min6, 12)

    def back(self):
        self.hide()
        ex.show()

    def bask(self):
        self.hide()
        ex.Bask_W.show()

    def plus1(self, num):
        self.num_lbl1.setText(str(int(self.num_lbl1.text()) + 1))
        # недоработано(доработать добавление в корзину)

    def min1(self, num):
        if int(self.num_lbl1.text()) > 0:
            self.num_lbl1.setText(str(int(self.num_lbl1.text()) - 1))
        else:
            pass
        # недоработано(доработать добавление в корзину)

    def plus2(self, num):
        self.num_lbl2.setText(str(int(self.num_lbl2.text()) + 1))
        # недоработано(доработать добавление в корзину)

    def min2(self, num):
        if int(self.num_lbl2.text()) > 0:
            self.num_lbl2.setText(str(int(self.num_lbl2.text()) - 1))
        else:
            pass
        # недоработано(доработать добавление в корзину)

    def plus3(self, num):
        self.num_lbl3.setText(str(int(self.num_lbl3.text()) + 1))
        # недоработано(доработать добавление в корзину)

    def min3(self, num):
        if int(self.num_lbl3.text()) > 0:
            self.num_lbl3.setText(str(int(self.num_lbl3.text()) - 1))
        else:
            pass
        # недоработано(доработать добавление в корзину)

    def plus4(self, num):
        self.num_lbl4.setText(str(int(self.num_lbl4.text()) + 1))
        # недоработано(доработать добавление в корзину)

    def min4(self, num):
        if int(self.num_lbl4.text()) > 0:
            self.num_lbl4.setText(str(int(self.num_lbl4.text()) - 1))
        else:
            pass
        # недоработано(доработать добавление в корзину)

    def plus5(self, num):
        self.num_lbl5.setText(str(int(self.num_lbl5.text()) + 1))
        # недоработано(доработать добавление в корзину)

    def min5(self, num):
        if int(self.num_lbl5.text()) > 0:
            self.num_lbl5.setText(str(int(self.num_lbl5.text()) - 1))
        else:
            pass
        # недоработано(доработать добавление в корзину)

    def plus6(self, num):
        self.num_lbl6.setText(str(int(self.num_lbl6.text()) + 1))
        # недоработано(доработать добавление в корзину)

    def min6(self, num):
        if int(self.num_lbl6.text()) > 0:
            self.num_lbl6.setText(str(int(self.num_lbl6.text()) - 1))
        else:
            pass
        # недоработано(доработать добавление в корзину)


class Meat_W(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Meat_W.ui", self)
        self.back_btn.clicked.connect(self.back)
        self.bask_btn.clicked.connect(self.bask)
        self.pl1_btn.clicked.connect(self.plus1, 13)
        self.min1_btn.clicked.connect(self.min1, 13)
        self.pl2_btn.clicked.connect(self.plus2, 14)
        self.min2_btn.clicked.connect(self.min2, 14)
        self.pl3_btn.clicked.connect(self.plus3, 15)
        self.min3_btn.clicked.connect(self.min3, 15)
        self.pl4_btn.clicked.connect(self.plus4, 16)
        self.min4_btn.clicked.connect(self.min4, 16)
        self.pl5_btn.clicked.connect(self.plus5, 17)
        self.min5_btn.clicked.connect(self.min5, 17)
        self.pl6_btn.clicked.connect(self.plus6, 18)
        self.min6_btn.clicked.connect(self.min6, 18)

    def back(self):
        self.hide()
        ex.show()

    def bask(self):
        self.hide()
        ex.Bask_W.show()

    def plus1(self, num):
        self.num_lbl1.setText(str(int(self.num_lbl1.text()) + 1))
        # недоработано(доработать добавление в корзину)

    def min1(self, num):
        if int(self.num_lbl1.text()) > 0:
            self.num_lbl1.setText(str(int(self.num_lbl1.text()) - 1))
        else:
            pass
        # недоработано(доработать добавление в корзину)

    def plus2(self, num):
        self.num_lbl2.setText(str(int(self.num_lbl2.text()) + 1))
        # недоработано(доработать добавление в корзину)

    def min2(self, num):
        if int(self.num_lbl2.text()) > 0:
            self.num_lbl2.setText(str(int(self.num_lbl2.text()) - 1))
        else:
            pass
        # недоработано(доработать добавление в корзину)

    def plus3(self, num):
        self.num_lbl3.setText(str(int(self.num_lbl3.text()) + 1))
        # недоработано(доработать добавление в корзину)

    def min3(self, num):
        if int(self.num_lbl3.text()) > 0:
            self.num_lbl3.setText(str(int(self.num_lbl3.text()) - 1))
        else:
            pass
        # недоработано(доработать добавление в корзину)

    def plus4(self, num):
        self.num_lbl4.setText(str(int(self.num_lbl4.text()) + 1))
        # недоработано(доработать добавление в корзину)

    def min4(self, num):
        if int(self.num_lbl4.text()) > 0:
            self.num_lbl4.setText(str(int(self.num_lbl4.text()) - 1))
        else:
            pass
        # недоработано(доработать добавление в корзину)

    def plus5(self, num):
        self.num_lbl5.setText(str(int(self.num_lbl5.text()) + 1))
        # недоработано(доработать добавление в корзину)

    def min5(self, num):
        if int(self.num_lbl5.text()) > 0:
            self.num_lbl5.setText(str(int(self.num_lbl5.text()) - 1))
        else:
            pass
        # недоработано(доработать добавление в корзину)

    def plus6(self, num):
        self.num_lbl6.setText(str(int(self.num_lbl6.text()) + 1))
        # недоработано(доработать добавление в корзину)

    def min6(self, num):
        if int(self.num_lbl6.text()) > 0:
            self.num_lbl6.setText(str(int(self.num_lbl6.text()) - 1))
        else:
            pass
        # недоработано(доработать добавление в корзину)


class Milk_W(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Milk_W.ui", self)
        self.back_btn.clicked.connect(self.back)
        self.bask_btn.clicked.connect(self.bask)
        self.pl1_btn.clicked.connect(self.plus1, 19)
        self.min1_btn.clicked.connect(self.min1, 19)
        self.pl2_btn.clicked.connect(self.plus2, 20)
        self.min2_btn.clicked.connect(self.min2, 20)
        self.pl3_btn.clicked.connect(self.plus3, 21)
        self.min3_btn.clicked.connect(self.min3, 21)
        self.pl4_btn.clicked.connect(self.plus4, 22)
        self.min4_btn.clicked.connect(self.min4, 22)
        self.pl5_btn.clicked.connect(self.plus5, 23)
        self.min5_btn.clicked.connect(self.min5, 23)
        self.pl6_btn.clicked.connect(self.plus6, 24)
        self.min6_btn.clicked.connect(self.min6, 24)

    def back(self):
        self.hide()
        ex.show()

    def bask(self):
        self.hide()
        ex.Bask_W.show()

    def plus1(self, num):
        self.num_lbl1.setText(str(int(self.num_lbl1.text()) + 1))
        # недоработано(доработать добавление в корзину)

    def min1(self, num):
        if int(self.num_lbl1.text()) > 0:
            self.num_lbl1.setText(str(int(self.num_lbl1.text()) - 1))
        else:
            pass
        # недоработано(доработать добавление в корзину)

    def plus2(self, num):
        self.num_lbl2.setText(str(int(self.num_lbl2.text()) + 1))
        # недоработано(доработать добавление в корзину)

    def min2(self, num):
        if int(self.num_lbl2.text()) > 0:
            self.num_lbl2.setText(str(int(self.num_lbl2.text()) - 1))
        else:
            pass
        # недоработано(доработать добавление в корзину)

    def plus3(self, num):
        self.num_lbl3.setText(str(int(self.num_lbl3.text()) + 1))
        # недоработано(доработать добавление в корзину)

    def min3(self, num):
        if int(self.num_lbl3.text()) > 0:
            self.num_lbl3.setText(str(int(self.num_lbl3.text()) - 1))
        else:
            pass
        # недоработано(доработать добавление в корзину)

    def plus4(self, num):
        self.num_lbl4.setText(str(int(self.num_lbl4.text()) + 1))
        # недоработано(доработать добавление в корзину)

    def min4(self, num):
        if int(self.num_lbl4.text()) > 0:
            self.num_lbl4.setText(str(int(self.num_lbl4.text()) - 1))
        else:
            pass
        # недоработано(доработать добавление в корзину)

    def plus5(self, num):
        self.num_lbl5.setText(str(int(self.num_lbl5.text()) + 1))
        # недоработано(доработать добавление в корзину)

    def min5(self, num):
        if int(self.num_lbl5.text()) > 0:
            self.num_lbl5.setText(str(int(self.num_lbl5.text()) - 1))
        else:
            pass
        # недоработано(доработать добавление в корзину)

    def plus6(self, num):
        self.num_lbl6.setText(str(int(self.num_lbl6.text()) + 1))
        # недоработано(доработать добавление в корзину)

    def min6(self, num):
        if int(self.num_lbl6.text()) > 0:
            self.num_lbl6.setText(str(int(self.num_lbl6.text()) - 1))
        else:
            pass
        # недоработано(доработать добавление в корзину)


class Seaf_W(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Seaf_W.ui", self)
        self.back_btn.clicked.connect(self.back)
        self.bask_btn.clicked.connect(self.bask)
        self.pl1_btn.clicked.connect(self.plus1, 25)
        self.min1_btn.clicked.connect(self.min1, 25)
        self.pl2_btn.clicked.connect(self.plus2, 26)
        self.min2_btn.clicked.connect(self.min2, 26)
        self.pl3_btn.clicked.connect(self.plus3, 27)
        self.min3_btn.clicked.connect(self.min3, 27)
        self.pl4_btn.clicked.connect(self.plus4, 28)
        self.min4_btn.clicked.connect(self.min4, 28)
        self.pl5_btn.clicked.connect(self.plus5, 29)
        self.min5_btn.clicked.connect(self.min5, 29)
        self.pl6_btn.clicked.connect(self.plus6, 30)
        self.min6_btn.clicked.connect(self.min6, 30)

    def back(self):
        self.hide()
        ex.show()

    def bask(self):
        self.hide()
        ex.Bask_W.show()

    def plus1(self, num):
        self.num_lbl1.setText(str(int(self.num_lbl1.text()) + 1))
        # недоработано(доработать добавление в корзину)

    def min1(self, num):
        if int(self.num_lbl1.text()) > 0:
            self.num_lbl1.setText(str(int(self.num_lbl1.text()) - 1))
        else:
            pass
        # недоработано(доработать добавление в корзину)

    def plus2(self, num):
        self.num_lbl2.setText(str(int(self.num_lbl2.text()) + 1))
        # недоработано(доработать добавление в корзину)

    def min2(self, num):
        if int(self.num_lbl2.text()) > 0:
            self.num_lbl2.setText(str(int(self.num_lbl2.text()) - 1))
        else:
            pass
        # недоработано(доработать добавление в корзину)

    def plus3(self, num):
        self.num_lbl3.setText(str(int(self.num_lbl3.text()) + 1))
        # недоработано(доработать добавление в корзину)

    def min3(self, num):
        if int(self.num_lbl3.text()) > 0:
            self.num_lbl3.setText(str(int(self.num_lbl3.text()) - 1))
        else:
            pass
        # недоработано(доработать добавление в корзину)

    def plus4(self, num):
        self.num_lbl4.setText(str(int(self.num_lbl4.text()) + 1))
        # недоработано(доработать добавление в корзину)

    def min4(self, num):
        if int(self.num_lbl4.text()) > 0:
            self.num_lbl4.setText(str(int(self.num_lbl4.text()) - 1))
        else:
            pass
        # недоработано(доработать добавление в корзину)

    def plus5(self, num):
        self.num_lbl5.setText(str(int(self.num_lbl5.text()) + 1))
        # недоработано(доработать добавление в корзину)

    def min5(self, num):
        if int(self.num_lbl5.text()) > 0:
            self.num_lbl5.setText(str(int(self.num_lbl5.text()) - 1))
        else:
            pass
        # недоработано(доработать добавление в корзину)

    def plus6(self, num):
        self.num_lbl6.setText(str(int(self.num_lbl6.text()) + 1))
        # недоработано(доработать добавление в корзину)

    def min6(self, num):
        if int(self.num_lbl6.text()) > 0:
            self.num_lbl6.setText(str(int(self.num_lbl6.text()) - 1))
        else:
            pass
        # недоработано(доработать добавление в корзину)


class Veg_W(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Veg_W.ui", self)
        self.back_btn.clicked.connect(self.back)
        self.bask_btn.clicked.connect(self.bask)
        self.pl1_btn.clicked.connect(self.plus1, 31)
        self.min1_btn.clicked.connect(self.min1, 31)
        self.pl2_btn.clicked.connect(self.plus2, 32)
        self.min2_btn.clicked.connect(self.min2, 32)
        self.pl3_btn.clicked.connect(self.plus3, 33)
        self.min3_btn.clicked.connect(self.min3, 33)
        self.pl4_btn.clicked.connect(self.plus4, 34)
        self.min4_btn.clicked.connect(self.min4, 34)
        self.pl5_btn.clicked.connect(self.plus5, 35)
        self.min5_btn.clicked.connect(self.min5, 35)
        self.pl6_btn.clicked.connect(self.plus6, 36)
        self.min6_btn.clicked.connect(self.min6, 36)

    def back(self):
        self.hide()
        ex.show()

    def bask(self):
        self.hide()
        ex.Bask_W.show()

    def plus1(self, num):
        self.num_lbl1.setText(str(int(self.num_lbl1.text()) + 1))
        # недоработано(доработать добавление в корзину)

    def min1(self, num):
        if int(self.num_lbl1.text()) > 0:
            self.num_lbl1.setText(str(int(self.num_lbl1.text()) - 1))
        else:
            pass
        # недоработано(доработать добавление в корзину)

    def plus2(self, num):
        self.num_lbl2.setText(str(int(self.num_lbl2.text()) + 1))
        # недоработано(доработать добавление в корзину)

    def min2(self, num):
        if int(self.num_lbl2.text()) > 0:
            self.num_lbl2.setText(str(int(self.num_lbl2.text()) - 1))
        else:
            pass
        # недоработано(доработать добавление в корзину)

    def plus3(self, num):
        self.num_lbl3.setText(str(int(self.num_lbl3.text()) + 1))
        # недоработано(доработать добавление в корзину)

    def min3(self, num):
        if int(self.num_lbl3.text()) > 0:
            self.num_lbl3.setText(str(int(self.num_lbl3.text()) - 1))
        else:
            pass
        # недоработано(доработать добавление в корзину)

    def plus4(self, num):
        self.num_lbl4.setText(str(int(self.num_lbl4.text()) + 1))
        # недоработано(доработать добавление в корзину)

    def min4(self, num):
        if int(self.num_lbl4.text()) > 0:
            self.num_lbl4.setText(str(int(self.num_lbl4.text()) - 1))
        else:
            pass
        # недоработано(доработать добавление в корзину)

    def plus5(self, num):
        self.num_lbl5.setText(str(int(self.num_lbl5.text()) + 1))
        # недоработано(доработать добавление в корзину)

    def min5(self, num):
        if int(self.num_lbl5.text()) > 0:
            self.num_lbl5.setText(str(int(self.num_lbl5.text()) - 1))
        else:
            pass
        # недоработано(доработать добавление в корзину)

    def plus6(self, num):
        self.num_lbl6.setText(str(int(self.num_lbl6.text()) + 1))
        # недоработано(доработать добавление в корзину)

    def min6(self, num):
        if int(self.num_lbl6.text()) > 0:
            self.num_lbl6.setText(str(int(self.num_lbl6.text()) - 1))
        else:
            pass
        # недоработано(доработать добавление в корзину)


class Bask_W(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Bask_W.ui", self)
        self.back_btn.clicked.connect(self.back)
        self.pay_btn.clicked.connect(self.pay)

    def back(self):
        self.hide()
        ex.show()

    def pay(self):
        self.Pay_W = Pay_W()
        self.Pay_W.show()
        self.hide()


class CardError(Exception):
    pass


class CardFormatError(CardError):
    pass


class CardLuhnError(CardError):
    pass


class Pay_W(QWidget):
    def __init__(self):
        super(Pay_W, self).__init__()
        uic.loadUi('Pay_W.ui', self)
        self.back_btn.clicked.connect(self.back)
        self.hintLabel.setText(
            'Введите номер карты (16 цифр без пробелов):')
        self.payButton.clicked.connect(self.process_data)

    def get_card_number(self):
        card_num = self.cardData.text()
        if not (card_num.isdigit() and len(card_num) == 16):
            raise CardFormatError("Неверный формат номера")
        return card_num

    def double(self, x):
        res = x * 2
        if res > 9:
            res = res - 9
        return res

    def luhn_algorithm(self, card):
        odd = map(lambda x: self.double(int(x)), card[::2])
        even = map(int, card[1::2])
        if (sum(odd) + sum(even)) % 10 == 0:
            return True
        else:
            raise CardLuhnError("Недействительный номер карты")

    def process_data(self):
        try:
            number = self.get_card_number()
            if self.luhn_algorithm(number):
                print("Ваша карта обрабатывается...")
        except CardError as e:
            self.errorLabel.setText(f"Ошибка! {e}")

    def back(self):
        self.hide()
        ex.Bask_W.show()


def except_hook(cls, exeption, traceback):
    sys.__excepthook__(cls, exeption, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Glav_Window()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())

# bask - от полного Basket, подписано как 'Оплата'
# conf - от полного Confectionery
# seaf - от полного Seafood
# veg - от полного Vegetables
# W - от полного Window
# При нажатии + или - в словаре происходят изменения:
# {1: (+-1 200)}, где 1 это номер продукта, +-1 - его кол-во, а 200 - его цена
# num - от Numbering
# min - от Minus
# pl - от Plus