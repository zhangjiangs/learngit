# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
from itertools import chain
from vm_query import Ui_MainWindow as v_ui
from db_query import Ui_MainWindow as d_ui
from storge_query import Ui_MainWindow as s_ui
from hello import Ui_MainWindow as h_ui
from cluster_query import Ui_MainWindow as c_ui
from insert import Ui_MainWindow as i_ui
from delete import Ui_MainWindow as de_ui
import pymysql

warning_1 = '数据查询失败...请检查网络或者数据库状态是否正常...'

sql_1 = "CALL taizhang.query_ip(%s)"
sql_2 = "CALL taizhang.query_db(%s)"
sql_3 = "CALL taizhang.query_ip(%s)"

sql_4 = "select DISTINCT vcenter_name from vcenter_cluster"
sql_5 = "select DISTINCT cluster_name from vcenter_cluster"
sql_6 = "select DISTINCT project_name from project_owner"
sql_7 = "select DISTINCT company_name from project_owner"
sql_8 = "select DISTINCT db_type from database_info"

sql_9 = "call taizhang.insert_vm(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
sql_10 = "select DISTINCT cluster_name from vcenter_cluster"
sql_11 = "select DISTINCT project_name from project_owner"
sql_12 = "select DISTINCT company_name from project_owner"

sql_13 = "call taizhang.insert_db(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
sql_14 = "select DISTINCT db_type from database_info"

sql_15 = "insert into vcenter_cluster (vcenter_name,cluster_name) values(%s,%s);"

sql_16 = "insert into project_owner (project_name,company_name,owner_team) values(%s,%s,%s);"

sql_17 = "select id from virtual_manchine where ip = %s"
# sql_18 = "DELETE from vm_pw where vm_id = %s"
# sql_19 = "delete from virtual_manchine where id = %s"
sql_18 = "delete vm_pw,virtual_manchine from vm_pw  left join virtual_manchine  on vm_pw.vm_id = virtual_manchine.id " \
         "where vm_pw.vm_id = %s "

sql_20 = "select dbcl_id from database_info where host_ip = %s"
sql_21 = "DELETE from db_cluster where id = %s"
sql_22 = "delete from database_pw where dbcl_id = %s"
sql_23 = "delete from database_info where host_ip = %s"

sql_24 = "delete from project_owner where project_name = %s"

sql_25 = "delete from vcenter_cluster  where cluster_name = %s"

global db, cursor


def db_connect():
    global db, cursor
    db = pymysql.connect(host='10.6.2.112',
                         user='root',
                         password='HTjt_6032',
                         database='taizhang')
    cursor = db.cursor()


# 主窗口
class hello_Window(QtWidgets.QMainWindow, h_ui):
    switch_window1 = QtCore.pyqtSignal()  # 跳转信号
    switch_window2 = QtCore.pyqtSignal()  # 跳转信号
    switch_window3 = QtCore.pyqtSignal()  # 跳转信号
    switch_window4 = QtCore.pyqtSignal()  # 跳转信号
    switch_window5 = QtCore.pyqtSignal()
    switch_window6 = QtCore.pyqtSignal()

    def __init__(self):
        super(hello_Window, self).__init__()
        self.setupUi(self)
        self.Button_1.clicked.connect(self.vm_query)
        self.Button_2.clicked.connect(self.db_query)
        self.Button_3.clicked.connect(self.storage_query)
        self.Button_4.clicked.connect(self.cluster_query)
        self.Button_5.clicked.connect(self.insert)
        self.Button_6.clicked.connect(self.delete)

    def vm_query(self):
        self.switch_window1.emit()

    def db_query(self):
        self.switch_window2.emit()

    def storage_query(self):
        self.switch_window3.emit()

    def cluster_query(self):
        self.switch_window4.emit()

    def insert(self):
        self.switch_window5.emit()

    def delete(self):
        self.switch_window6.emit()


# vm窗口
class vm_query_Window(QtWidgets.QMainWindow, v_ui):
    switch_window1 = QtCore.pyqtSignal()  # 跳转信号

    def __init__(self):
        super(vm_query_Window, self).__init__()
        self.setupUi(self)
        self.query.clicked.connect(self.q)

    def q(self):
        try:
            input_1 = self.leftLine.toPlainText()
            db_connect()
            cursor.execute(sql_1, input_1)
            result = cursor.fetchone()
            self.result_table.clearContents()
            print(result)
            a = len(result)
            for i in range(a):
                self.result_table.setItem(0, i, QtWidgets.QTableWidgetItem(str(result[i])))
        except:
            QMessageBox.warning(None, '警告', warning_1, QMessageBox.Yes)


# db窗口
class db_query_Window(QtWidgets.QMainWindow, d_ui):
    switch_window2 = QtCore.pyqtSignal()  # 跳转信号

    def __init__(self):
        super(db_query_Window, self).__init__()
        self.setupUi(self)
        self.query.clicked.connect(self.q)

    def q(self):
        try:
            input_2 = self.leftLine.toPlainText()
            db_connect()
            cursor.execute(sql_2, input_2)
            result = cursor.fetchall()
            print(result)
            self.result_table.clearContents()
            x = 0
            for i in result:
                y = 0
                for j in i:
                    self.result_table.setItem(x, y, QtWidgets.QTableWidgetItem(str(result[x][y])))
                    y = y + 1
                x = x + 1
        except:
            QMessageBox.warning(None, '警告', '查询失败，请检查网络或者台账数据库是否正常……', QMessageBox.Yes)


# storage窗口
class storage_query_Window(QtWidgets.QMainWindow, s_ui):
    switch_window3 = QtCore.pyqtSignal()  # 跳转信号

    def __init__(self):
        super(storage_query_Window, self).__init__()
        self.setupUi(self)
        self.query.clicked.connect(self.q)

    def q(self):
        try:
            input_3 = self.leftLine.toPlainText()
            db_connect()
            cursor.execute(sql_3, input_3)
            result = cursor.fetchone()
            print(result)
            self.result_table.clearContents()
            a = len(result)
            for i in range(a):
                self.result_table.setItem(0, i, QtWidgets.QTableWidgetItem(str(result[i])))
        except:
            QMessageBox.warning(None, '警告', warning_1, QMessageBox.Yes)


# cluster_query窗口
class cluster_query_Window(QtWidgets.QMainWindow, c_ui):
    switch_window4 = QtCore.pyqtSignal()  # 跳转信号

    def __init__(self):
        super(cluster_query_Window, self).__init__()
        self.setupUi(self)
        self.button_1.clicked.connect(self.vcenter_query)
        self.button_2.clicked.connect(self.cluster_name_query)
        self.button_3.clicked.connect(self.project_query)
        self.button_4.clicked.connect(self.company_query)
        self.button_5.clicked.connect(self.dbtype_query)

    def query(self, sql):
        try:
            db_connect()
            cursor.execute(sql)
            result = cursor.fetchall()
            result_list = list(chain.from_iterable(result))
            output = "\n".join(result_list)
            self.textBrowser.setPlainText(str(output))
        except:
            self.textBrowser.setPlainText(str(warning_1))

    def vcenter_query(self):
        cluster_query_Window.query(self, sql_4)

    def cluster_name_query(self):
        cluster_query_Window.query(self, sql_5)

    def project_query(self):
        cluster_query_Window.query(self, sql_6)

    def company_query(self):
        cluster_query_Window.query(self, sql_7)

    def dbtype_query(self):
        cluster_query_Window.query(self, sql_8)


# insert窗口
class insert_Window(QtWidgets.QMainWindow, i_ui):
    switch_window5 = QtCore.pyqtSignal()  # 跳转信号

    def __init__(self):
        super(insert_Window, self).__init__()
        self.setupUi(self)
        self.commit_1.clicked.connect(self.vm_insert)
        self.commit_2.clicked.connect(self.database_insert)
        self.commit_3.clicked.connect(self.vcenter_cluster_insert)
        self.commit_4.clicked.connect(self.project_owner_insert)

    def vm_insert(self):
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
                       input12, input13, input14, input15, input16, input17, input18]
        try:
            db_connect()
            cursor.execute(sql_10)
            cluster_name = cursor.fetchall()
            cluster_name_list = list(chain.from_iterable(cluster_name))
            cursor.execute(sql_11)
            project_name = cursor.fetchall()
            project_name_list = list(chain.from_iterable(project_name))
            cursor.execute(sql_12)
            company_name = cursor.fetchall()
            company_name_list = list(chain.from_iterable(company_name))
            print(cluster_name_list)
            print(project_name_list)
            print(company_name_list)
            if input_list1[0] in cluster_name_list \
                    and input_list1[1] in project_name_list \
                    and input_list1[2] in company_name_list:
                cursor.execute(sql_9, input_list1)
                print("信息输入成功……")
                db.commit()
                QMessageBox.information(None, '消息', '虚拟机信息录入成功……', QMessageBox.Yes)
            else:
                QMessageBox.warning(None, '警告', "虚拟机信息录入失败，请检查集群名称、项目名称、公司名称是否输入正确……", QMessageBox.Yes)
        except:
            print("信息输入失败，请检查……")
            QMessageBox.warning(None, '警告', "虚拟机信息录入失败，请检查输入信息是否完整、正确，网络或者台账数据库是否正常……", QMessageBox.Yes)

    def database_insert(self):
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
        try:
            db_connect()
            cursor.execute(sql_14)
            db_type = cursor.fetchall()
            db_type_list = list(chain.from_iterable(db_type))
            print(db_type_list)
            if input_list2[4] in db_type_list:
                cursor.execute(sql_13, input_list2)
                print("信息插入成功……")
                print(input_list2)
                QMessageBox.information(None, '消息', '数据库信息录入成功……', QMessageBox.Yes)
                db.commit()
            else:
                QMessageBox.warning(None, '警告', "数据库信息录入失败，请检查数据库类型是否输入正确……", QMessageBox.Yes)
        except:
            print("信息插入失败，请检查……")
            QMessageBox.warning(None, '警告', "数据库信息录入失败，请检查输入信息是否完整、正确，网络或者台账数据库是否正常……", QMessageBox.Yes)

    def vcenter_cluster_insert(self):
        input29 = self.input_29.toPlainText()
        input30 = self.input_30.toPlainText()
        input_list3 = [input29, input30]
        print(input_list3)
        try:
            db_connect()
            if input_list3 == ['', '']:
                QMessageBox.warning(None, '警告', "虚拟化环境及集群信息录入失败，您什么信息都没有输入……", QMessageBox.Yes)
            else:
                cursor.execute(sql_15, input_list3)
                print("信息插入成功……")
                print(input_list3)
                QMessageBox.information(None, '消息', '虚拟化环境及集群信息录入成功……', QMessageBox.Yes)
                db.commit()
        except:
            print("信息插入失败，请检查……")
            QMessageBox.warning(None, '警告', "虚拟化环境及集群信息录入失败，请检查网络或者台账数据库是否正常……", QMessageBox.Yes)

    def project_owner_insert(self):
        input31 = self.input_31.toPlainText()
        input32 = self.input_32.toPlainText()
        input33 = self.input_33.toPlainText()
        input_list4 = [input31, input32, input33]
        print(input_list4)
        try:
            db_connect()
            if input_list4 == ['', '', '']:
                QMessageBox.warning(None, '警告', "项目、公司、负责小组信息录入失败，您什么都没有输入……", QMessageBox.Yes)
            else:
                cursor.execute(sql_16, input_list4)
                print("信息插入成功……")
                print(input_list4)
                QMessageBox.information(None, '消息', '项目、公司、负责小组信息录入成功……', QMessageBox.Yes)
                db.commit()
        except:
            print("信息插入失败，请检查……")
            QMessageBox.warning(None, '警告', "项目、公司、负责小组信息录入失败，请检查网络或者台账数据库是否正常……", QMessageBox.Yes)


# delete 窗口
class delete_Window(QtWidgets.QMainWindow, de_ui):
    switch_window6 = QtCore.pyqtSignal()  # 跳转信号

    def __init__(self):
        super(delete_Window, self).__init__()
        self.setupUi(self)
        self.deletebutton_1.clicked.connect(self.vm_delete)
        self.deletebutton_2.clicked.connect(self.database_delete)
        self.deletebutton_3.clicked.connect(self.project_owner_delete)
        self.deletebutton_4.clicked.connect(self.vcenter_cluster_delete)

    def vm_delete(self):
        input1 = self.textEdit_1.toPlainText()
        try:
            choose_1 = QMessageBox.warning(None, '警告', "你确定要删除IP为%s的虚拟机信息吗？！" % input1,
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if choose_1 == QMessageBox.Yes:
                db_connect()
                cursor.execute(sql_17, input1)
                result = cursor.fetchone()
                print("找出要删除的虚拟机ID是：", result)
                if result is not None:
                    cursor.execute(sql_18, result)
                    db.commit()
                    print("虚拟机信息删除成功")
                    QMessageBox.information(None, '消息', '虚拟机信息删除成功', QMessageBox.Yes)
                else:
                    QMessageBox.information(None, '消息', '台账中没有IP为%s的服务器信息' % input1, QMessageBox.Yes)
            else:
                pass
        except:
            print("网络好像不可达，请检查网络状态或者台账数据库状态……")
            QMessageBox.warning(None, '警告', '网络好像不可达，请检查网络状态或者台账数据库状态……', QMessageBox.Yes)

    def database_delete(self):
        input2 = self.textEdit_2.toPlainText()
        try:
            choose_2 = QMessageBox.warning(None, '警告', "你确定要删除IP为%s的数据库信息吗？！" % input2,
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if choose_2 == QMessageBox.Yes:
                db_connect()
                cursor.execute(sql_20, input2)
                result_2 = cursor.fetchone()
                if result_2 is not None:
                    cursor.execute(sql_21, result_2)
                    cursor.execute(sql_22, result_2)
                    cursor.execute(sql_23, input2)
                    db.commit()
                    print("数据库信息删除成功")
                    QMessageBox.information(None, '消息', '数据库信息删除成功', QMessageBox.Yes)
                else:
                    QMessageBox.information(None, '消息', '台账中没有IP为%s的数据库信息' % input2, QMessageBox.Yes)
            else:
                print(choose_2)
                pass
        except:
            print("数据库信息删除失败，请检查IP地址是否输入正确……")
            QMessageBox.warning(None, '警告', "网络好像不可达，请检查网络状态或者台账数据库状态……", QMessageBox.Yes)

    def project_owner_delete(self):
        input3 = self.textEdit_3.toPlainText()
        try:
            choose_3 = QMessageBox.warning(None, '警告', "你确定要删除%s项目吗？！" % input3, QMessageBox.Yes | QMessageBox.No,
                                           QMessageBox.Yes)
            if choose_3 == QMessageBox.Yes:
                print(choose_3)
                db_connect()
                a = cursor.execute(sql_24, input3)
                db.commit()
                if a == 1:
                    print("项目相关信息删除成功")
                    QMessageBox.information(None, '消息', '%s项目相关信息删除成功' % input3, QMessageBox.Yes)
                else:
                    print("该项目不存在")
                    QMessageBox.warning(None, '警告', '%s项目相关信息在台账中不存在，请检查项目名称是否正确！' % input3, QMessageBox.Yes)
            else:
                print(choose_3)
                pass
        except:
            print("%s项目相关信息删除失败，请检查……", input3)
            QMessageBox.warning(None, '警告', '网络好像不可达，请检查网络状态或者台账数据库状态……', QMessageBox.Yes)

    def vcenter_cluster_delete(self):
        input4 = self.textEdit_4.toPlainText()
        try:
            choose_4 = QMessageBox.warning(None, '警告', "你确定要删除%s虚拟化集群吗？！" % input4, QMessageBox.Yes | QMessageBox.No,
                                           QMessageBox.Yes)
            if choose_4 == QMessageBox.Yes:
                print(choose_4)
                db_connect()
                a = cursor.execute(sql_25, input4)
                db.commit()
                if a == 1:
                    print("虚拟化集群相关信息删除成功")
                    QMessageBox.information(None, '消息', '%s虚拟化集群相关信息删除成功' % input4, QMessageBox.Yes)
                else:
                    print("该虚拟化集群不存在")
                    QMessageBox.warning(None, '警告', '%s虚拟化集群相关信息在台账中不存在，请检查虚拟化集群名称是否正确！' % input4, QMessageBox.Yes)
            else:
                print(choose_4)
                pass
        except:
            QMessageBox.warning(None, '警告', '网络好像不可达，请检查网络状态或者台账数据库状态……', QMessageBox.Yes)


# 页面跳转
class Controller:
    def __init__(self):
        self.hello = hello_Window()
        self.vm = vm_query_Window()
        self.db = db_query_Window()
        self.storage = storage_query_Window()
        self.cluster = cluster_query_Window()
        self.insert = insert_Window()
        self.delete = delete_Window()

    # 跳转到 hello 窗口
    def show_hello(self):
        self.hello = hello_Window()
        self.hello.switch_window1.connect(self.show_vm)
        self.hello.switch_window2.connect(self.show_db)
        self.hello.switch_window3.connect(self.show_storage)
        self.hello.switch_window4.connect(self.show_cluster)
        self.hello.switch_window5.connect(self.show_insert)
        self.hello.switch_window6.connect(self.show_delete)
        self.hello.show()

    # 跳转到 vm 窗口
    def show_vm(self):
        self.vm = vm_query_Window()
        self.vm.show()

    # 跳转到 db 窗口
    def show_db(self):
        self.db = db_query_Window()
        self.db.show()

    # 跳转到 storage 窗口
    def show_storage(self):
        self.storage = storage_query_Window()
        self.storage.show()

    # 跳转到 cluster 窗口
    def show_cluster(self):
        self.cluster = cluster_query_Window()
        self.cluster.show()

    # 跳转到 insert 窗口
    def show_insert(self):
        self.insert = insert_Window()
        self.insert.show()

    # 跳转到 delete 窗口
    def show_delete(self):
        self.delete = delete_Window()
        self.delete.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Controller = Controller()  # 控制器实例
    Controller.show_hello()  # 默认展示的是 hello 页面
    sys.exit(app.exec_())
