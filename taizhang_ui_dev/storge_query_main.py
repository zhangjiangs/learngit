import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QMainWindow
import pymysql
import storge_query
from functools import partial

def query(ui):
    input = ui.leftLine.toPlainText()
    db = pymysql.connect(host='10.6.2.112',
                         user='root',
                         password='HTjt_6032',
                         database='taizhang')
    cursor = db.cursor()
    sql = "CALL taizhang.query_ip(%s)"
    try:
        cursor.execute(sql,input)
        result = cursor.fetchone()        
    except:
        print ("Error: unable to fetch data")
    db.close()
    print (result)
#    x = 0
    a = len(result)
    for i in range(a):
        ui.result_table.setItem(i, 0, QtWidgets.QTableWidgetItem(str(result[i])))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = storge_query.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.query.clicked.connect(partial(query, ui))
    sys.exit(app.exec_())
