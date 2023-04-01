from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget,
QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox,
QRadioButton, QGroupBox, QButtonGroup)
from random import (shuffle,randint)


app = QApplication([])
btn_OK = QPushButton('Ответить')
lb_Question = QLabel('')
RadioGroupBox = QGroupBox('Варианты ответов:')
rbtn_1 = QRadioButton('')
rbtn_2 = QRadioButton('')
rbtn_3 = QRadioButton('')
rbtn_4 = QRadioButton('')
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
shuffle(answers)
RG = QButtonGroup()



layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment = Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)


layout_line1 = QVBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
RadioGroupBox.show()
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch = 2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.setSpacing(5)
layout_card.addLayout(layout_line3, stretch = 1)

RG.setExclusive(False)
rbtn_1.setChecked(False)
rbtn_2.setChecked(False)
rbtn_3.setChecked(False)
rbtn_4.setChecked(False)
RG.setExclusive(True)

AnsGroupBox.hide()

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3



def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RG.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RG.setExclusive(True)



questions_list = list()

def next_question():
    window.total += 1
    cur_question = randint(0, len(questions_list) -1)
    q = questions_list[cur_question]
    ask(q)


def show_correct(res):
    lb_Result.setText(res)
    show_result()



def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
    print(round(window.score/window.total*100))


def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')


def start_test():
    if 'Ответить' == btn_OK.text():
        show_result()
    else:
        show_question()

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()


def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()


window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memory Card)')
window.cur_question = -1
window.score = 0
window.total = 0



q = Question('Какой национальности не существует?','Смурфы','Энцы','Чулымцы','Алеуты')
questions_list.append(q)

q = Question('Столица Норвегии?','Осло','Амстердам','Оттава','Вена')
questions_list.append(q)

q = Question('Самое быстрое животное в мире?','Гепард','Лев','Тигр','Гиена')
questions_list.append(q)

q = Question('Сколько граней у куба?','6','8','7','9')
questions_list.append(q)

q = Question('Государственный язык Бразилии?','Португальский','Бразильский','Испанский','Итальянский')
questions_list.append(q)

q = Question('Страна с самой высокой продолжительностью жизни?','Китай','Россия','Босния и Герцоговина','Эстония')
questions_list.append(q)


btn_OK.clicked.connect(click_OK)
next_question()
#ask(questions_list[0])


window.show()

app.exec_()