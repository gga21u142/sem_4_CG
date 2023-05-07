# This Python file uses the following encoding: utf-8
import sys
import time
import copy
import math
from PySide6.QtTest import QTest
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QGraphicsScene, QColormap, QColorDialog, QLabel, QTableWidgetItem, QGraphicsView, QGraphicsLineItem
from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt, QPointF
from PySide6.QtGui import QColor, QPixmap, QPainter, QBrush, QWheelEvent, QPen
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.action_log = list()
        self.log_size = 10

        self.task_lines = list()
        self.task_cutter = list()

        self.canvas_init()
        self.color_bg = (255, 255, 255, 255)
        self.color_line = (0, 0, 0, 255)
        self.color_cutted =  (0, 170, 0, 255)
        self.color_cutter = (170, 0, 0, 255)
        self.ui.graphicsView.wheelEvent = self.wheelEvent



        #Обработка нажатия кнопок и ивентов
        self.ui.about_author.triggered.connect(self.info_author)
        self.ui.about_programm.triggered.connect(self.info_task)

        self.ui.graphicsView.mousePressEvent = self.MB_click
        self.ui.graphicsView.mouseReleaseEvent = self.MB_release

        self.ui.pushButton_clear.clicked.connect(self.clean_button)
        self.ui.pushButton_undo.clicked.connect(self.log_undo)
        self.ui.pushButton_color_bg.clicked.connect(self.color_bg_change)
        self.ui.pushButton_color_line.clicked.connect(self.color_line_change)
        self.ui.pushButton_color_cutted.clicked.connect(self.color_cutted_change)

        self.ui.pushButton_line_add.clicked.connect(self.line_add_button)
        self.ui.pushButton_box_add.clicked.connect(self.cutter_point_add_button)
        self.ui.pushButton_cutter_connect.clicked.connect(self.cutter_connect)
        self.ui.pushButton_cut.clicked.connect(self.cut_lines)

    # Служебные функции

    def info_author(self):
        info_author = QMessageBox()
        info_author.setWindowTitle("Об авторе")
        info_author.setText("\tСтудент ИУ7-44Б\t\n\tГареев Г. А.\t")
        info_author.setDefaultButton(QMessageBox.Ok)
        info_author.setIcon(QMessageBox.Information)

        info_author.exec_()


    def info_task(self):
        info_task = QMessageBox()
        info_task.setWindowTitle("Условие задачи")
        info_task.setText("Реализация алгоритм Кируса-Бека для отсечения отрезка произвольным выпуклым отсекателем.")
        info_task.setDefaultButton(QMessageBox.Ok)
        info_task.setIcon(QMessageBox.Information)

        info_task.exec_()


    def closeEvent(self, event):
        msg = QMessageBox(self)
        msg.setWindowTitle("Выход")
        msg.setIcon(QMessageBox.Question)
        msg.setText("Вы действительно хотите выйти ?")

        buttonAceptar  = msg.addButton("Да", QMessageBox.YesRole)
        buttonCancelar = msg.addButton("Нет", QMessageBox.RejectRole)
        msg.setDefaultButton(buttonAceptar)
        msg.exec_()

        if msg.clickedButton() == buttonAceptar:
            event.accept()
        elif msg.clickedButton() == buttonCancelar:
            event.ignore()


    def show_warning(self, text):
        error = QMessageBox()
        error.setWindowTitle("Ошибка!")
        error.setText(text)
        error.setDefaultButton(QMessageBox.Ok)
        error.setIcon(QMessageBox.Warning)
        error.exec_()


    def canvas_init(self):
        self.scale = 1

        self.scene = QGraphicsScene(self)
        self.ui.graphicsView.setScene(self.scene)

        self.pixmap = QPixmap(2500,2500)
        self.pixmap.fill(Qt.transparent)

        self.scene.addPixmap(self.pixmap)

        self.canvas_size = (2500, 2500)
        self.canvas_center = (self.canvas_size[0] // 2, self.canvas_size[1] // 2)
        self.view_size = (self.ui.graphicsView.width(), self.ui.graphicsView.height())
        self.log_update()


    def canvas_scrollbar_reset(self):
        self.view_size = (self.ui.graphicsView.width(), self.ui.graphicsView.height())
        self.ui.graphicsView.horizontalScrollBar().setValue(self.canvas_center[0] - (self.view_size[0] // 2))
        self.ui.graphicsView.verticalScrollBar().setValue(self.canvas_center[1] - (self.view_size[1] // 2))


    def showEvent(self, event):
        self.canvas_scrollbar_reset()


    def wheelEvent(self, event: QWheelEvent):
        if event.angleDelta().y() > 0:
            sub_scale = self.scale * 1.1
            if sub_scale >= 250:
                return
            else:
                self.scale = sub_scale
                self.ui.graphicsView.scale(1.1, 1.1)
        else:
            sub_scale = self.scale * 0.9
            if sub_scale <= 0.3:
                return
            else:
                self.scale = sub_scale
                self.ui.graphicsView.scale(0.9, 0.9)


    def log_update(self):
        lines_copy = self.task_lines.copy()
        cutter_copy = self.task_cutter.copy()
        self.action_log.append([lines_copy, cutter_copy])
        if len(self.action_log) > self.log_size:
            self.action_log.pop(0)


    def log_undo(self):
        if len(self.action_log) <= 1:
            self.show_warning("Невозможно отменить последнее действие")
        else:
            self.action_log.pop()
            self.task_lines.clear()
            self.task_cutter.clear()
            task_lines = self.action_log[(len(self.action_log) - 1)][0].copy()
            task_cutter = self.action_log[(len(self.action_log) - 1)][1].copy()

            self.canvas_clean()
            self.ui.tableWidget_lines.setRowCount(0)
            self.ui.tableWidget_cutter.setRowCount(0)
            for line in task_lines:
                self.line_add(line[0], line[1])
            for point in task_cutter:
                self.cutter_point_add(point)

            self.canvas_update()
            self.ui.graphicsView.show()


    # Функции кнопок

    def clean_button(self):
        self.canvas_clean()
        self.ui.graphicsView.resetTransform()
        self.canvas_scrollbar_reset()
        self.ui.tableWidget_lines.setRowCount(0)
        self.ui.tableWidget_cutter.setRowCount(0)
        self.task_lines.clear()
        self.task_cutter.clear()
        self.log_update()

    def canvas_clean(self):
        self.scale = 1

        self.canvas_size = (2500, 2500)
        self.view_size = (self.ui.graphicsView.width(), self.ui.graphicsView.height())
        self.canvas_center = (self.canvas_size[0] // 2, self.canvas_size[1] // 2)

        self.scene.clear()

        self.scene.addPixmap(self.pixmap)
        self.color_bg = (255, 255, 255, 255)
        self.ui.pushButton_color_bg.setStyleSheet('background-color: rgba(255, 255, 255, 255)')
        brush = QBrush(QColor(self.color_bg[0], self.color_bg[1], self.color_bg[2], self.color_bg[3]))
        self.ui.graphicsView.setBackgroundBrush(brush)

    def canvas_update(self):
        self.scene.update()

    def color_bg_change(self):
        color = QColorDialog.getColor()

        if color.isValid():
            self.color_bg = color.getRgb()
            print("BG color changed on rgba" + str(self.color_bg))

            color_str = 'background-color: rgba' + str(self.color_bg)
            self.ui.pushButton_color_bg.setStyleSheet(color_str)

            brush = QBrush(QColor(self.color_bg[0], self.color_bg[1], self.color_bg[2], self.color_bg[3]))
            self.ui.graphicsView.setBackgroundBrush(brush)


    def color_line_change(self):
        color = QColorDialog.getColor()

        if color.isValid():
            self.color_line = color.getRgb()
            print("LINE color changed on rgba" + str(self.color_line))

            color_str = 'background-color: rgba' + str(self.color_line)
            self.ui.pushButton_color_line.setStyleSheet(color_str)

    def color_cutted_change(self):
        color = QColorDialog.getColor()

        if color.isValid():
            self.color_cutted = color.getRgb()
            print("CUTTED color changed on rgba" + str(self.color_cutted))

            color_str = 'background-color: rgba' + str(self.color_cutted)
            self.ui.pushButton_color_cutted.setStyleSheet(color_str)


    def MB_click(self, event):
        if event.button() == Qt.LeftButton:
            position = self.ui.graphicsView.mapToScene(event.pos())
            self.line_point_begin = (position.x() - self.canvas_center[0], -position.y() + self.canvas_center[1])
        elif event.button() == Qt.RightButton:
            position = self.ui.graphicsView.mapToScene(event.pos())
            cutter_point = (position.x() - self.canvas_center[0], -position.y() + self.canvas_center[1])
            if self.cutter_point_add(cutter_point) == 0:
                self.log_update()



    def MB_release(self, event):
        if event.button() == Qt.LeftButton:
            position = self.ui.graphicsView.mapToScene(event.pos())
            self.line_point_end = (position.x() - self.canvas_center[0], -position.y() + self.canvas_center[1])
            self.line_add(self.line_point_begin, self.line_point_end)
            self.canvas_update()
            self.log_update()


    def line_add_button(self):
        point_1 = (self.ui.doubleSpinBox_line_x_b.value(), self.ui.doubleSpinBox_line_y_b.value())
        point_2 = (self.ui.doubleSpinBox_line_x_e.value(), self.ui.doubleSpinBox_line_y_e.value())

        self.task_lines.append((point_1, point_2))
        self.line_add(point_1, point_2)
        self.canvas_update()
        self.log_update()

    def cutter_point_add_button(self):
        point_1 = (self.ui.doubleSpinBox_box_x_b.value(), self.ui.doubleSpinBox_box_y_b.value())
        if self.cutter_point_add(point_1) == 0:
            self.log_update()

    def cutter_connect(self):
        if len(self.task_cutter) < 3:
            self.show_warning("Задано менее трех точек, невозможно замкнуть отсекатель.")
            return

        if self.task_cutter[0] == self.task_cutter[-1]:
            self.show_warning("Текущий отсекатель уже замкнут.")
            return

        self.line_draw(self.task_cutter[0], self.task_cutter[-1], self.color_cutter)
        self.task_cutter.append(self.task_cutter[0])

    # Функции отрисовки

    def line_add(self, point_1, point_2):
        self.line_draw(point_1, point_2)
        rowPosition = self.ui.tableWidget_lines.rowCount()
        self.ui.tableWidget_lines.insertRow(rowPosition)
        self.ui.tableWidget_lines.setItem(rowPosition, 0, QTableWidgetItem(str((round(point_1[0], 2), round(point_1[1], 2)))))
        self.ui.tableWidget_lines.setItem(rowPosition, 1, QTableWidgetItem(str((round(point_2[0], 2), round(point_2[1], 2)))))
        if (point_1, point_2) not in self.task_lines:
            self.task_lines.append((point_1, point_2))


    def cutter_point_add(self, point_1):
        if len(self.task_cutter) > 1 and self.task_cutter[0] == self.task_cutter[-1]:
            self.task_cutter.clear()
            self.ui.tableWidget_cutter.setRowCount(0)
            self.canvas_redraw()
            self.canvas_update()

        if len(self.task_cutter) == 0 or point_1 != self.task_cutter[-1]:
            if len(self.task_cutter) > 0:
                self.line_draw(point_1, self.task_cutter[-1], self.color_cutter)
            self.task_cutter.append(point_1)
            rowPosition = self.ui.tableWidget_cutter.rowCount()
            self.ui.tableWidget_cutter.insertRow(rowPosition)
            self.ui.tableWidget_cutter.setItem(rowPosition, 0, QTableWidgetItem(str((round(point_1[0], 2)))))
            self.ui.tableWidget_cutter.setItem(rowPosition, 1, QTableWidgetItem(str((round(point_1[1], 2)))))
            self.canvas_update()
            return 0

        return 1


    def canvas_redraw(self):
        self.canvas_clean()
        for line in self.task_lines:
            self.line_draw(line[0], line[1])



    def line_draw(self, point_b, point_e, color = "default"):
        if color == "default":
            pen = QPen(QColor(self.color_line[0], self.color_line[1], self.color_line[2], self.color_line[3]))
        else:
            pen = QPen(QColor(color[0], color[1], color[2], color[3]))

        self.scene.addLine(point_b[0] + self.canvas_center[0], -point_b[1] + self.canvas_center[1], point_e[0] + self.canvas_center[0], -point_e[1] + self.canvas_center[1], pen)

    def is_cutter_convex(self):
        n = len(self.task_cutter[:-1])
        if n < 3:
            return False

        for i in range(n - 1):
            point_1 = self.task_cutter[i]
            point_2 = self.task_cutter[i + 1]
            side = None
            for j in range(n):
                if j != i and j != i + 1:
                    point = self.task_cutter[j]
                    det = (point_2[0] - point_1[0]) * (point[1] - point_1[1]) - (point_2[1] - point_1[1]) * (point[0] - point_1[0])

                    cur_side = -1 if det >= 0 else 1

                    if side == None or side == 0:
                        side = cur_side
                    elif side != cur_side:
                        return False
        return True

    # Функции отсечения

    def cut_lines(self):
        if len(self.task_cutter) == 0 or self.task_cutter[0] != self.task_cutter[-1]:
            self.show_warning("Отсекатель не задан или не замкнут.")
            return
        if not self.is_cutter_convex():
            self.show_warning("Отсекатель имеет форму невыпуклого многоугольника. Задайте корректный отсекатель.")
            return
        self.task_cutter.pop()
        for line in self.task_lines:
            point_1, point_2 = self.cyrus_beck(line)
            if point_1 != None:
                self.line_draw(point_1, point_2, self.color_cutted)
        self.task_cutter.append(self.task_cutter[0])
        self.canvas_update()


    def calc_vector_scalar(self, vect_1, vect_2):
        return vect_1[0] * vect_2[0] + vect_1[1] * vect_2[1]


    def find_internal_normal(self, dot1, dot2, pos):
        direct_vect = [dot2[0] - dot1[0], dot2[1] - dot1[1]]
        check_vect = [pos[0] - dot2[0], pos[1] - dot2[1]]

        if direct_vect[1] != 0:
            tan = - direct_vect[0] / direct_vect[1]
            normal = [1, tan]
        else:
            normal = [0, 1]

        if (self.calc_vector_scalar(check_vect, normal) < 0):
            return [-normal[0], -normal[1]]

        return normal


    def cyrus_beck(self, line):
        direct_vect = [line[1][0] - line[0][0], line[1][1] - line[0][1]]

        t_bot = 0
        t_top = 1

        leng = len(self.task_cutter)
        for i in range(leng):

            normal = self.find_internal_normal(self.task_cutter[i], self.task_cutter[(i + 1) % leng], self.task_cutter[(i + 2) % leng])
            line_p_vect = [line[0][0] - self.task_cutter[i][0], line[0][1] - self.task_cutter[i][1]]

            denominator = self.calc_vector_scalar(direct_vect, normal)
            numerator = self.calc_vector_scalar(line_p_vect, normal)

            if denominator == 0:
                if numerator <= 0:
                    return None, None
                else:
                    continue

            t = - numerator / denominator

            if denominator > 0:
                if t <= 1:
                    t_bot = max(t_bot, t)
                else:
                    return None, None
            elif denominator < 0:
                if t >= 0:
                    t_top = min(t_top, t)
                else:
                    return None, None

            if t_bot > t_top:
                break

        if t_bot <= t_top:
            point_1 = [line[0][0] + direct_vect[0] * t_bot, line[0][1] + direct_vect[1] * t_bot]
            point_2 = [line[0][0] + direct_vect[0] * t_top, line[0][1] + direct_vect[1] * t_top]

            return point_1, point_2

        return None, None
