import re
import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
class Main(QDialog):
    global array7
    array7 = []
    global itrpr
    itrpr = 0
    global itrrow
    itrrow = 0

    def __init__(self):
        super(Main, self).__init__()
        loadUi('Form.ui', self)
        self.setWindowTitle('Работа с файлами в Python')
        self.pushButton_run.clicked.connect(self.run)
        self.pushButton_clean.clicked.connect(self.clean)
        self.pushButton_load.clicked.connect(self.load)
        self.pushButton_export.clicked.connect(self.export)

    def export(self):
        out_file = open(u'input-Output.txt', 'w')  # открываем файл в режиме записи
        for row in array7:  # перебираем каждую строку массива
            for num in row:  # перебираем каждое значение строки
                out_file.write("%d " % num)  # записываем это значение
            out_file.write('\n')  # дописываем перевод на новую строку

    def run(self):
        fm = self.find_max()
        fmin = self.find_min()
        self.textEdit_array.insertPlainText('Max = ' + str(fm[0]) + ' [' + str(fm[1]) + ',' + str(fm[2]) + ']\n' + '\n')
        self.textEdit_array.insertPlainText('Min = ' + str(fmin[0]) + ' [' + str(fmin[1]) + ',' + str(fmin[2]) + ']\n' + '\n')
        sum = self.find_sum()
        l = len(str(sum))
        self.textEdit_array.insertPlainText('Sum = ' + str(sum) + '\n' + '\n')
        if sum > 100:
            itr = 0
            for i in array7:
                for j in i:
                    row = itr
                    col = i.index(j)
                    if col == 2:
                        array7[row][col] /= 2
                itr += 1

            array7[fm[1]][fm[2]] = fmin[0]
            array7[fmin[1]][fmin[2]] = fm[0]

        for i in array7:
            for j in i:
                l2 = len(str(j))
                l1 = l - l2 + 3
                s = ""
                for i in range(l1):
                    s += " "
                self.textEdit_array.insertPlainText(str(j) + s)
            self.textEdit_array.insertPlainText('\n')
        return array7

    def find_sum(self):
        sum = 0
        i = 0
        while i <= itrrow:
            for j in range(itrpr + 1):
                sum += array7 [i][j]
            i += 1
        return sum

    def find_max(self):
        col = 0
        row = 0
        itr = 0
        max_num = 0
        for i in array7:
            for j in i:
                if j > max_num:
                    max_num = j
                    row = itr
                    col = i.index(j)
            itr += 1
        return [max_num, row, col]

    def find_min(self):
        col = 0
        row = 0
        itr = 0
        min_num = 100
        for i in array7:
            for j in i:
                if j < min_num:
                    min_num = j
                    row = itr
                    col = i.index(j)
            itr += 1
        return [min_num, row, col]

    def clean(self):
        self.textEdit_array.setPlainText('')
        global itrpr
        itrpr = 0
        global itrrow
        itrrow = 0
        global array7
        array7 = []

    def load(self):
        global path_to_file
        path_to_file = QFileDialog.getOpenFileName(self, 'Открыть файл', '',
                                                   "Text Files (*.txt)")[0]

        if path_to_file:
            file = open(path_to_file, 'r')

            f = file.read()
            # выводим считанные данные на экран
            self.textEdit_array.insertPlainText("Полученные данные: \n" +
                                               f + "\n")

            array = []
            for num in re.findall(r'\b[0-9]+\b', f):
                array.append(num)
            sub = []
            global itrpr
            global itrrow

            for x in f:
                if (x == "\n"):
                    itrrow += 1

            print(f)
            for x in f:
                if (x == "\n"):
                    break
                elif (x == " "):
                    itrpr += 1

            print(itrpr)
            print(itrrow)

            for i in array:
                sub.append(int(i))
                if len(sub) > itrpr:
                    array7.append(sub)
                    sub = []
        print(array7)


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()