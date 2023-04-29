class Logging():

    def __init__(self):

        self.max_len = 10
        self.log = list()
    
    def update_log(self, Condition):
        copy = Condition.copy()
        self.log.append(copy)
        if len(self.log) > self.max_len:
            self.log.pop(0)
        print("\nLog list:")
        for i in range(len(self.log)):
            print(self.log[i])
        print("\n")
    
    def undo_log(self):
        if (len(self.log) > 1):
            self.log.pop()
            return self.log[len(self.log) - 1]
        else:
            return []
