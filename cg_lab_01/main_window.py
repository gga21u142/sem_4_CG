from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QPushButton
from points import Points
from matplotwidget import MatplotlibWidget
from task_solve import *
from my_logging import Logging

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1302, 621)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1302, 621))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_input = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_input.sizePolicy().hasHeightForWidth())
        self.label_input.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        self.label_input.setFont(font)
        self.label_input.setObjectName("label_input")
        self.verticalLayout_3.addWidget(self.label_input)
        self.d_dot_switch = QtWidgets.QRadioButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.d_dot_switch.sizePolicy().hasHeightForWidth())
        self.d_dot_switch.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.d_dot_switch.setFont(font)
        self.d_dot_switch.setToolTip("")
        self.d_dot_switch.setObjectName("d_dot_switch")
        self.verticalLayout_3.addWidget(self.d_dot_switch)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_x = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_x.sizePolicy().hasHeightForWidth())
        self.label_x.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_x.setFont(font)
        self.label_x.setObjectName("label_x")
        self.horizontalLayout_2.addWidget(self.label_x)
        self.line_crd_x = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_crd_x.sizePolicy().hasHeightForWidth())
        self.line_crd_x.setSizePolicy(sizePolicy)
        self.line_crd_x.setMinimumSize(QtCore.QSize(414, 34))
        self.line_crd_x.setMaximumSize(QtCore.QSize(414, 34))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.line_crd_x.setFont(font)
        self.line_crd_x.setText("")
        self.line_crd_x.setObjectName("line_crd_x")
        self.horizontalLayout_2.addWidget(self.line_crd_x)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_y = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_y.sizePolicy().hasHeightForWidth())
        self.label_y.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_y.setFont(font)
        self.label_y.setObjectName("label_y")
        self.horizontalLayout_3.addWidget(self.label_y)
        self.line_crd_y = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_crd_y.sizePolicy().hasHeightForWidth())
        self.line_crd_y.setSizePolicy(sizePolicy)
        self.line_crd_y.setMinimumSize(QtCore.QSize(414, 34))
        self.line_crd_y.setMaximumSize(QtCore.QSize(414, 34))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.line_crd_y.setFont(font)
        self.line_crd_y.setText("")
        self.line_crd_y.setObjectName("line_crd_y")
        self.horizontalLayout_3.addWidget(self.line_crd_y)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.btn_dot_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_dot_add.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_dot_add.sizePolicy().hasHeightForWidth())
        self.btn_dot_add.setSizePolicy(sizePolicy)
        self.btn_dot_add.setMaximumSize(QtCore.QSize(448, 50))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(20)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.btn_dot_add.setFont(font)
        self.btn_dot_add.setToolTip("")
        self.btn_dot_add.setAutoDefault(False)
        self.btn_dot_add.setDefault(False)
        self.btn_dot_add.setFlat(False)
        self.btn_dot_add.setObjectName("btn_dot_add")
        self.verticalLayout_3.addWidget(self.btn_dot_add)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btn_dot_delete = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_dot_delete.sizePolicy().hasHeightForWidth())
        self.btn_dot_delete.setSizePolicy(sizePolicy)
        self.btn_dot_delete.setMinimumSize(QtCore.QSize(220, 66))
        self.btn_dot_delete.setMaximumSize(QtCore.QSize(220, 66))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_dot_delete.setFont(font)
        self.btn_dot_delete.setObjectName("btn_dot_delete")
        self.horizontalLayout_6.addWidget(self.btn_dot_delete)
        self.btn_dot_change = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_dot_change.sizePolicy().hasHeightForWidth())
        self.btn_dot_change.setSizePolicy(sizePolicy)
        self.btn_dot_change.setMinimumSize(QtCore.QSize(220, 66))
        self.btn_dot_change.setMaximumSize(QtCore.QSize(220, 66))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_dot_change.setFont(font)
        self.btn_dot_change.setObjectName("btn_dot_change")
        self.horizontalLayout_6.addWidget(self.btn_dot_change)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_undo = QtWidgets.QPushButton(self.centralwidget)
        self.btn_undo.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_undo.sizePolicy().hasHeightForWidth())
        self.btn_undo.setSizePolicy(sizePolicy)
        self.btn_undo.setMinimumSize(QtCore.QSize(220, 66))
        self.btn_undo.setMaximumSize(QtCore.QSize(220, 66))
        font = QtGui.QFont()
        font.setFamily("MS PMincho")
        font.setPointSize(36)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.btn_undo.setFont(font)
        self.btn_undo.setAutoDefault(False)
        self.btn_undo.setDefault(False)
        self.btn_undo.setFlat(False)
        self.btn_undo.setObjectName("btn_undo")
        self.horizontalLayout_4.addWidget(self.btn_undo)
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy)
        self.btn_clear.setMinimumSize(QtCore.QSize(220, 66))
        self.btn_clear.setMaximumSize(QtCore.QSize(220, 66))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_clear.setFont(font)
        self.btn_clear.setObjectName("btn_clear")
        self.horizontalLayout_4.addWidget(self.btn_clear)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.btn_all = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_all.sizePolicy().hasHeightForWidth())
        self.btn_all.setSizePolicy(sizePolicy)
        self.btn_all.setMinimumSize(QtCore.QSize(449, 55))
        self.btn_all.setMaximumSize(QtCore.QSize(449, 55))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_all.setFont(font)
        self.btn_all.setObjectName("btn_all")
        self.verticalLayout_3.addWidget(self.btn_all)
        self.btn_answer = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_answer.sizePolicy().hasHeightForWidth())
        self.btn_answer.setSizePolicy(sizePolicy)
        self.btn_answer.setMinimumSize(QtCore.QSize(449, 44))
        self.btn_answer.setMaximumSize(QtCore.QSize(449, 44))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_answer.setFont(font)
        self.btn_answer.setObjectName("btn_answer")
        self.verticalLayout_3.addWidget(self.btn_answer)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_d = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_d.sizePolicy().hasHeightForWidth())
        self.label_d.setSizePolicy(sizePolicy)
        self.label_d.setMinimumSize(QtCore.QSize(55, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        self.label_d.setFont(font)
        self.label_d.setObjectName("label_d")
        self.verticalLayout_4.addWidget(self.label_d)
        self.table_dot_D = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_dot_D.sizePolicy().hasHeightForWidth())
        self.table_dot_D.setSizePolicy(sizePolicy)
        self.table_dot_D.setMinimumSize(QtCore.QSize(266, 60))
        self.table_dot_D.setMaximumSize(QtCore.QSize(266, 60))
        self.table_dot_D.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table_dot_D.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table_dot_D.setAutoScroll(False)
        self.table_dot_D.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table_dot_D.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_dot_D.setObjectName("table_dot_D")
        self.table_dot_D.setColumnCount(2)
        self.table_dot_D.setRowCount(0)
        self.table_dot_D.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        item = QtWidgets.QTableWidgetItem()
        self.table_dot_D.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_dot_D.setHorizontalHeaderItem(1, item)
        self.verticalLayout_4.addWidget(self.table_dot_D)
        self.label_a = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_a.sizePolicy().hasHeightForWidth())
        self.label_a.setSizePolicy(sizePolicy)
        self.label_a.setMinimumSize(QtCore.QSize(55, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        self.label_a.setFont(font)
        self.label_a.setObjectName("label_a")
        self.verticalLayout_4.addWidget(self.label_a)
        self.table_dots_A = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_dots_A.sizePolicy().hasHeightForWidth())
        self.table_dots_A.setSizePolicy(sizePolicy)
        self.table_dots_A.setMinimumSize(QtCore.QSize(266, 408))
        self.table_dots_A.setMaximumSize(QtCore.QSize(266, 16777215))
        self.table_dots_A.setStatusTip("")
        self.table_dots_A.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.table_dots_A.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table_dots_A.setAutoScroll(False)
        self.table_dots_A.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table_dots_A.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_dots_A.setObjectName("table_dots_A")
        self.table_dots_A.setColumnCount(2)
        self.table_dots_A.setRowCount(0)
        self.table_dots_A.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        item = QtWidgets.QTableWidgetItem()
        self.table_dots_A.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_dots_A.setHorizontalHeaderItem(1, item)
        self.verticalLayout_4.addWidget(self.table_dots_A)
    
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout_canvas = QtWidgets.QVBoxLayout()
        self.verticalLayout_canvas.setObjectName("verticalLayout_canvas")
        # self.widget_canvas = QtWidgets.QWidget(self.centralwidget)
        # self.widget_canvas.setMinimumSize(QtCore.QSize(543, 546))
        # self.widget_canvas.setObjectName("widget_canvas")
        #self.verticalLayout_canvas.addWidget(self.widget_canvas)
        self.gridLayout.addLayout(self.verticalLayout_canvas, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1302, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.author = QtWidgets.QAction(MainWindow)
        self.author.setObjectName("author")
        self.text = QtWidgets.QAction(MainWindow)
        self.text.setCheckable(False)
        self.text.setMenuRole(QtWidgets.QAction.AboutRole)
        self.text.setObjectName("text")
        self.menu.addAction(self.text)
        self.menu.addAction(self.author)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Геометрические преобразования.  Задача 1."))
        self.label_input.setText(_translate("MainWindow", "Ввести точку:"))
        self.d_dot_switch.setStatusTip(_translate("MainWindow", "Включен - вводится точка D, выключен - точка мн-ва A."))
        self.d_dot_switch.setText(_translate("MainWindow", "Точка D"))
        self.label_x.setText(_translate("MainWindow", "X:"))
        self.label_y.setText(_translate("MainWindow", "Y:"))
        self.btn_dot_add.setStatusTip(_translate("MainWindow", "Добавляет точку в таблицу."))
        self.btn_dot_add.setText(_translate("MainWindow", "►"))
        self.btn_dot_delete.setStatusTip(_translate("MainWindow", "Выводит окно графики."))
        self.btn_dot_delete.setText(_translate("MainWindow", "Удалить точку"))
        self.btn_dot_change.setStatusTip(_translate("MainWindow", "Выводит окно графики."))
        self.btn_dot_change.setText(_translate("MainWindow", "Изменить точку"))
        self.btn_undo.setStatusTip(_translate("MainWindow", "Отменяет предыдущую операцию."))
        self.btn_undo.setText(_translate("MainWindow", "←"))
        self.btn_clear.setStatusTip(_translate("MainWindow", "Очищает таблицу и окно графики."))
        self.btn_clear.setText(_translate("MainWindow", "Очистить"))
        self.btn_all.setStatusTip(_translate("MainWindow", "Строит все возможные параллелограммы."))
        self.btn_all.setText(_translate("MainWindow", "Построить все\n"
"параллелограммы"))
        self.btn_answer.setStatusTip(_translate("MainWindow", "Строит 2 параллелограмма, площаль пересечения которых максимальна."))
        self.btn_answer.setText(_translate("MainWindow", "Решение"))
        self.label_d.setText(_translate("MainWindow", "Координата точки D:"))
        item = self.table_dot_D.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "X"))
        item = self.table_dot_D.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Y"))
        self.label_a.setText(_translate("MainWindow", "Координаты точек мн-ва A:"))
        item = self.table_dots_A.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "X"))
        item = self.table_dots_A.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Y"))
        self.menu.setTitle(_translate("MainWindow", "Инфо"))
        self.author.setText(_translate("MainWindow", "Об авторе"))
        self.text.setText(_translate("MainWindow", "О программе"))



    def setupDefault(self):
        self.canvas_w = None
        self.task_points = Points()

        self.canvas_point_D = None
        self.canvas_points = list()
        self.selected_point = None
        self.is_selected = False
        
        self.Parallels = list()
        self.canvas_parallels = list()

        self.condition = [self.task_points.dots_A.copy(), 
                          self.task_points.dot_D.copy(), 
                          self.Parallels.copy(), 
                          self.canvas_parallels.copy()]
        self.logs = Logging()

        self.logs.update_log(self.condition)



        self.author.triggered.connect(self.about_author)
        self.text.triggered.connect(self.about_task)
        self.btn_dot_add.clicked.connect(self.btn_add_dot)
        self.btn_dot_delete.clicked.connect(self.btn_delete_dot)
        self.btn_dot_change.clicked.connect(self.btn_change_dot)
        self.btn_clear.clicked.connect(self.cleanse)
        self.table_dots_A.cellClicked.connect(self.table_A_selected)
        self.table_dot_D.cellClicked.connect(self.table_D_selected)
        self.btn_all.clicked.connect(self.draw_all_parallels)
        self.btn_answer.clicked.connect(self.draw_solution)
        self.btn_undo.clicked.connect(self.btn_undo_log)

        self.init_canvas()


    def about_author(self):
        info_author = QMessageBox()
        info_author.setWindowTitle("Об авторе")
        info_author.setText("\tСтудент ИУ7-44Б\t\n\tГареев Г. А.\t")
        info_author.setDefaultButton(QMessageBox.Ok)

        info_author.exec_()
    
    def about_task(self):
        info_task = QMessageBox()
        info_task.setWindowTitle("Условие задачи")
        info_task.setText("На плоскости заданы множество точек А и точка d вне\t\nего. Подсчитать количество (неупорядоченных)\t\nразличных троек точек a, b, c из А таких, что\t\nчетырехугольник abcd является параллелограммом.\t\nВывести два параллелограмма, площадь пересечения\t\nкоторых наибольшая.\n\t\t\t\t\tВерсия 1.0.0\t")
        info_task.setDefaultButton(QMessageBox.Ok)

        info_task.exec_()

    def closeEvent(self, event):
        # Переопределить colseEvent
        reply = QMessageBox.question\
        (MainWindow, 'Вы нажали на крестик',
            "Вы уверены, что хотите уйти?",
             QMessageBox.Yes,
             QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


    def btn_add_dot(self):
        coord_x = self.line_crd_x.text()
        self.line_crd_x.clear()
        coord_y = self.line_crd_y.text()
        self.line_crd_y.clear()
        
        try:
            coord_x = round(float(coord_x), 6)
            coord_y = round(float(coord_y), 6)
        except:
            error = QMessageBox()
            error.setWindowTitle("Ошибка!")
            error.setText("Введены некорректные координаты!")
            error.setDefaultButton(QMessageBox.Ok)
            error.setIcon(QMessageBox.Warning)

            error.exec_()
        else:
            if self.d_dot_switch.isChecked():
                self.task_points.change_dot_D([coord_x, coord_y])
                self.table_dot_D.setRowCount(1)
                self.table_dot_D.setItem(0, 0, QTableWidgetItem(str(coord_x)))
                self.table_dot_D.setItem(0, 1, QTableWidgetItem(str(coord_y)))
                self.d_dot_switch.setChecked(False)
            elif [coord_x, coord_y] not in self.task_points.dots_A:
                self.task_points.add_dot_A([coord_x, coord_y])
                self.table_dots_A.setRowCount(self.task_points.count_dots_A())
                self.table_dots_A.setItem(self.task_points.count_dots_A() - 1, 0, QTableWidgetItem(str(coord_x)))
                self.table_dots_A.setItem(self.task_points.count_dots_A() - 1, 1, QTableWidgetItem(str(coord_y)))
            
            self.refresh_canvas()
            self.update_condition()
            self.logs.update_log(self.condition)
            print(self.condition)
            
    def btn_delete_dot(self):
        if self.d_dot_switch.isChecked():
            self.task_points.delete_dot_D()
            self.table_dot_D.removeRow(0)
            self.d_dot_switch.setChecked(False)
        else:
            i = self.table_dots_A.currentRow()
            if i >= 0:
                self.task_points.delete_dot_A(i)
                self.table_dots_A.removeRow(i)
                self.table_dots_A.setRowCount(self.task_points.count_dots_A())
        
        self.refresh_canvas_parallels()
        self.refresh_canvas()
        self.update_condition()
        self.logs.update_log(self.condition)
        print(self.condition)

    def btn_change_dot(self):
        coord_x = self.line_crd_x.text()
        self.line_crd_x.clear()
        coord_y = self.line_crd_y.text()
        self.line_crd_y.clear()
        
        try:
            coord_x = float(coord_x)
            coord_y = float(coord_y)
        except:
            error = QMessageBox()
            error.setWindowTitle("Ошибка!")
            error.setText("Введены некорректные координаты!")
            error.setDefaultButton(QMessageBox.Ok)
            error.setIcon(QMessageBox.Warning)
            error.exec_()
        else:
            if self.d_dot_switch.isChecked():
                self.table_dot_D.setRowCount(1)
                self.task_points.change_dot_D([coord_x, coord_y])
                self.table_dot_D.setItem(0, 0, QTableWidgetItem(str(coord_x)))
                self.table_dot_D.setItem(0, 1, QTableWidgetItem(str(coord_y)))
                self.d_dot_switch.setChecked(False)
            else:
                i = self.table_dots_A.currentRow()
                if i >= 0 and [coord_x, coord_y] not in self.task_points.dots_A:
                    self.task_points.change_dot_A(i, [coord_x, coord_y])
                    self.table_dots_A.setItem(i, 0, QTableWidgetItem(str(coord_x)))
                    self.table_dots_A.setItem(i, 1, QTableWidgetItem(str(coord_y)))
            
            self.refresh_canvas_parallels()
            self.refresh_canvas()
            self.update_condition()
            self.logs.update_log(self.condition)
            print(self.condition)

    def btn_undo_log(self):
        condition = self.logs.undo_log()
        if len(condition) > 0:
            self.condition[0] = condition[0].copy()
            self.condition[1] = condition[1].copy()
            self.condition[2] = condition[2].copy()
            self.condition[3] = condition[3].copy()

            self.task_points.dots_A = self.condition[0]
            self.task_points.dot_D = self.condition[1]
            self.Parallels = self.condition[2]
            self.canvas_parallels = self.condition[3]

            self.refresh_table()
            self.refresh_canvas()
            self.refresh_canvas_parallels()
        else:
            error = QMessageBox()
            error.setWindowTitle("Ошибка!")
            error.setText("Нельзя отменить прошлое действие!")
            error.setDefaultButton(QMessageBox.Ok)
            error.setIcon(QMessageBox.Warning)
            error.exec_()
        print(self.condition)

    def cleanse(self):
        self.task_points.clear_all_points()
        
        
        self.refresh_canvas_parallels()
        self.refresh_table()
        self.refresh_canvas()
        self.update_condition()
        self.logs.update_log(self.condition)
        print(self.condition)

    def refresh_canvas_parallels(self):
        if (len(self.Parallels) > 0):
            if self.task_points.is_dot_D():
                canvas_parallels = list()
                Parallels = find_all_parallel(self.task_points.dots_A, *self.task_points.dot_D)
                for i in range(len(Parallels)):
                    coords = Parallels[i]
                    coords.append(coords[0])
                    xs, ys = zip(*coords)
                    canvas_parallels.append([xs, ys])
                

                self.Parallels =  [x for x in self.Parallels if x in Parallels]
                self.canvas_parallels = [x for x in self.canvas_parallels if x in canvas_parallels]

            else:
                self.Parallels.clear()
                self.canvas_parallels.clear()
            
    def refresh_table(self):
        self.table_dots_A.setRowCount(0)
        self.table_dot_D.setRowCount(0)
        for i in range(self.task_points.count_dots_A()):
            self.table_dots_A.setRowCount(self.task_points.count_dots_A())
            self.table_dots_A.setItem(i, 0, QTableWidgetItem(str(self.task_points.dots_A[i][0])))
            self.table_dots_A.setItem(i, 1, QTableWidgetItem(str(self.task_points.dots_A[i][1])))
        if self.task_points.is_dot_D():
            self.table_dot_D.setRowCount(1)
            self.table_dot_D.setItem(0, 0, QTableWidgetItem(str(self.task_points.dot_D[0][0])))
            self.table_dot_D.setItem(0, 1, QTableWidgetItem(str(self.task_points.dot_D[0][1])))
        
    def refresh_canvas(self):
        self.matplotlib_widget.axis.clear()
        self.canvas_points.clear()
        self.canvas_point_D = None
        self.selected_point = None
        self.is_selected = False
        
        for dot in self.task_points.dots_A:
            self.draw_point([dot[0], dot[1]], 'r')

        if self.task_points.is_dot_D():
            self.draw_point(self.task_points.dot_D[0], 'b')
        
        for i in range(len(self.canvas_parallels)):
            self.matplotlib_widget.axis.plot(*self.canvas_parallels[i])

        self.canvas_default()
        self.matplotlib_widget.axis.figure.canvas.draw()

    def canvas_default(self):
        self.matplotlib_widget.axis.set_aspect("auto", 'box')
        self.matplotlib_widget.axis.set_xlim(-100, 100)
        self.matplotlib_widget.axis.set_ylim(-100, 100)
        self.matplotlib_widget.axis.autoscale(True)
        

    def init_canvas(self):
        self.matplotlib_widget = MatplotlibWidget()
        self.verticalLayout_canvas.addWidget(self.matplotlib_widget)
        self.canvas_default()

        self.matplotlib_widget.axis.figure.canvas.mpl_connect('button_press_event', self.plot_click)
        self.matplotlib_widget.axis.figure.canvas.mpl_connect('pick_event', self.plot_pick)        

    def plot_click(self, event):
        if not self.matplotlib_widget.toolbar.mode and event.button == 1:
            
            x = event.xdata
            y = event.ydata
            print("Clicked on: ", x, y)
            if x is None or y is None:
                return
            
            x = round(x, 6)
            y = round(y, 6)            
            if self.d_dot_switch.isChecked():
                self.d_dot_switch.setChecked(False)
                if not self.task_points.is_dot_D():
                    self.task_points.change_dot_D([x, y])
                    
                else:
                    box = QtWidgets.QMessageBox()
                    box.setIcon(QMessageBox.Question)
                    box.setWindowTitle('Изменение точки D')
                    box.setText('Вы уверены, что хотите изменить точку D?')
                    box.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
                    buttonY = box.button(QMessageBox.Yes)
                    buttonY.setText('Да')
                    buttonN = box.button(QMessageBox.No)
                    buttonN.setText('Нет')
                    box.exec_()

                    if box.clickedButton() == buttonY:
                        self.task_points.change_dot_D([x, y])

            else:
                if not [x, y] in self.task_points.dots_A:
                    self.task_points.add_dot_A([x, y])
                    
            self.refresh_table()
            self.refresh_canvas()
            self.update_condition()
            self.logs.update_log(self.condition)
            print(self.condition)
            

    def draw_point(self, Coords, color):
        if not (Coords[0] is None or Coords[1] is None):
            point = self.matplotlib_widget.axis.plot(Coords[0], Coords[1], color+'o', picker=10)
            if color == 'r':
                self.canvas_points.append(point)
            elif color == 'b':
                self.canvas_point_D = point
            self.matplotlib_widget.figure.canvas.draw()
            


    def plot_pick(self, event):
        if not self.matplotlib_widget.toolbar.mode and event.mouseevent.button == 3:
            if self.is_selected == 'A':
                self.selected_point.set_color('r')
            elif self.is_selected == 'D':
                self.selected_point.set_color('b')
            
            line = event.artist
            self.selected_point = line
            line.set_color('g')

            self.x = line.get_xdata()[0]
            self.y = line.get_ydata()[0]
            
            if self.task_points.is_dot_D() and [self.x, self.y] == self.task_points.dot_D[0]:
                self.table_dot_D.setCurrentCell(0, 0)
                self.is_selected = 'D'
            else:
                self.table_dots_A.setCurrentCell(self.task_points.dots_A.index([self.x, self.y]), 0)
                self.is_selected = 'A'

            
            self.update_condition()
            self.logs.update_log(self.condition)
            print(self.condition)  
            self.matplotlib_widget.axis.figure.canvas.draw_idle()

    def table_A_selected(self):
        if self.is_selected == 'A':
            self.selected_point.set_color('r')
        elif self.is_selected == 'D':
            self.selected_point.set_color('b')
        
        self.is_selected = 'A'
        self.selected_point = self.canvas_points[self.table_dots_A.currentRow()][0]
        print(self.selected_point)
        self.selected_point.set_color('g')
        self.matplotlib_widget.axis.figure.canvas.draw_idle()
        self.update_condition()
        self.logs.update_log(self.condition)
        print(self.condition)

    def table_D_selected(self):
        if self.is_selected == 'A':
            self.selected_point.set_color('r')
        elif self.is_selected == 'D':
            self.selected_point.set_color('b')
        
        self.is_selected = 'D'
        self.selected_point = self.canvas_point_D[0]
        print(self.selected_point)
        self.selected_point.set_color('g')
        self.matplotlib_widget.axis.figure.canvas.draw_idle()
        self.update_condition()
        self.logs.update_log(self.condition)
        print(self.condition)


    def draw_all_parallels(self):
        if self.task_points.is_dot_D():
            self.Parallels = find_all_parallel(self.task_points.dots_A, *self.task_points.dot_D)
            for i in range(len(self.Parallels)):
                coords = self.Parallels[i]
                coords.append(coords[0])
                xs, ys = zip(*coords)
                if [xs, ys] not in self.canvas_parallels:
                    self.canvas_parallels.append([xs, ys])
                self.matplotlib_widget.axis.plot(xs, ys)
            self.update_condition()
            self.logs.update_log(self.condition)
            print(self.condition)
            self.matplotlib_widget.figure.canvas.draw()
        else:
            self.show_warning_no_D()

    def draw_solution(self):
        if self.task_points.is_dot_D():
            self.Parallels = find_all_parallel(self.task_points.dots_A, *self.task_points.dot_D)
            self.canvas_parallels = list()

            max_intersection_area, parallel1, parallel2 = task_solution(self.Parallels)
            if max_intersection_area != -1:

                coords = parallel1
                coords.append(coords[0])
                xs, ys = zip(*coords)
                if [xs, ys] not in self.canvas_parallels:
                    self.canvas_parallels.append([xs, ys])
                self.matplotlib_widget.axis.plot(xs, ys)

                coords = parallel2
                coords.append(coords[0])
                xs, ys = zip(*coords)
                if [xs, ys] not in self.canvas_parallels:
                    self.canvas_parallels.append([xs, ys])
                self.matplotlib_widget.axis.plot(xs, ys)


                self.refresh_canvas()
                self.update_condition()
                self.logs.update_log(self.condition)
                print(self.condition)

                ans = QMessageBox()
                ans.setWindowTitle("Задача успешно решена!")
                ans.setText(f"Наибольша площадь пересечения равна: {max_intersection_area}\nПервый параллелограмм:\n{parallel1[:-1]}\nВторой параллелограмм:\n{parallel2[:-1]}")
                ans.setDefaultButton(QMessageBox.Ok)
                ans.setIcon(QMessageBox.Information)
                ans.exec_()
        else:
            self.show_warning_no_D()

    def show_warning_no_D(self):
        error = QMessageBox()
        error.setWindowTitle("Ошибка!")
        error.setText("Точка D не задана!")
        error.setDefaultButton(QMessageBox.Ok)
        error.setIcon(QMessageBox.Warning)
        error.exec_()

    def update_condition(self):
        self.condition = [self.task_points.dots_A.copy(), self.task_points.dot_D.copy(), self.Parallels.copy(), self.canvas_parallels.copy()]


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.setupDefault()
    MainWindow.show()
    sys.exit(app.exec_())