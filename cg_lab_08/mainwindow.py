# This Python file uses the following encoding: utf-8
import sys
import time
import copy
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
        self.ui.pushButton_box_add.clicked.connect(self.cutter_add_button)
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
            self.task_lines = self.action_log[(len(self.action_log) - 1)][0].copy()
            self.task_cutter = self.action_log[(len(self.action_log) - 1)][1].copy()

            self.canvas_clean()
            self.ui.tableWidget_lines.setRowCount(0)
            for line in self.task_lines:
                self.line_add(line[0], line[1])
            if len(self.task_cutter) != 0:
                self.cutter_add(self.task_cutter[0], self.task_cutter[1])

            self.canvas_update()
            self.ui.graphicsView.show()


    # Функции кнопок

    def clean_button(self):
        self.canvas_clean()
        self.ui.graphicsView.resetTransform()
        self.canvas_scrollbar_reset()
        self.ui.tableWidget_lines.setRowCount(0)
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
            self.cutter_point_begin = (position.x() - self.canvas_center[0], -position.y() + self.canvas_center[1])
        self.canvas_update()


    def MB_release(self, event):
        if event.button() == Qt.LeftButton:
            position = self.ui.graphicsView.mapToScene(event.pos())
            self.line_point_end = (position.x() - self.canvas_center[0], -position.y() + self.canvas_center[1])
            self.line_add(self.line_point_begin, self.line_point_end)
            self.canvas_update()
            self.log_update()
        elif event.button() == Qt.RightButton:
            position = self.ui.graphicsView.mapToScene(event.pos())
            self.cutter_point_end = (position.x() - self.canvas_center[0], -position.y() + self.canvas_center[1])
            self.cutter_add(self.cutter_point_begin, self.cutter_point_end)
            self.canvas_redraw()
            self.log_update()


    def line_add_button(self):
        point_1 = (self.ui.doubleSpinBox_line_x_b.value(), self.ui.doubleSpinBox_line_y_b.value())
        point_2 = (self.ui.doubleSpinBox_line_x_e.value(), self.ui.doubleSpinBox_line_y_e.value())

        self.task_lines.append((point_1, point_2))
        self.line_add(point_1, point_2)
        self.canvas_update()
        self.log_update()

    def cutter_add_button(self):
        point_1 = (self.ui.doubleSpinBox_box_x_b.value(), self.ui.doubleSpinBox_box_y_b.value())
        point_2 = (self.ui.doubleSpinBox_box_x_e.value(), self.ui.doubleSpinBox_box_y_e.value())
        self.cutter_add(point_1, point_2)
        self.canvas_redraw()
        self.log_update()

    # Функции отрисовки

    def line_add(self, point_1, point_2):
        self.line_draw(point_1, point_2)
        rowPosition = self.ui.tableWidget_lines.rowCount()
        self.ui.tableWidget_lines.insertRow(rowPosition)
        self.ui.tableWidget_lines.setItem(rowPosition, 0, QTableWidgetItem(str((round(point_1[0], 2), round(point_1[1], 2)))))
        self.ui.tableWidget_lines.setItem(rowPosition, 1, QTableWidgetItem(str((round(point_2[0], 2), round(point_2[1], 2)))))
        if (point_1, point_2) not in self.task_lines:
            self.task_lines.append((point_1, point_2))


    def cutter_add(self, point_1, point_2):
        rect = [point_1, (point_2[0], point_1[1]), point_2, (point_1[0], point_2[1])]
        for i in range(4):
            if rect[i][0] < point_1[0] or (rect[i][0] == point_1[0] and rect[i][1] > point_1[1]):
                point_1 = rect[i]

            if rect[i][0] > point_2[0] or (rect[i][0] == point_2[0] and rect[i][1] < point_2[1]):
                point_2 = rect[i]

        self.rect_draw(point_1, point_2)
        self.ui.doubleSpinBox_box_x_b.setValue(point_1[0])
        self.ui.doubleSpinBox_box_y_b.setValue(point_1[1])
        self.ui.doubleSpinBox_box_x_e.setValue(point_2[0])
        self.ui.doubleSpinBox_box_y_e.setValue(point_2[1])
        self.task_cutter = [point_1, point_2]


    def canvas_redraw(self):
        self.canvas_clean()
        for line in self.task_lines:
            self.line_draw(line[0], line[1])
        if len(self.task_cutter) != 0:
            self.cutter_add(self.task_cutter[0], self.task_cutter[1])
        self.canvas_update()

    def line_draw(self, point_b, point_e, color = "default"):
        if color == "default":
            pen = QPen(QColor(self.color_line[0], self.color_line[1], self.color_line[2], self.color_line[3]))
        else:
            pen = QPen(QColor(color[0], color[1], color[2], color[3]))

        self.scene.addLine(point_b[0] + self.canvas_center[0], -point_b[1] + self.canvas_center[1], point_e[0] + self.canvas_center[0], -point_e[1] + self.canvas_center[1], pen)

    def rect_draw(self, point_b, point_e):
        rect = [point_b, (point_e[0], point_b[1]), point_e, (point_b[0], point_e[1])]
        for i in range(4):
            self.line_draw(rect[i], rect[(i + 1) % 4], (170, 0, 0, 255))


    # Функции отсечения





