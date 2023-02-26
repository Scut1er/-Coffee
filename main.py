import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
import sqlite3


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        QMainWindow.setFixedSize(self, 800, 600)
        self.tableWidget.setColumnWidth(0, 10)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 110)
        self.tableWidget.setColumnWidth(3, 120)
        self.tableWidget.setColumnWidth(4, 265)
        self.tableWidget.setColumnWidth(5, 60)
        self.tableWidget.setColumnWidth(6, 100)
        self.rendering()

    def rendering(self):
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        request = "SELECT * FROM coffee_table"
        rows = cur.execute("SELECT COUNT(*) from coffee_table").fetchone()
        self.tableWidget.setRowCount(rows[0])
        counter = 0
        for row in cur.execute(request):
            self.tableWidget.setItem(counter, 0, QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(counter, 1, QTableWidgetItem(row[1]))
            self.tableWidget.setItem(counter, 2, QTableWidgetItem(str(row[2])))
            self.tableWidget.setItem(counter, 3, QTableWidgetItem(row[3]))
            self.tableWidget.setItem(counter, 4, QTableWidgetItem(row[4]))
            self.tableWidget.setItem(counter, 5, QTableWidgetItem(str(row[5])))
            self.tableWidget.setItem(counter, 6, QTableWidgetItem(str(row[6])))
            counter += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
