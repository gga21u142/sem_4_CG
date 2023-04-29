from copy import *
# Класс для регулирования состояния программы

class Logging():

    def __init__(self):

        self.max_len = 10
        self.log = list()
    
    def get_log_len(self):
        return len(self.log)
    
    def update_log(self, Condition):
        copy = deepcopy(Condition)
        self.log.append(copy)
        if self.get_log_len() > self.max_len:
            self.log.pop(0)
        print("\nLog list:")
        for i in range(self.get_log_len()):
            print(self.log[i][:2])
        print("\n")
    
    def undo_log(self):
        if self.get_log_len() > 1:
            self.log.pop()
            return deepcopy(self.log.pop())
