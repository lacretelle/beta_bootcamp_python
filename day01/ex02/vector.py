class Vector:
    def __init__(self, values, length=0):
        try:
            if type(values) is list:
               self.values = values
               self.length = len(values)
            elif len(values) > 1:
                count = 0
                self.length = values[1]
                lst = []
                while count < values[1]:
                    lst.append(float(count))
                    count += 1
                self.values = lst
            else:
                count = 0
                self.length = values
                lst = []
                while count < values:
                    lst.append(float(count))
                    count += 1
                self.values = lst
        except Exception as error:
            print ("Error is "+error)

    def __add__(self, op):
        if type(op) is Vector:
            if op.length == self.length:
                tmp = []
                for i, val in enumerate(op.values):
                    tmp.append(val + self.values[i])
                return (Vector(tmp))
            else:
                print ("Error.")
                exit()
        elif isinstance(op, int) or isinstance(op, float):
            tmp = []
            i = 0
            while i < self.length: 
                tmp.append(self.values[i] + op)
                i += 1
            return (Vector(tmp))
        else:
            print ("Error.")
            exit()
    
    def __sub__(self, op):
        if type(op) is Vector:
            if op.length == self.length:
                tmp = []
                for i, val in enumerate(op.values):
                    tmp.append(self.values[i] - val)
                return (Vector(tmp))
            else:
                print ("Error.")
                exit()
        elif isinstance(op, int) or isinstance(op, float):
            tmp = []
            i = 0
            while i < self.length: 
                tmp.append(self.values[i] - op)
                i += 1
            return (Vector(tmp))
        else:
            print ("Error.")
            exit()
    
    def __div__(self, op):
        if isinstance(op, int) or isinstance(op, float):
            tmp = []
            i = 0
            if op != 0:
                while i < self.length:
                    tmp.append(self.values[i] / op)
                return (Vector(tmp))
            else:
                print ("Error.")
                exit()
        else:
            print ("Error.")
            exit()
    
    def __mul__(self, op):
        if type(op) is Vector:
            if op.length == self.length:
                tmp = []
                for i, val in enumerate(op.values):
                    tmp.append(self.values[i] * val)
                return (Vector(tmp))
            else:
                print ("Error.")
                exit()
        elif isinstance(op, int) or isinstance(op, float):
            print ("enter in int")
            tmp = []
            i = 0
            while i < self.length: 
                tmp.append(self.values[i] * op)
                i += 1
            return (Vector(tmp))
        else:
            print ("Error.")
            exit()

    def __str__(self):
        txt = "(Vector {})".format(self.values)
        return str(txt)
    
    def __repr__(self):
        txt = "(Vector {})".format(self.values)
        return str(txt)
