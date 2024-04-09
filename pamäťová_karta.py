from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QButtonGroup
from random import *
app = QApplication([])
main_win = QWidget() #vytvorí okno
main_win.resize(800, 400) # velkost okna
main_win.setWindowTitle('Vedomostná karta')
main_win.total = 0
main_win.score = 0

question = QLabel("")
button = QPushButton("Vyhodnotiť")

class Question():
    def __init__(self,question_text,right_answer,wrong1,wrong2,wrong3):
        self.question = question_text
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3 

question_list = [
    Question("Akej farby je drevo","Hnedá","Čierna","Modrá","Biela"),
    Question("Hlavné mesto Sloveska","Bratislava", "Košice","Prešov","Michalovce"),
    Question("Akým jazykom sa rozpráva v Česku","Čeština", "Slovenčina","Maďarština","Cestina"),
    Question("Hlavné mesto Čiech","Praha", "Brno","Ostrava","Plzeň"),
    Question("Hlavné mesto Nemecka","Berlín", "Hamburg","Mníchov","Dortmund"),
    Question("Rieka pretekajúca Prahou", "Vltava","Dunaj","Labe", "Hornád")


]
used_questions= []
def next_question():
    main_win.total +=1
    if len(used_questions) < len(question_list):
        cur_question = randint(0, len (question_list) -1)

        while cur_question in used_questions:
            cur_question = randint(0, len(question_list) -1)

        used_questions.append(cur_question)
    

        ask(question_list[cur_question])

    else:
        app.quit()



btn_answer1 = QRadioButton("")
btn_answer2 = QRadioButton("")
btn_answer3 = QRadioButton("")
btn_answer4 = QRadioButton("")

RadioGroup= QButtonGroup()
RadioGroup.addButton(btn_answer1)
RadioGroup.addButton(btn_answer2)
RadioGroup.addButton(btn_answer3)
RadioGroup.addButton(btn_answer4)

row = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()

col1.addWidget(btn_answer1,alignment=Qt.AlignLeft)
col1.addWidget(btn_answer2,alignment=Qt.AlignLeft)

col2.addWidget(btn_answer3,alignment=Qt.AlignLeft)
col2.addWidget(btn_answer4,alignment=Qt.AlignLeft)

row.addLayout(col1)
row.addLayout(col2)

row.setSpacing(50)

groupBox = QGroupBox("Odpovede")


groupBox.setLayout(row)


answerBox= QGroupBox("Výsledky")
result = QLabel("Správne")
row3 = QHBoxLayout()
row3.addWidget(result,alignment=Qt.AlignCenter)

answerBox.setLayout(row3)

main_layout = QVBoxLayout()
main_layout.addWidget(question, alignment= Qt.AlignCenter)
main_layout.addWidget(answerBox, alignment= Qt.AlignCenter)
main_layout.addWidget(groupBox, alignment= Qt.AlignCenter)
main_layout.addWidget(button, alignment= Qt.AlignCenter)

answerBox.hide()

def show_result():
    check_answer()
    groupBox.hide()
    answerBox.show()
    button.setText("Ďalšia otázka")


def show_question():
    answerBox.hide()
    groupBox.show()
    button.setText("Vyhodnoť")

    RadioGroup.setExclusive(False)#mozme editovat
    btn_answer1.setChecked(False)#da prec toto modre
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    RadioGroup.setExclusive(True)

    next_question()

def start_test():
    if button.text() == "Ďalšia otázka":
        show_question()
    else:
        show_result()


btns = [btn_answer1,btn_answer2,btn_answer3,btn_answer4]
def ask(q: Question):
    question.setText(q.question)
    shuffle(btns)

    btns[0].setText(q.right_answer)
    btns[1].setText(q.wrong1)
    btns[2].setText(q.wrong2)
    btns[3].setText(q.wrong3)


    result.setText(q.right_answer)
    groupBox.show()
    
def check_answer():
    if btns[0].isChecked():
        show_correct("Správne")
        main_win.score += 1
    else:
        show_correct("Nesprávne")
    
    show_stats()
    
    

def show_correct(res):
    result.setText(res)
    groupBox.hide()
    answerBox.show()

def show_stats():
    print("Štatistika")
    print("Otázok dokopy:", main_win.total)
    print("Správne odpovede:", main_win.score)
    print("Hodnotenie", main_win.score / main_win.total *100,"%" )

main_win.setLayout(main_layout)
button.clicked.connect(start_test)
next_question()
main_win.show()
app.exec_()
