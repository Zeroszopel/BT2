class Test:
    def __init__(self, id, name):
        self._id = id
        self._name = name


def SortCri(e):
    return e._id


test1 = Test(2, "a")
test2 = Test(6, "b")
test3 = Test(7, "c")
test4 = Test(3, "d")
list = []
list.append(test1)
list.append(test2)
list.append(test3)
list.append(test4)
list.sort(key=Test._id)
for i in list:
    print(i._id, "   ", i._name)
