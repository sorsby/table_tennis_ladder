class Printer:

    def __init__(self, string=None):
        self.string = string

    def prnt(self):
        print self.string

    def set_string(self, string):
        self.string = string