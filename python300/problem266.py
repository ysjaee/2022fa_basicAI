class Stock:
    def __init__(self, name, code, per, pbr, bpr):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.bpr = bpr

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code