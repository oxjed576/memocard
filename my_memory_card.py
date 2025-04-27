from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, 
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QRadioButton, 
    QGroupBox, QPushButton, QButtonGroup)
from random import shuffle 

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


app = QApplication([])
memo_win = QWidget()
memo_win.setWindowTitle("Memo Card")
memo_win.resize(400, 400)

btn_OK = QPushButton("Ответить")
lb_question = QLabel("В каком году была основана Москва?")

RadioGroupBox = QGroupBox("Варианты ответов")
rbtn1 = QRadioButton("вариант 1")
rbtn2 = QRadioButton("вариант 2")
rbtn3 = QRadioButton("вариант 3")
rbtn4 = QRadioButton("вариант 4")

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)


layout1 = QHBoxLayout()
layout2 = QVBoxLayout()
layout3 = QVBoxLayout()

layout2.addWidget(rbtn1)
layout2.addWidget(rbtn2)
layout3.addWidget(rbtn3)
layout3.addWidget(rbtn4)

layout1.addLayout(layout2)
layout1.addLayout(layout3)
RadioGroupBox.setLayout(layout1) 

AnsGroupBox = QGroupBox()
lb_Result = QLabel("Прав или нет")
lb_correct = QLabel("Ответ будет тут")
lay_ans = QVBoxLayout()
lay_ans.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
lay_ans.addWidget(lb_correct, alignment=Qt.AlignCenter, stretch=2)
AnsGroupBox.setLayout(lay_ans)

lay_line1 = QHBoxLayout()
lay_line2 = QHBoxLayout()
lay_line3 = QHBoxLayout()

lay_line1.addWidget(lb_question, alignment=Qt.AlignCenter)
lay_line2.addWidget(RadioGroupBox)
lay_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()
lay_line3.addStretch(1)
lay_line3.addWidget(btn_OK, stretch=2)
lay_line3.addStretch(1)

lay_card = QVBoxLayout()
lay_card.addLayout(lay_line1, stretch=2)
lay_card.addLayout(lay_line2, stretch=8)
lay_card.addStretch(1)
lay_card.addLayout(lay_line3, stretch=1)
lay_card.addStretch(1)
lay_card.addSpacing(5)

memo_win.setLayout(lay_card)

question_list = []
q= Question("в каком году создан стандофф ", "2017", "2016", "2018", "2020")
question_list.append(q)
q= Question("в каком году создан майнкрафт: ", "2009", "2007", "2008", "2010")
question_list.append(q)
q= Question("самое сильное оружие в майнкрафт: ", "незеритовый топор", "алм. меч", "незер. меч", "алм. топор")
question_list.append(q)
q= Question("в каком году был создан outlast: ", "2015", "2010", "2012", "2013")
question_list.append(q)
q= Question("dв каком году был создан outlast 2: ", "2015", "2014", "2018", "2017")
question_list.append(q)

def click_ok():
    
    if btn_OK.text() == "Ответить":
        check_answer()
    else:
        next_question()


def show_question():
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_OK.setText("Ответить")


def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText("Следующий вопрос")

answers = [rbtn1, rbtn2, rbtn3, rbtn4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_question.setText(q.question)
    lb_correct.setText(q.right_answer)
    show_question()


def check_answer():
    if answers[0].isChecked:
        show_correct("Правильно!")
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct("Неверно!")

def show_correct(res):
    lb_Result.setText(res)
    show_result()

memo_win.cur_question = -1
def next_question():
    memo_win.cur_question += 1
    if memo_win.cur_question >= len(question_list):
        memo_win.cur_question = 0
    ask(question_list[memo_win.cur_question])   


next_question()
btn_OK.clicked.connect(click_ok)

memo_win.show()
app.exec_()
