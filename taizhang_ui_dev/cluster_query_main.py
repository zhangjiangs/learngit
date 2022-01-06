# -*- coding: utf-8 -*-

import sys
from itertools import chain
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
import pymysql
import cluster_query
from functools import partial

sql_1 = "select DISTINCT vcenter_name from vcenter_cluster"
sql_2 = "select DISTINCT cluster_name from vcenter_cluster"
sql_3 = "select DISTINCT project_name from project_owner"
sql_4 = "select DISTINCT company_name from project_owner"
sql_5 = "select DISTINCT db_type from database_info"
warning = '数据查询失败...请检查网络或者数据库状态是否正常...'


class query_window(QtWidgets.QMainWindow):
    def __init__(self):
        super(query_window, self).__init__()
        self.setupUi(self)

    def query(self, sql):
        try:
            db = pymysql.connect(host='10.6.2.112',
                                 user='root',
                                 password='HTjt_6032',
                                 database='taizhang')
            cursor = db.cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
            result_list = list(chain.from_iterable(result))
            output = "\n".join(result_list)
            self.textBrowser.setPlainText(str(output))
        except:
            self.textBrowser.setPlainText(str(warning))

    def vcenter_query(self):
        query_window.query(self, sql_1)

    def cluster_name_query(self):
        query_window.query(self, sql_2)

    def project_query(self):
        query_window.query(self, sql_3)

    def company_query(self):
        query_window.query(self, sql_4)

    def dbtype_query(self):
        query_window.query(self, sql_5)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = cluster_query.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.button_1.clicked.connect(partial(query_window.vcenter_query, ui))
    ui.button_2.clicked.connect(partial(query_window.cluster_name_query, ui))
    ui.button_3.clicked.connect(partial(query_window.project_query, ui))
    ui.button_4.clicked.connect(partial(query_window.company_query, ui))
    ui.button_5.clicked.connect(partial(query_window.dbtype_query, ui))
    sys.exit(app.exec_())
