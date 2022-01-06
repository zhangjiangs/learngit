# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
import pymysql
import insert
from functools import partial
from itertools import chain


class insertwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(insertwindow, self).__init__()
        self.setupUi(self)

    def vm(self):
        input1 = self.input_1.toPlainText()
        input2 = self.input_2.toPlainText()
        input3 = self.input_3.toPlainText()
        input4 = self.input_4.toPlainText()
        input5 = self.input_5.toPlainText()
        input6 = self.input_6.toPlainText()
        input7 = self.input_7.toPlainText()
        input8 = self.input_8.toPlainText()
        input9 = self.input_9.toPlainText()
        input10 = self.input_10.toPlainText()
        input11 = self.input_11.toPlainText()
        input12 = self.input_12.toPlainText()
        input13 = self.input_13.toPlainText()
        input14 = self.input_14.toPlainText()
        input15 = self.input_15.toPlainText()
        input16 = self.input_16.toPlainText()
        input17 = self.input_17.toPlainText()
        input18 = self.input_18.toPlainText()
        input_list1 = [input1, input2, input3, input4, input5, input6, input7, input8, input9, input10, input11,
                       input12,
                       input13, input14, input15, input16, input17, input18]
        db = pymysql.connect(host='10.6.2.112',
                             user='root',
                             password='HTjt_6032',
                             database='taizhang')
        cursor = db.cursor()
        sql_1 = "call taizhang.insert_vm(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        sql_2 = "select DISTINCT cluster_name from vcenter_cluster"
        sql_3 = "select DISTINCT project_name from project_owner"
        sql_4 = "select DISTINCT company_name from project_owner"
        try:
            cursor.execute(sql_2)
            cluster_name = cursor.fetchall()
            cluster_name_list = list(chain.from_iterable(cluster_name))
            cursor.execute(sql_3)
            project_name = cursor.fetchall()
            project_name_list = list(chain.from_iterable(project_name))
            cursor.execute(sql_4)
            company_name = cursor.fetchall()
            company_name_list = list(chain.from_iterable(company_name))
            print(cluster_name_list)
            print(project_name_list)
            print(company_name_list)
            if input_list1[0] in cluster_name_list and input_list1[1] in project_name_list and input_list1[2] in company_name_list:
                cursor.execute(sql_1, input_list1)
                print("信息输入成功……")
                db.commit()
                QMessageBox.information(None, '消息', '虚拟机信息录入成功……', QMessageBox.Yes)
            else:
                QMessageBox.warning(None, '警告', "虚拟机信息录入失败，请检查集群名称、项目名称、公司名称是否输入正确……", QMessageBox.Yes)
        except:
            print("信息输入失败，请检查……")
            db.rollback()
            QMessageBox.warning(None, '警告', "虚拟机信息录入失败，请检查……", QMessageBox.Yes)
        db.close()

    def database(self):
        input19 = self.input_19.toPlainText()
        input20 = self.input_20.toPlainText()
        input21 = self.input_21.toPlainText()
        input22 = self.input_22.toPlainText()
        input23 = self.input_23.toPlainText()
        input24 = self.input_24.toPlainText()
        input25 = self.input_25.toPlainText()
        input26 = self.input_26.toPlainText()
        input27 = self.input_27.toPlainText()
        input28 = self.input_28.toPlainText()
        input_list2 = [input19, input20, input21, input22, input23, input24, input25, input26, input27, input28]
        db = pymysql.connect(host='10.6.2.112',
                             user='root',
                             password='HTjt_6032',
                             database='taizhang')
        cursor = db.cursor()
        sql_5 = "call taizhang.insert_db(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        sql_6 = "select DISTINCT db_type from database_info"
        try:
            cursor.execute(sql_6)
            db_type = cursor.fetchall()
            db_type_list = list(chain.from_iterable(db_type))
            print(db_type_list)
            if input_list2[4] in db_type_list:
                cursor.execute(sql_5, input_list2)
                print("信息插入成功……")
                print(input_list2)
                QMessageBox.information(None, '消息', '数据库信息录入成功……', QMessageBox.Yes)
                db.commit()
            else:
                QMessageBox.warning(None, '警告', "数据库信息录入失败，请检查数据库类型是否输入正确……", QMessageBox.Yes)
        except:
            print("信息插入失败，请检查……")
            QMessageBox.warning(None, '警告', "数据库信息录入失败，请检查……", QMessageBox.Yes)
            db.rollback()
        db.close()

    def vcenter_cluster(self):
        input29 = self.input_29.toPlainText()
        input30 = self.input_30.toPlainText()
        input_list3 = [input29, input30]
        print(input_list3)
        db = pymysql.connect(host='10.6.2.112',
                             user='root',
                             password='HTjt_6032',
                             database='taizhang')
        cursor = db.cursor()
        sql_7 = "insert into vcenter_cluster (vcenter_name,cluster_name) values(%s,%s);"
        try:
            cursor.execute(sql_7, input_list3)
            print("信息插入成功……")
            print(input_list3)
            QMessageBox.information(None, '消息', '虚拟化环境及集群信息录入成功……', QMessageBox.Yes)
            db.commit()
        except:
            print("信息插入失败，请检查……")
            QMessageBox.warning(None, '警告', "虚拟化环境及集群信息录入失败，请检查……", QMessageBox.Yes)
            db.rollback()
        db.close()

    def project_owner(self):
        input31 = self.input_31.toPlainText()
        input32 = self.input_32.toPlainText()
        input33 = self.input_33.toPlainText()
        input_list4 = [input31, input32, input33]
        print(input_list4)
        db = pymysql.connect(host='10.6.2.112',
                             user='root',
                             password='HTjt_6032',
                             database='taizhang')
        cursor = db.cursor()
        sql_8 = "insert into project_owner (project_name,company_name,owner_team) values(%s,%s,%s);"
        try:
            cursor.execute(sql_8, input_list4)
            print("信息插入成功……")
            print(input_list4)
            QMessageBox.information(None, '消息', '项目、公司、负责小组信息录入成功……', QMessageBox.Yes)
            db.commit()
        except:
            print("信息插入失败，请检查……")
            QMessageBox.warning(None, '警告', "项目、公司、负责小组信息录入失败，请检查……", QMessageBox.Yes)
            db.rollback()
        db.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    insertMainWindow = QMainWindow()
    self = insert.Ui_MainWindow()
    self.setupUi(insertMainWindow)
    insertMainWindow.show()
    self.commit_1.clicked.connect(partial(insertwindow.vm, self))
    self.commit_2.clicked.connect(partial(insertwindow.database, self))
    self.commit_3.clicked.connect(partial(insertwindow.vcenter_cluster, self))
    self.commit_4.clicked.connect(partial(insertwindow.project_owner, self))
    sys.exit(app.exec_())
