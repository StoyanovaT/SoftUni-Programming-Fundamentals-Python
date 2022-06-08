def loading_bar(percent):
    if number == 100:
        print("100% Complete!")
        print("[%%%%%%%%%%]")
    else:
        number_percent = (number // 10) * "%"
        number_dots = (10 - (number // 10)) * "."
        print(f"{number}% [{number_percent}{number_dots}]")
        print("Still loading...")


number = int(input())
loading_bar(number)