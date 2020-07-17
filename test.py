class Student:
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex

    def calculate_avg(self,date):
        sum = 0

        for num in date:
            sum += num

        avg = sum / len(date)
        return avg

    def judge(self,avg):

        if(avg >= 60):
            result = "passed"
        else:
            result = "failed"

        return result

st01 = Student("kasai","m")
date = [85,65,70,80,90]
avg = st01.calculate_avg(date)
result = st01.judge(avg)

print(avg)
print(st01.name+" "+st01.sex+" "+result)
