class Character():

    def __init__(self,name,age,sex,jobs,):
        self.name = name
        self.age = age
        self.sex = sex 
        self.jobs = jobs
    
    def say(self):
        print("こんにちは")
        pass
    
class Weapon_marchant(Character):
    
    def __init__(self,name,age,sex,jobs,say_content):
        super().__init__(name,age,sex,jobs)

        self.say_content = say_content

    def say(self):
        print("やあ！",self.say_content)


charcter1 = Character("none","none","none","none")
charcter1.say()

charcter2 = Weapon_marchant("bukiya","35","M","weapon_marchant","ここは武器屋だよ")
charcter2.say()