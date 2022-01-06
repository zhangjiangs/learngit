import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
import pymysql
import db_query
from functools import partial

def query(ui):
    input = ui.leftLine.toPlainText()
    db = pymysql.connect(host='10.6.2.112',
                         user='root',
                         password='HTjt_6032',
                         database='taizhang')
    cursor = db.cursor()
    sql = "CALL taizhang.query_db(%s)"
    try:
        cursor.execute(sql,input)
        result = cursor.fetchall()        
    except:
        print ("Error: unable to fetch data")
    db.close()
    print (result)
    ui.result_table.clearContents()
    x = 0
    for i in result:
        y = 0
        for j in i:
            ui.result_table.setItem(x, y, QtWidgets.QTableWidgetItem(str(result[x][y])))
            y = y + 1
        x = x + 1

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = db_query.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.query.clicked.connect(partial(query, ui))
    sys.exit(app.exec_())
