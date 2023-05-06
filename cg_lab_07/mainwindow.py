# This Python file uses the following encoding: utf-8
import sys
import time
import copy
from PySide6.QtTest import QTest
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QGraphicsScene, QColormap, QColorDialog, QLabel
from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPixmap, QPainter, QBrush, QWheelEvent
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

        self.canvas_init()
        self.color_bg = (255, 255, 255, 255)
        self.color_rib = (170, 0, 0, 255)
        self.color_fill =  (0, 170, 0, 255)
        self.ui.graphicsView.wheelEvent = self.wheelEvent


        #Обработка нажатия кнопок и ивентов
        self.ui.about_author.triggered.connect(self.info_author)
        self.ui.about_programm.triggered.connect(self.info_task)

        self.ui.pushButton_clear.clicked.connect(self.clean_button)
        self.ui.pushButton_undo.clicked.connect(self.log_undo)
        self.ui.graphicsView.mousePressEvent = self.LMB_event
        self.ui.pushButton_color_bg.clicked.connect(self.color_bg_change)
        self.ui.pushButton_color_rib.clicked.connect(self.color_rib_change)
        self.ui.pushButton_color_fill.clicked.connect(self.color_fill_change)

#        self.ui.pushButton_dot_add.clicked.connect(self.point_add_button)
#        self.ui.pushButton_fill.clicked.connect(self.fill_figure_point)

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
        info_task.setText("Реализация и исследование алгоритма со списком ребер и флагом для растрового заполнения области. Реализвать ввод точек нажатием кнопки мыши, через поле. Программа должна предусматривать отрисовку с задержкой для наглядной демонстрации алгоритма. Также после выполнения заливки необходимо указать затраченное кол-во времени.\nДополнительные функции:\n1) Ведение жернала действий для их отмены\n2) Возможность двигать\масштабировать канвас\n3) Изменение цвета заливки, ребер и фона")
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
        self.table_add_point(('-----', '-----'))

        self.scene = QGraphicsScene(self)
        self.ui.graphicsView.setScene(self.scene)

        self.pixmap = QPixmap(2500,2500)
        self.pixmap.fill(Qt.transparent)

        self.scene.addPixmap(self.pixmap)

        self.canvas_size = (2500, 2500)
        self.view_size = (self.ui.graphicsView.width(), self.ui.graphicsView.height())
        self.canvas_center = (self.canvas_size[0] // 2, self.canvas_size[1] // 2)


    def canvas_scrollbar_reset(self):
        self.ui.graphicsView.horizontalScrollBar().setValue(self.canvas_center[0] - (self.view_size[0] // 2))
        self.ui.graphicsView.verticalScrollBar().setValue(self.canvas_center[1] - (self.view_size[1] // 2))


    def showEvent(self, event):
        self.canvas_clean()


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
        pixmap_copy = self.pixmap.copy()
        self.action_log.append(pixmap_copy.copy())
        if len(self.action_log) > self.log_size:
            self.action_log.pop(0)


    def log_undo(self):
        if len(self.action_log) <= 1:
            self.show_warning("Невозможно отменить последнее действие")
        else:
            self.action_log.pop()
            self.pixmap = self.action_log[(len(self.action_log) - 1)][0]
            self.points = self.action_log[(len(self.action_log) - 1)][1]

            self.ui.tableWidget_ribs.setRowCount(2)
            self.ui.tableWidget_ribs.setCellWidget(0, 0, QLabel(str(self.points.fill_point[0])))
            self.ui.tableWidget_ribs.setCellWidget(0, 1, QLabel(str(self.points.fill_point[1])))

            self.scene.clear()
            self.scene.addPixmap(self.pixmap)
            self.ui.graphicsView.show()

    def table_add_point(self, point):
        rowPosition = self.ui.tableWidget_ribs.rowCount()
        self.ui.tableWidget_ribs.insertRow(rowPosition)
        self.ui.tableWidget_ribs.setCellWidget(rowPosition, 0, QLabel(str(point[0])))
        self.ui.tableWidget_ribs.setCellWidget(rowPosition, 1, QLabel(str(point[1])))

    def figure_inside_warning(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("Закраска")
        msg.setIcon(QMessageBox.Question)
        msg.setText("Затравочная точка находится вне фигуры.\nЕсли у вас фигура с пересекающимися ребрами, то сообщение может быть ошибочным.\nПродолжить?")

        buttonAceptar  = msg.addButton("Да", QMessageBox.YesRole)
        buttonCancelar = msg.addButton("Нет", QMessageBox.RejectRole)
        msg.setDefaultButton(buttonAceptar)
        msg.exec_()

        if msg.clickedButton() == buttonAceptar:
            return True
        elif msg.clickedButton() == buttonCancelar:
            return False

    # Функции кнопок

    def clean_button(self):
        self.canvas_clean()
        self.points.clear()
        self.ui.tableWidget_ribs.setRowCount(0)

    def canvas_clean(self):
        self.scale = 1

        self.canvas_size = (2500, 2500)
        self.view_size = (self.ui.graphicsView.width(), self.ui.graphicsView.height())
        self.canvas_center = (self.canvas_size[0] // 2, self.canvas_size[1] // 2)

        self.scene.clear()

        self.pixmap = QPixmap(2500, 2500)
        self.pixmap.fill(Qt.transparent)

        self.scene.addPixmap(self.pixmap)
        self.color_bg = (255, 255, 255, 255)
        self.ui.pushButton_color_bg.setStyleSheet('background-color: rgba(255, 255, 255, 255)')
        brush = QBrush(QColor(self.color_bg[0], self.color_bg[1], self.color_bg[2], self.color_bg[3]))
        self.ui.graphicsView.setBackgroundBrush(brush)

        self.ui.graphicsView.resetTransform()
        self.canvas_scrollbar_reset()
        self.log_update()

    def update_scene(self):
        self.scene.clear()
        self.scene.addPixmap(self.pixmap)
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


    def color_rib_change(self):
        color = QColorDialog.getColor()

        if color.isValid():
            self.color_rib = color.getRgb()
            print("RIB color changed on rgba" + str(self.color_rib))

            color_str = 'background-color: rgba' + str(self.color_rib)
            self.ui.pushButton_color_rib.setStyleSheet(color_str)

    def color_fill_change(self):
        color = QColorDialog.getColor()

        if color.isValid():
            self.color_fill = color.getRgb()
            print("FILL color changed on rgba" + str(self.color_fill))

            color_str = 'background-color: rgba' + str(self.color_fill)
            self.ui.pushButton_color_fill.setStyleSheet(color_str)

    # Функции отрисовки

    def draw_point(self, point, color, log = True):
        painter = QPainter(self.pixmap)
        painter.setPen(QColor(color[0], color[1], color[2], color[3]))
        painter.drawPoint(point[0] + self.canvas_center[0], -point[1] + self.canvas_center[1])
        painter.end()
        if log:
            self.log_update()

    def draw_line(self, point_b, point_e, log = True):
        painter = QPainter(self.pixmap)
        painter.setPen(QColor(QColor(self.color_rib[0], self.color_rib[1], self.color_rib[2], self.color_rib[3])))
        painter.drawLine(point_b[0] + self.canvas_center[0], -point_b[1] + self.canvas_center[1], point_e[0] + self.canvas_center[0], -point_e[1] + self.canvas_center[1])
        painter.end()
        if log:
            self.log_update()


        x, y = point

        # Проходимся по каждой стороне фигуры
        for figure in self.points.figures:
            intersections = 0

            for i in range(len(figure)):
                # Получаем координаты текущей и следующей точек стороны
                current_point = figure[i]
                next_point = figure[(i + 1) % len(figure)]

                # Проверяем, находится ли точка выше, ниже или на одном уровне со стороной
                if (current_point[1] <= y and next_point[1] > y) or \
                   (current_point[1] > y and next_point[1] <= y):

                    # Вычисляем координату x пересечения луча и стороны
                    intersect = (next_point[0] - current_point[0]) * (y - current_point[1]) / \
                                (next_point[1] - current_point[1]) + current_point[0]

                    # Увеличиваем количество пересечений, если точка пересекает сторону
                    if intersect > x:
                        intersections += 1

            if intersections % 2 != 0:
                return True

        # Если количество пересечений нечетное, то точка внутри фигуры
        return False


    def LMB_event(self, event):
        if event.button() == Qt.LeftButton:
            position = self.ui.graphicsView.mapToScene(event.pos())
            click_point = (round(position.x() - (self.canvas_center[0])), round(-(position.y() - (self.canvas_center[1]))))

            self.table_add_point(click_point)
            self.draw_line(self.points.points[-2], click_point)
            self.update_scene()

    def point_add_button(self):
        click_point = (self.ui.spinBox_add_x.value(), self.ui.spinBox_add_y.value())

        self.table_add_point(click_point)
        self.draw_line(self.points.points[-2], click_point)
        self.update_scene()

    # Функции заливки

    def pixel_color_get(self, point):
        return self.pixmap.toImage().pixelColor(point[0] + self.canvas_center[0], -point[1] + self.canvas_center[1]).getRgb()


