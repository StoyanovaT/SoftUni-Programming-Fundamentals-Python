def perfect_number(num):
    divisors = []
    for i in range(1, number):
        if number // i == number / i:
            divisors.append(i)

    if number == sum(divisors):
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


number = int(input())
perfect_number(number)
