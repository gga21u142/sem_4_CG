class Points():

    def __init__(self):
        
        self.dot_D = list()
        self.dots_A = list()


    def is_dot_D(self):
        return True if len(self.dot_D)>0 else False
    
    def change_dot_D(self, Coords):
        if len(self.dot_D) == 0:
            self.dot_D.append(Coords)
        else:
            self.dot_D[0] = Coords
    
    def delete_dot_D(self):
        if len(self.dot_D) == 1:
            self.dot_D.pop()
    

    def add_dot_A(self, Coords):
        self.dots_A.append(Coords)
    
    def delete_dot_A(self, index):
        if len(self.dots_A) >= index + 1:
            self.dots_A.pop(index)
        
    def change_dot_A(self, index, Coords):
        if len(self.dots_A) >= index + 1:
            self.dots_A[index] = Coords

    def count_dots_A(self):
        return int(len(self.dots_A))
    

    def print_all_points(self):
        print("Точка D: " + str(self.dot_D))
        print("Точки A: " + str(self.dots_A))
    
    def clear_all_points(self):
        self.dot_D.clear()
        self.dots_A.clear()
