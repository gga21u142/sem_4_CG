# This Python file uses the following encoding: utf-8


class Points:
    def __init__(self):
        self.points = list()
        self.figures = list()

    def add_point(self, point):
        if len(self.points) == 0:
            self.points.append(point)
            return 0
        elif point != self.points[-1]:
            self.points.append(point)
            return 0
        return -1

    def clear(self):
        self.points.clear()
        self.figures.clear()

    def points_conect(self):
        if (len(self.points) > 2):
            if (self.points[0] != self.points[-1]):
                self.points.append(self.points[0])
            self.figures.append(self.points.copy())
            self.points.clear()
            return 0
        return -1


