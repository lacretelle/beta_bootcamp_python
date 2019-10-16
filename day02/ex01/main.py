def what_are_the_vars(*args, **kwargs):
    count = 0
    obj = {}
    for arg in args:
        s = "var_%d" % count
        obj.update({s : arg})
        count += 1
    for kw in kwargs:
        obj.update({kw : kwargs[kw]})
    return (ObjectC(obj))

class ObjectC(object):
    def __init__(self, object):
        for key, val in object.items():
            setattr(self, key, val)

def doom_printer(obj):
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")

if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
