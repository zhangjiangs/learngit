# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
import pymysql
import delete
from functools import partial


class deletewindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(deletewindow, self).__init__()
        self.setupUi(self)

    def vm(self):
        input1 = self.textEdit_1.toPlainText()
        db = pymysql.connect(host='10.6.2.112',
                             user='root',
                             password='HTjt_6032',
                             database='taizhang')
        cursor = db.cursor()
        sql_1 = "select id from virtual_manchine where ip = %s"
        sql_2 = "DELETE from vm_pw where vm_id = %s"
        sql_3 = "delete from virtual_manchine where ip = %s"
        try:
            cursor.execute(sql_1, input1)
            result_1 = cursor.fetchone()
            print("找出要删除的虚拟机ID是：", result_1)
            db.commit()
            choose_1 = QMessageBox.warning(None, '警告', "你确定要删除IP为%s的虚拟机信息吗？！" % input1,
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if choose_1 == QMessageBox.Yes:
                print(choose_1)
                cursor.execute(sql_2, result_1)
                db.commit()
                cursor.execute(sql_3, input1)
                db.commit()
                print("虚拟机信息删除成功")
                QMessageBox.information(None, '消息', '虚拟机信息删除成功', QMessageBox.Yes)
            else:
                print(choose_1)
                pass
        except:
            print("虚拟机信息删除失败，请检查IP地址是否输入正确……")
            db.rollback()
            QMessageBox.warning(None, '警告', "虚拟机信息删除失败，请检查IP地址是否输入正确……", QMessageBox.Yes)
        db.close()

    def database(self):
        input2 = self.textEdit_2.toPlainText()
        db = pymysql.connect(host='10.6.2.112',
                             user='root',
                             password='HTjt_6032',
                             database='taizhang')
        cursor = db.cursor()
        sql_4 = "select dbcl_id from database_info where host_ip = %s"
        sql_5 = "DELETE from db_cluster where id = %s"
        sql_6 = "delete from database_pw where dbcl_id = %s"
        sql_7 = "delete from database_info where host_ip = %s"
        try:
            cursor.execute(sql_4, input2)
            result_2 = cursor.fetchone()
            print("找出要删除的数据库ID是：", result_2)
            db.commit()
            choose_2 = QMessageBox.warning(None, '警告', "你确定要删除IP为%s的数据库信息吗？！" % input2,
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if choose_2 == QMessageBox.Yes:
                print(choose_2)
                cursor.execute(sql_5, result_2)
                db.commit()
                cursor.execute(sql_6, result_2)
                db.commit()
                cursor.execute(sql_7, input2)
                db.commit()
                print("数据库信息删除成功")
                QMessageBox.information(None, '消息', '数据库信息删除成功', QMessageBox.Yes)
            else:
                print(choose_2)
                pass
        except:
            print("数据库信息删除失败，请检查IP地址是否输入正确……")
            db.rollback()
            QMessageBox.warning(None, '警告', "数据库信息删除失败，请检查IP地址是否输入正确……", QMessageBox.Yes)
        db.close()

    def project_owner(self):
        input3 = self.textEdit_3.toPlainText()
        db = pymysql.connect(host='10.6.2.112',
                             user='root',
                             password='HTjt_6032',
                             database='taizhang')
        cursor = db.cursor()
        sql_8 = "delete from project_owner where project_name = %s"
        try:
            choose_3 = QMessageBox.warning(None, '警告', "你确定要删除%s项目吗？！" % input3, QMessageBox.Yes | QMessageBox.No,
                                           QMessageBox.Yes)
            if choose_3 == QMessageBox.Yes:
                print(choose_3)
                a = cursor.execute(sql_8, input3)
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
            db.rollback()
            QMessageBox.warning(None, '警告', '%s项目相关信息删除失败，请检查……' % input3, QMessageBox.Yes)
        db.close()

    def vcenter_cluster(self):
        input4 = self.textEdit_4.toPlainText()
        db = pymysql.connect(host='10.6.2.112',
                             user='root',
                             password='HTjt_6032',
                             database='taizhang')
        cursor = db.cursor()
        sql_9 = "delete from vcenter_cluster  where cluster_name = %s"
        try:
            choose_4 = QMessageBox.warning(None, '警告', "你确定要删除%s虚拟化集群吗？！" % input4, QMessageBox.Yes | QMessageBox.No,
                                           QMessageBox.Yes)
            if choose_4 == QMessageBox.Yes:
                print(choose_4)
                a = cursor.execute(sql_9, input4)
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
            print("%s虚拟化集群相关信息删除失败，请检查……", input4)
            db.rollback()
            QMessageBox.warning(None, '警告', '%s虚拟化集群相关信息删除失败，请检查……' % input4, QMessageBox.Yes)
        db.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    insertMainWindow = QMainWindow()
    self = delete.Ui_MainWindow()
    self.setupUi(insertMainWindow)
    insertMainWindow.show()
    self.deletebutton_1.clicked.connect(partial(deletewindow.vm, self))
    self.deletebutton_2.clicked.connect(partial(deletewindow.database, self))
    self.deletebutton_3.clicked.connect(partial(deletewindow.project_owner, self))
    self.deletebutton_4.clicked.connect(partial(deletewindow.vcenter_cluster, self))
    sys.exit(app.exec_())
