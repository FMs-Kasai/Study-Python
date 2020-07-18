from time import sleep

def count_up_timer(secs):
    for i in range(secs,-1,-1):
        print(i)
        sleep(1)

    print("時間です")

print("秒数を入力")
target_time = int(input("secs:"))

count_up_timer(target_time)

