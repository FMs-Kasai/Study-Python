class Student:
    def avg(self):
        print((80 + 40) / 2)

class Student2:
    def avg(self,math,english):
        print((math + english) / 2)

class Student3:
    def __init__(self):
        self.name = "No Name"

class Student4:
    def __init__(self,name,weight,height,sex):
        self.name = name
        self.weight = weight
        self.height = height
        self.sex = sex

a001 = Student()
a001.avg()

a002 = Student2()
a002.avg(50,40)

a001.name = "kasai"
print(a001.name)

a002.name = "sato"
print(a002.name)

a003 = Student3()
a004 = Student3()
a003.name = "Kasai"

print(a003.name)
print(a004.name)

a005 = Student4("リヴァイ兵長","60","160","m")
print(a005.name,a005.sex,a005.height,a005.weight)

a006 = Student4("Kasai","","160","m")
print(a006.name,a006.sex,a006.height)