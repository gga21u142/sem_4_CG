# This Python file uses the following encoding: utf-8
import sys
import time
import matplotlib.pyplot as plt
from figure_points import *
from message_boxes import *
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QGraphicsScene, QColormap
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

        self.colors_line = {"Черный":(0, 0, 0, 255), "Белый":(255, 255, 255, 255), "Красный":(255, 0, 0, 255), "Зеленый":(0, 255, 0, 255), "Синий":(0, 0, 255, 255), "Желтый":(255, 255, 0, 255), "Розовый":(255, 0, 255, 255)}
        self.colors_bg = {"Черный":(0, 0, 0, 127), "Белый":(255, 255, 255, 255), "Красный":(255, 0, 0, 127), "Зеленый":(0, 255, 0, 127), "Синий":(0, 0, 255, 127), "Желтый":(255, 255, 0, 127), "Розовый":(255, 0, 255, 127)}
        self.action_log = list()
        self.log_size = 10

        self.canvas_init()
        self.ui.graphicsView.wheelEvent = self.wheelEvent

        #Обработка нажатия кнопок и ивентов
        self.ui.about_author.triggered.connect(self.info_author)
        self.ui.about_program.triggered.connect(self.info_task)
        self.ui.pushButton_measure_circle.clicked.connect(self.btn_measure_circle)
        self.ui.pushButton_measure_ellipse.clicked.connect(self.btn_measure_ellipse)
        self.ui.pushButton_clear.clicked.connect(self.canvas_clean)
        self.ui.pushButton_circle_draw.clicked.connect(self.circle_draw_hub)
        self.ui.pushButton_ellipse_draw.clicked.connect(self.ellipse_draw_hub)
        self.ui.pushButton_circle_spectre_draw.clicked.connect(self.circle_spectre_draw_hub)
        self.ui.pushButton_ellipse_spectre_draw.clicked.connect(self.ellipse_spectre_draw_hub)
        self.ui.pushButto_undo.clicked.connect(self.log_undo)

        self.ui.comboBox_color_bg.textActivated.connect(self.change_bg_color_word)
        self.ui.comboBox_color_figure.textActivated.connect(self.change_line_color)


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
        info_task.setText("Реализация построения окружностей, эллипсов и спектров различными алгоритмами: каноническим и параметрическим уравнениями, методом Брезенхема и средней точки, функцией стандартной библиотеки. Сравнение временных характеристик построения спектров для различных алгоритмов.")
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

    def show_info_measure(self, figure):
        msg = QMessageBox()
        msg.setWindowTitle("О процессе замера времени")
        msg.setText("При замере времени выполнения алгоритмов для окружности меняется ее радиус, для эллипсов линейно возрастают оба радиуса с соотношением 1/2.\nВыполнить замер?")
        buttonAceptar  = msg.addButton("Да", QMessageBox.YesRole)
        buttonCancelar = msg.addButton("Нет", QMessageBox.RejectRole)
        msg.setIcon(QMessageBox.Information)
        msg.setDefaultButton(buttonAceptar)
        msg.exec_()

        if msg.clickedButton() == buttonAceptar:
            print("Measure time for " + figure)
            if figure == "circle":
                self.measure_time_circle()
            else:
                self.measure_time_ellipse()

    def canvas_init(self):
        self.canvas_bg_color = (255, 255, 255, 255)
        self.canvas_line_color = (0, 0, 0, 255)
        self.scale = 1

        self.scene = QGraphicsScene(self)
        self.ui.graphicsView.setScene(self.scene)

        self.pixmap = QPixmap(10000,10000)
        self.pixmap.fill(Qt.transparent)

        self.scene.addPixmap(self.pixmap)

        self.canvas_size = (10000, 10000)
        self.view_size = (self.ui.graphicsView.width(), self.ui.graphicsView.height())
        self.canvas_center = (self.canvas_size[0] // 2, self.canvas_size[1] // 2)

        self.log_update()

    def canvas_scrollbar_reset(self):
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
        pixmap_copy = self.pixmap.copy()
        self.action_log.append([pixmap_copy.copy(), self.canvas_bg_color])
        if len(self.action_log) > self.log_size:
            self.state_stack.pop(0)
        print(self.action_log)
    def log_undo(self):
        if len(self.action_log) <= 1:
            show_warn_cant_undo()
        else:
            self.action_log.pop()
            i = (len(self.action_log) - 1)
            self.pixmap = self.action_log[i][0]
            self.change_bg_color_value(self.action_log[i][1])
            for memb in self.colors_bg.items():
                if memb[1] == self.action_log[i][1]:
                    index = self.ui.comboBox_color_bg.findText(memb[0])
                    if index != -1:
                        self.ui.comboBox_color_bg.setCurrentIndex(index)

            self.scene.clear()
            self.scene.addPixmap(self.pixmap)
            self.ui.graphicsView.show()
    # Функции кнопок

    def btn_measure_circle(self):
        self.show_info_measure("circle")

    def btn_measure_ellipse(self):
        self.show_info_measure("ellipse")

    def change_bg_color_word(self, text):
        print("Bg color changed on ")
        print(self.colors_bg[text])
        self.canvas_bg_color = self.colors_bg[text]

        color = self.canvas_bg_color
        brush = QBrush(QColor(color[0], color[1], color[2], color[3]))
        self.ui.graphicsView.setBackgroundBrush(brush)
        self.log_update()

    def change_bg_color_value(self, value):
        print("Bg color changed on ")
        print(value)
        self.canvas_bg_color = value

        color = self.canvas_bg_color
        brush = QBrush(QColor(color[0], color[1], color[2], color[3]))
        self.ui.graphicsView.setBackgroundBrush(brush)

    def change_line_color(self, text):
        print("Figure color changed on ")
        print(self.colors_line[text])
        self.canvas_line_color = (self.colors_line[text])
    def canvas_clean(self):
        self.canvas_bg_color = (255, 255, 255, 255)
        self.scale = 1

        self.canvas_size = (10000, 10000)
        self.view_size = (self.ui.graphicsView.width(), self.ui.graphicsView.height())
        self.canvas_center = (self.canvas_size[0] // 2, self.canvas_size[1] // 2)

        self.scene.clear()

        self.pixmap = QPixmap(10000, 10000)
        self.pixmap.fill(Qt.transparent)

        self.scene.addPixmap(self.pixmap)

        self.change_bg_color_word("Белый")
        self.ui.comboBox_color_bg.setCurrentIndex(0)

        self.ui.graphicsView.resetTransform()
        self.canvas_scrollbar_reset()
        self.log_update()

    def update_scene(self):
        self.scene.addPixmap(self.pixmap)
        self.ui.graphicsView.show()


    # Хабы отрисовки

    def circle_draw_hub(self):
        method = self.ui.comboBox_alrorithm.currentIndex()
        centre = [round(self.ui.doubleSpinBox_circle_centre_x.value()), round(self.ui.doubleSpinBox_circle_centre_y.value())]
        centre[0] += self.canvas_center[0]
        centre[1] += self.canvas_center[1]
        if centre[0] >= 10000 or centre[0] <= 0 or centre[1] >= 10000 or centre[1] <= 0:
            show_warn_centre()
            return
        radius = round(self.ui.doubleSpinBox_circle_radius.value())
        if radius == 0:
            show_warn_cir_radius()
            return

        points = list()
        if method == 0:
            print("Canon")
            points = draw_circle_canon(centre, radius)

        elif method == 1:
            print("Parametr")
            points = draw_circle_param(centre, radius)

        elif method == 2:
            print("Brezenhem")
            points = draw_circle_bresenham(centre, radius)

        elif method == 3:
            print("Mid dot")
            points = draw_circle_mid_point(centre, radius)

        elif method == 4:
            print("Bible")
            self.ellipse_bible_draw(centre, radius, radius)

        else:
            print("gg")
            return

        self.points_draw(points)
        self.update_scene()
        self.log_update()

    def circle_spectre_draw_hub(self):
        method = self.ui.comboBox_alrorithm.currentIndex()
        centre = [round(self.ui.doubleSpinBox_circle_centre_x.value()), round(self.ui.doubleSpinBox_circle_centre_y.value())]
        centre[0] += self.canvas_center[0]
        centre[1] += self.canvas_center[1]
        if centre[0] >= 10000 or centre[0] <= 0 or centre[1] >= 10000 or centre[1] <= 0:
            show_warn_centre()
            return

        rad_beg = 0
        rad_end = 0
        step = 0
        count = 0

        if self.ui.checkBox.isChecked():
            rad_beg = round((self.ui.doubleSpinBox_circle_start_radius.value()))
        if self.ui.checkBox_2.isChecked():
            rad_end = round(self.ui.doubleSpinBox_circle_end_radius.value())
        if self.ui.checkBox_3.isChecked():
            step = self.ui.spinBox_circle_step.value()
        if self.ui.checkBox_4.isChecked():
            count = self.ui.spinBox_circle_amount.value()

        logic = (rad_beg == 0) + (rad_end == 0) + (step == 0) + (count == 0)
        if logic != 1:
            show_warn_cir_spec_settings()
            return

        if rad_beg == 0:
            rad_beg = rad_end - step * count
        if rad_end == 0:
            rad_end = rad_beg + step * count
        if step == 0:
            step = (rad_end - rad_beg) // count
        if count == 0:
            count = (rad_end - rad_beg) // step

        if rad_beg <= 0 or rad_end <= 0 or step <= 0 or count <= 0:
            show_warn_cir_spec_wrong_set()
            return

        if method == 0:
            print("Canon")
            self.spectre_circle_canon_draw(centre, rad_beg, rad_end, step, count)

        elif method == 1:
            print("Parametr")
            self.spectre_circle_param_draw(centre, rad_beg, rad_end, step, count)

        elif method == 2:
            print("Brezenhem")
            self.spectre_circle_bresenham_draw(centre, rad_beg, rad_end, step, count)

        elif method == 3:
            print("Mid dot")
            self.spectre_circle_mid_point_draw(centre, rad_beg, rad_end, step, count)

        elif method == 4:
            print("Bible")
            self.spectre_circle_bible_draw(centre, rad_beg, rad_end, step, count)

        else:
            print("gg")
            return

        self.update_scene()
        self.log_update()

    def ellipse_draw_hub(self):
        method = self.ui.comboBox_alrorithm.currentIndex()
        centre = [round(self.ui.doubleSpinBox_ellipse_centre_x.value()), round(self.ui.doubleSpinBox_ellipse_centre_y.value())]
        centre[0] += self.canvas_center[0]
        centre[1] += self.canvas_center[1]
        if centre[0] >= 10000 or centre[0] <= 0 or centre[1] >= 10000 or centre[1] <= 0:
            show_warn_centre()
            return
        radius_x = round(self.ui.doubleSpinBox_ellipse_radius_x.value())
        radius_y = round(self.ui.doubleSpinBox_ellipse_radius_y.value())
        if radius_x == 0 or radius_y == 0:
            show_warn_ell_radius()
            return

        point = list()
        if method == 0:
            print("Canon")
            points = draw_ellipse_canon(centre, radius_x, radius_y)

        elif method == 1:
            print("Parametr")
            points = draw_ellipse_param(centre, radius_x, radius_y)

        elif method == 2:
            print("Brezenhem")
            points = draw_ellipse_bresenham(centre, radius_x, radius_y)

        elif method == 3:
            print("Mid dot")
            points = draw_ellipse_mid_point(centre, radius_x, radius_y)

        elif method == 4:
            print("Bible")
            self.ellipse_bible_draw(centre, radius_x, radius_y)

        else:
            print("gg")
            return

        self.points_draw(points)
        self.update_scene()
        self.log_update()

    def ellipse_spectre_draw_hub(self):
        method = self.ui.comboBox_alrorithm.currentIndex()
        centre = [round(self.ui.doubleSpinBox_ellipse_centre_x.value()), round(self.ui.doubleSpinBox_ellipse_centre_y.value())]
        centre[0] += self.canvas_center[0]
        centre[1] += self.canvas_center[1]

        if centre[0] >= 10000 or centre[0] <= 0 or centre[1] >= 10000 or centre[1] <= 0:
            show_warn_centre()
            return

        rad_beg_x = round(self.ui.doubleSpinBox_ellipse_start_rx.value())
        rad_beg_y = round(self.ui.doubleSpinBox_ellipse_start_ry.value())
        rad_step_x = 0
        rad_step_y = 0
        count = self.ui.spinBox_ellipse_amount.value()
        if count == 0 or rad_beg_x == 0 or rad_beg_y == 0:
            show_warn_ell_spec_settings()
            return

        if self.ui.radioButton_step_rx.isChecked():
            rad_step_x = round(self.ui.doubleSpinBox_ellipse_step_rx.value())
            if rad_step_x == 0:
                show_warn_ell_spec_step()
                return
        elif self.ui.radioButton_step_ry.isChecked():
            rad_step_y = round(self.ui.doubleSpinBox_ellipse_step_ry.value())
            if rad_step_y == 0:
                show_warn_ell_spec_step()
                return
        else:
            show_warn_ell_spec_step()
            return

        if method == 0:
            print("Canon")
            self.spectre_ellipse_canon_draw(centre, rad_beg_x, rad_beg_y, rad_step_x, rad_step_y, count)

        elif method == 1:
            print("Parametr")
            self.spectre_ellipse_param_draw(centre, rad_beg_x, rad_beg_y, rad_step_x, rad_step_y, count)

        elif method == 2:
            print("Brezenhem")
            self.spectre_ellipse_bresenham_draw(centre, rad_beg_x, rad_beg_y, rad_step_x, rad_step_y, count)

        elif method == 3:
            print("Mid dot")
            self.spectre_ellipse_mid_point_draw(centre, rad_beg_x, rad_beg_y, rad_step_x, rad_step_y, count)

        elif method == 4:
            print("Bible")
            self.spectre_ellipse_bible_draw(centre, rad_beg_x, rad_beg_y, rad_step_x, rad_step_y, count)

        else:
            print("gg")
            return

        self.update_scene()
        self.log_update()


    # Функции отрисовки

    def draw_point(self, point):
        painter = QPainter(self.pixmap)
        painter.setPen(QColor(QColor(self.canvas_line_color[0], self.canvas_line_color[1], self.canvas_line_color[2], self.canvas_line_color[3])))
        painter.drawPoint(point[0], point[1])
        painter.end()

    def points_draw(self, points):
        for point in points:
            self.draw_point(point)

    def ellipse_bible_draw(self, centre, radius_x, radius_y):
        painter = QPainter(self.pixmap)
        painter.setPen(QColor(self.canvas_line_color[0], self.canvas_line_color[1], self.canvas_line_color[2], self.canvas_line_color[3]))
        painter.drawEllipse(centre[0] - radius_x, centre[1] - radius_y, radius_x * 2, radius_y * 2)
        painter.end()
    # Спектр окружности

    def spectre_circle_bible_draw(self, centre, rad_beg, rad_end, step, count):
        rad_cur = rad_beg
        for i in range(count):
            self.ellipse_bible_draw(centre, rad_cur, rad_cur)
            rad_cur += step

    def spectre_circle_canon_draw(self, centre, rad_beg, rad_end, step, count):
        rad_cur = rad_beg
        for i in range(count):
            points = draw_circle_canon(centre, rad_cur)
            self.points_draw(points)
            rad_cur += step

    def spectre_circle_param_draw(self, centre, rad_beg, rad_end, step, count):
        rad_cur = rad_beg
        for i in range(count):
            points = draw_circle_param(centre, rad_cur)
            self.points_draw(points)
            rad_cur += step
    def spectre_circle_bresenham_draw(self, centre, rad_beg, rad_end, step, count):
        rad_cur = rad_beg
        for i in range(count):
            points = draw_circle_bresenham(centre, rad_cur)
            self.points_draw(points)
            rad_cur += step

    def spectre_circle_mid_point_draw(self, centre, rad_beg, rad_end, step, count):
        rad_cur = rad_beg
        for i in range(count):
            points = draw_circle_mid_point(centre, rad_cur)
            self.points_draw(points)
            rad_cur += step

    # Спектр эллипса

    def spectre_ellipse_bible_draw(self, centre, rad_beg_x, rad_beg_y, rad_step_x, rad_step_y, count):
        rad_cur_x = rad_beg_x
        rad_cur_y = rad_beg_y
        for i in range(count):
            self.ellipse_bible_draw(centre, rad_cur_x, rad_cur_y)
            rad_cur_x += rad_step_x
            rad_cur_y += rad_step_y

    def spectre_ellipse_canon_draw(self, centre, rad_beg_x, rad_beg_y, rad_step_x, rad_step_y, count):
        rad_cur_x = rad_beg_x
        rad_cur_y = rad_beg_y
        for i in range(count):
            points = draw_ellipse_canon(centre, rad_cur_x, rad_cur_y)
            self.points_draw(points)
            rad_cur_x += rad_step_x
            rad_cur_y += rad_step_y
    def spectre_ellipse_param_draw(self, centre, rad_beg_x, rad_beg_y, rad_step_x, rad_step_y, count):
        rad_cur_x = rad_beg_x
        rad_cur_y = rad_beg_y
        for i in range(count):
            points = draw_ellipse_param(centre, rad_cur_x, rad_cur_y)
            self.points_draw(points)
            rad_cur_x += rad_step_x
            rad_cur_y += rad_step_y
    def spectre_ellipse_bresenham_draw(self, centre, rad_beg_x, rad_beg_y, rad_step_x, rad_step_y, count):
        rad_cur_x = rad_beg_x
        rad_cur_y = rad_beg_y
        for i in range(count):
            points = draw_ellipse_bresenham(centre, rad_cur_x, rad_cur_y)
            self.points_draw(points)
            rad_cur_x += rad_step_x
            rad_cur_y += rad_step_y

    def spectre_ellipse_mid_point_draw(self, centre, rad_beg_x, rad_beg_y, rad_step_x, rad_step_y, count):
        rad_cur_x = rad_beg_x
        rad_cur_y = rad_beg_y
        for i in range(count):
            points = draw_ellipse_mid_point(centre, rad_cur_x, rad_cur_y)
            self.points_draw(points)
            rad_cur_x += rad_step_x
            rad_cur_y += rad_step_y


    # Замеры времени
    def measure_time_circle(self):
        centre = [0, 0]
        rad_beg = 100
        step = 100
        count = 100
        iterations = 5

        Times = [[0] * count for i in range(4)]

        for i in range(iterations):
            cur_rad = rad_beg
            for j in range(count):
                time_start = time.time_ns()
                draw_circle_canon(centre, cur_rad)
                time_end = time.time_ns()
                Times[0][j] += time_end - time_start

                time_start = time.time_ns()
                draw_circle_param(centre, cur_rad)
                time_end = time.time_ns()
                Times[1][j] += time_end - time_start

                time_start = time.time_ns()
                draw_circle_bresenham(centre, cur_rad)
                time_end = time.time_ns()
                Times[2][j] += time_end - time_start

                time_start = time.time_ns()
                draw_circle_mid_point(centre, cur_rad)
                time_end = time.time_ns()
                Times[3][j] += time_end - time_start

                cur_rad += step

            for timer in Times:
                timer = [t // 1000 for t in timer]

        for timer in Times:
            timer = [t // iterations for t in timer]

        Radiuses = [i for i in range(rad_beg, rad_beg + step * count, step)]
        plt.figure(figsize=(14, 5))
        plt.title("Зависимость времени выполнения алгоритмов от радиуса окружности")
        plt.ylabel("Время, mcs")
        plt.xlabel("Радиус")
        plt.plot(Radiuses, Times[0], label="Канон. ур-е")
        plt.plot(Radiuses, Times[1], linestyle = '--', label="Парам. ур-е")
        plt.plot(Radiuses, Times[3], linestyle = ':', label="Алг-м Брезенхема")
        plt.plot(Radiuses, Times[2], linestyle = '-.', label="Алг-м средней точки")
        plt.legend()
        plt.show()


    def measure_time_ellipse(self):
        centre = [0, 0]
        rad_beg_x = 50
        rad_beg_y = 100
        step_x = 50
        step_y = 100
        count = 100
        iterations = 5

        Times = [[0] * count for i in range(4)]

        for i in range(iterations):
            cur_rad_x = rad_beg_x
            cur_rad_y = rad_beg_y
            for j in range(count):
                time_start = time.time_ns()
                draw_ellipse_canon(centre, cur_rad_x, cur_rad_y)
                time_end = time.time_ns()
                Times[0][j] += time_end - time_start

                time_start = time.time_ns()
                draw_ellipse_param(centre, cur_rad_x, cur_rad_y)
                time_end = time.time_ns()
                Times[1][j] += time_end - time_start

                time_start = time.time_ns()
                draw_ellipse_bresenham(centre, cur_rad_x, cur_rad_y)
                time_end = time.time_ns()
                Times[2][j] += time_end - time_start

                time_start = time.time_ns()
                draw_ellipse_mid_point(centre, cur_rad_x, cur_rad_y)
                time_end = time.time_ns()
                Times[3][j] += time_end - time_start

                cur_rad_x += step_x
                cur_rad_y += step_y

            for timer in Times:
                timer = [t // 1000 for t in timer]

        for timer in Times:
            timer = [t // iterations for t in timer]

        Radiuses = [i for i in range(rad_beg_y, rad_beg_y + step_y * count, step_y)]
        plt.figure(figsize=(14, 5))
        plt.title("Зависимость времени выполнения алгоритмов от радиусов эллипса (Rx/Ry = 1/2)")
        plt.ylabel("Время, mcs")
        plt.xlabel("Радиус Ry")
        plt.plot(Radiuses, Times[0], label="Канон. ур-е")
        plt.plot(Radiuses, Times[1], linestyle = '--', label="Парам. ур-е")
        plt.plot(Radiuses, Times[3], linestyle = ':', label="Алг-м Брезенхема")
        plt.plot(Radiuses, Times[2], linestyle = '-.', label="Алг-м средней точки")
        plt.legend()
        plt.show()



