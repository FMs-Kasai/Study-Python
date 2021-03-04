def input_min_sens() -> float:
    min_sens = input('センシを入力して下さい(下限：　0.01~1.00)')
    try:
        min_sens = float(min_sens)
    except:
        print('数字で入力してください')
        return input_min_sens()

    if min_sens >= 0.01 and min_sens < 1.00:
        return min_sens
    else:
        print('0.01以上1.00未満で入力してください')
        return input_min_sens()

def input_max_sens(min_sens: float) -> float:

    max_sens = input('センシを入力してください(上限：　{}~1.00)'
                     .format(min_sens)
                     )
    try:
        max_sens = float(max_sens)
    except:
        print('数字で入力してください')
        return input_min_sens()

    if max_sens > min_sens and max_sens <= 1.00:
        return max_sens
    else:
        print('{}より大きい数字かつ1.00以下で入力してください'
              .format(min_sens)
              )
        return input_max_sens(min_sens)

def input_decide_sens_number() -> int:
    decide_sens_number = input()
    try:
        int(decide_sens_number)
    except:
        print('数字の1か2か3で入力してください')
        return input_decide_sens_number()

    if decide_sens_number > 0 and decide_sens_number <= 3:
        return decide_sens_number
    else:
        print('数字の1か2か3で入力してください')
        return input_decide_sens_number()

def decide_sens() -> float:
    min_sens = input_min_sens()
    max_sens = input_max_sens(min_sens)

    optimal_sens = (min_sens + max_sens) / 2
    print('あなたのセンシは{}です。合っていますか？1,2,3で入力してください\n'
          '合っている:1,　速い:2, 遅い:3'
          .format(optimal_sens)
          )
    decide_sens_number = input_decide_sens_number()

decide_sens()