def say_hello():
    print("hello")

def say_greeting(greeting):
    print(greeting)

def add(num1,num2):
    return (num1 + num2)

def avg(num1,num2,num3):
    return ((num1 + num2 + num3) / 3)

say_hello()
say_hello()
say_hello()

say_greeting("Hi!")
say_greeting("good morning")

add(5,6) #printがないから実行しても表示されない
print(add(5,6))

avg_result = avg(9,4,2)
print(avg_result)


