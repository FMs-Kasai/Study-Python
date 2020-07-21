import random

print("じゃんけん（グー:1 チョキ:2 パー:3）")
user_hand = int(input())
cpu_hand = random.randint(1,3)
result = ""

if user_hand == cpu_hand:
    result = "draw"

if (user_hand == 1 and cpu_hand == 2) or (user_hand == 2 and cpu_hand == 3) or (user_hand == 3 and cpu_hand == 1):
    result = "user-win"

if (user_hand == 2 and cpu_hand == 1) or (user_hand == 3 and cpu_hand == 2) or (user_hand == 1 and cpu_hand == 3):
    result = "user-lose"

print(result)