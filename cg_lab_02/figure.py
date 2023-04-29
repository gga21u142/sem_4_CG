
# Класс для точек программы
from math import cos, sin, radians, pi

class Figure():

    def __init__(self):
        
        self.dots = list()
        self.connections = list()

    def figure_clear(self):
        self.dots.clear()
        self.connections.clear()
    
    def get_dots_count(self):
        return len(self.dots)
    
    def get_connections_count(self):
        return len(self.connections)
    
    def dots_read_from_file(self, dots_count, file):
        for i in range(dots_count):
            try:
                dot_x, dot_y = map(float, file.readline().split())
            except:
                return -1
            self.dots.append([dot_x, dot_y])
        return 0

    def connections_read_from_file(self, connections_count, file):
        dots_count = self.get_dots_count()

        for i in range(connections_count):
            try:
                dot_1, dot_2 = map(int, file.readline().split())
            except:
                return -1

            if dot_1 < dots_count and dot_2 < dots_count:
                self.connections.append((dot_1, dot_2))
            else:
                return -1
            
        return 0
            
    
    def figure_download_from_file(self, src):
        self.figure_clear()

        with open(src, 'r') as file:
            try:
                dots_count = int(file.readline())
            except:
                return -1
            
            if self.dots_read_from_file(dots_count, file) != 0:
                self.figure_clear()
                return -1
            
            try:
                connections_count = int(file.readline())
            except:
                self.figure_clear()
                return -1
            
            if self.connections_read_from_file(connections_count, file) != 0:
                self.figure_clear()
                return -1
        
        return 0
            
    def figure_move(self, move_x, move_y):
        for i in range(self.get_dots_count()):
            self.dots[i][0] += move_x
            self.dots[i][1] += move_y
        return 0
        
    def figure_rotate(self, centre, degree):
        degree_ = radians(degree)
        cos_ = cos(degree_)
        sin_ = sin(degree_)
        for dot in self.dots:
            new_x = centre[0] + (dot[0] - centre[0]) * cos_ + (dot[1] - centre[1]) * sin_
            new_y = centre[1] + (dot[1] - centre[1]) * cos_ - (dot[0] - centre[0]) * sin_
            dot[0], dot[1] = new_x, new_y
        return 0

    def figure_scale(self, centre, coeff_x, coeff_y):
        if coeff_x != 0 and coeff_y != 0:
            for dot in self.dots:
                new_x = centre[0] + coeff_x * (dot[0] - centre[0])
                new_y = centre[1] + coeff_y * (dot[1] - centre[1])
                dot[0], dot[1] = new_x, new_y
            return 0
        return -1
            
            


