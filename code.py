import sys
from PyQt5.QtWidgets import QApplication, QDialog, QProgressBar, QPushButton
from PyQt5.QtCore import QThread, pyqtSignal

# x = int(input("> "))
x = 10000


class MyThread(QThread):
    counter = pyqtSignal(int)

    def run(self):
        n1, n2 = 0, 1
        if x <= 0:
            print("Please enter a positive integer")
        elif x == 1:
            print("Fibonacci sequence upto", x, ":")
            print(n1)
        else:
            file = open("fibs.txt", "w")
            for j in range(x):
                file.write(f"{n1}\n")
                self.counter.emit(j)
                nth = n1 + n2
                n1 = n2
                n2 = nth


class Actions(QDialog):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Progress Bar')
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)
        self.pbar.setMaximum(x-1)
        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)
        self.setGeometry(300, 300, 280, 170)
        self.show()

    def doAction(self):
        self.calc = MyThread()
        self.calc.counter.connect(self.onChanged)
        self.calc.start()

    def onChanged(self, value):
        self.pbar.setValue(value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Actions()
    sys.exit(app.exec_())