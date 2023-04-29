# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QMessageBox

def show_warn_centre():
    error = QMessageBox()
    error.setWindowTitle("Ошибка!")
    error.setText("Координаты точки центра вышли за пределы отрисовки. Координаты должны попадать в интервал [-5000, 5000]!")
    error.setDefaultButton(QMessageBox.Ok)
    error.setIcon(QMessageBox.Warning)
    error.exec_()

def show_warn_cir_radius():
    error = QMessageBox()
    error.setWindowTitle("Ошибка!")
    error.setText("Радиус окружности не должен быть равен нулю!")
    error.setDefaultButton(QMessageBox.Ok)
    error.setIcon(QMessageBox.Warning)
    error.exec_()

def show_warn_ell_radius():
    error = QMessageBox()
    error.setWindowTitle("Ошибка!")
    error.setText("Радиусы эллипса не должны быть равны нулю!")
    error.setDefaultButton(QMessageBox.Ok)
    error.setIcon(QMessageBox.Warning)
    error.exec_()

def show_warn_ell_spec_step():
    error = QMessageBox()
    error.setWindowTitle("Ошибка!")
    error.setText("Для построения спектра вы должны выбрать шаг радиуса и задать его отличным от нуля!")
    error.setDefaultButton(QMessageBox.Ok)
    error.setIcon(QMessageBox.Warning)
    error.exec_()

def show_warn_ell_spec_settings():
    error = QMessageBox()
    error.setWindowTitle("Ошибка!")
    error.setText("Значения начальных радиусов и кол-ва фигур должны быть больше нуля!")
    error.setDefaultButton(QMessageBox.Ok)
    error.setIcon(QMessageBox.Warning)
    error.exec_()

def show_warn_cir_spec_settings():
    error = QMessageBox()
    error.setWindowTitle("Ошибка!")
    error.setText("Для построения спектра необходимо выбрать 3 параметра и задать их отличными от нуля!")
    error.setDefaultButton(QMessageBox.Ok)
    error.setIcon(QMessageBox.Warning)
    error.exec_()

def show_warn_cir_spec_wrong_set():
    error = QMessageBox()
    error.setWindowTitle("Ошибка!")
    error.setText("Невозможно построить спектр с введенными настройками!")
    error.setDefaultButton(QMessageBox.Ok)
    error.setIcon(QMessageBox.Warning)
    error.exec_()

def show_warn_cant_undo():
    error = QMessageBox()
    error.setWindowTitle("Ошибка!")
    error.setText("Достигнут лимит отмены действий!")
    error.setDefaultButton(QMessageBox.Ok)
    error.setIcon(QMessageBox.Warning)
    error.exec_()
