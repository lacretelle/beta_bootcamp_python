class Account(object): 
    ID_COUNT = 0
    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name self.__dict__.update(kwargs)
        if hasattr(self, 'value'):
            self.value = 0
        self.ID_COUNT += 1
    def transfer(self, amount): 
        self.value += amount
