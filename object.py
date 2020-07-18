class Human():

    def __init__(self,name,sex):
        self.name = name
        self.sex = sex

    def sleep(self):
        print(self.name, "寝る")

    def eat(self):
        print(self.name, "食べる")

class Ryo(Human):

    def __init__(self,name,sex,age):
        super().__init__(name,sex)

        self.age = age

    def study(self):
        print(self.name,"勉強する")

    def go_unv(self):
        print(self.name,"大学に行く")

class Mother(Human):
    def __init__(self,name,sex,jobs):
        super().__init__(name,sex)

        self.jobs = jobs

    def work(self):
        print(self.name,"働く")
        print("職業:",self.jobs)

human = Human("No-name","?")
print("名前:{}  性別:{}".format(human.name,human.sex))

human.eat()
human.sleep()

human2 = Ryo("Ryo","M","21")
human2.sleep()
human2.eat()
human2.study()

human3 = Mother("???","F","health-care-worker")
human3.eat()
human3.work()