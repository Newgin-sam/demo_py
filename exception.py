def ask_for_int():
    while True:
        try:
            val = int(input("please enter a number : "))
        except:
            print("this is not a number")
            continue
        else:
            print("thanks")
            break
        finally:
            print("this is final \n")

ask_for_int()