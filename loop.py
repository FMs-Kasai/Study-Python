while True:
    print("Who are you?:")
    name = input()
    c = 0

    if name == "Ryo":
        print("Hi Ryo Enter the password")
        password = input()
    else:
        continue

    while password != "bananafish":
        print("Failed")
        c = c + 1

        if c >= 3:
            print("3回間違えたので強制終了します")
            exit()

        print("Enter the password")
        password = input()

    print("passed")
    break




