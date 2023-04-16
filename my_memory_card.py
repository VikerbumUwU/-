from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QGroupBox, QRadioButton
class Question():
    def __init__(self,question,ra,rw1,rw2,rw3,kol = 1,kolr = 1):
        self.question = question
        self.ra = ra
        self.rw1 = rw1
        self.rw2 = rw2
        self.rw3 = rw3
        self.kol = kol
        self.kolr = kolr
    def init(self,question,ra,rw1,rw2,rw3):
        self.question = question
        self.ra = ra
        self.rw1 = rw1
        self.rw2 = rw2
        self.rw3 = rw3
    def start_t(self):
        if buton.text() == 'Ответить':
            q.check_answer()
            self.kol += 1
        else:
            q.ask()
    def check_answer(self):
        if answer[0].isChecked():
            q.show_correct('Правильно')
            self.kolr += 1
        else:
            q.show_correct('Неверно')
    def show_correct(self,ye):
        Lab1.setText(ye)
        Lab11.setText('Правильный: '+self.ra)
        q.show_r()
    def show_r(self):
        kvad.hide()
        kvad1.show()
        next_question()
        buton.setText('Следующий вопрос')
    def ask(self):
        shuffle(answer)
        answer[0].setText(self.ra)
        answer[1].setText(self.rw1)
        answer[2].setText(self.rw2)
        answer[3].setText(self.rw3)
        Lab.setText(self.question)
        q.show_q()
    def show_q(self):
        kvad1.hide()
        kvad.show()
        buton.setText('Ответить')
        print('Количество ответов:',self.kol)
        print('Количество верных ответов:',self.kolr)
        print('Рейтинг: ',self.kol / self.kolr * 100)
def next_question():
    while True:
        m_win.cur_question = randint(0,20)
        if m_win.cur_question % 5 == 0 or m_win.cur_question == 0:
            if m_win.cur_question <= 15:
                break
    q.init(
        spis[m_win.cur_question + 0],
        spis[m_win.cur_question + 1],
        spis[m_win.cur_question + 2],
        spis[m_win.cur_question + 3],
        spis[m_win.cur_question + 4]
    )
app = QApplication([])
m_win = QWidget()
line = QVBoxLayout()
linev = QHBoxLayout()
linen = QHBoxLayout()
line.addLayout(linev)
line.addLayout(linen) 
kvad = QGroupBox('Вариантики ответов')
vt1 = QRadioButton('Испанский')
vt2 = QRadioButton('Бразильский')
vt3 = QRadioButton('Ангийский')
vt4 = QRadioButton('Португальский')
linee = QHBoxLayout()
lv = QVBoxLayout()
ln = QVBoxLayout()
lv.addWidget(vt1, alignment=Qt.AlignHCenter)
lv.addWidget(vt3, alignment=Qt.AlignHCenter)
ln.addWidget(vt2, alignment=Qt.AlignHCenter)
ln.addWidget(vt4, alignment=Qt.AlignHCenter)
linee.addLayout(lv)
linee.addLayout(ln)
kvad.setLayout(linee)
kvad1 = QGroupBox('Результатик теста')
Lab1 = QLabel('Правильно/Неправильно')
Lab11 = QLabel('Правильный ответик')
linee1 = QVBoxLayout()
linee1.addWidget(Lab1, alignment=Qt.AlignLeft)
linee1.addWidget(Lab11, alignment=Qt.AlignHCenter)
kvad1.setLayout(linee1)
m_win.cur_question = 0
Lab = QLabel('Государственный язык0 Бразилии')
buton = QPushButton('Ответить')
linev.addWidget(Lab)
linev.addWidget(kvad)
linev.addWidget(kvad1)
kvad1.hide()
linen.addWidget(buton)
m_win.setLayout(line)
from random import shuffle, randint
answer = [vt3, vt2, vt1, vt4]
spis = [
    'Государственный язык Бразилии','Испанский','Английский','Бразильский','Портукальский',
    'Государственный язык2 Бразилии','Испанский','Английский','Бразильский','Портукальский',
    'Государственный язык3 Бразилии','Испанский','Английский','Бразильский','Портукальский',
    'Государственный язык4 Бразилии','Испанский','Английский','Бразильский','Портукальский',
        ]
q = Question(spis[0],spis[1],spis[2],spis[3],spis[4])
q.ask()
q.show_q()
buton.clicked.connect(q.start_t)
m_win.show()
app.exec()
def vopros():
    if input() == 4:
        print('Правильно')
    else:
        print('Неправильно')