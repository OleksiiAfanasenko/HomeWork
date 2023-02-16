def is_power_of_two(number):
    if number == 1:
        return "yes"
    elif number % 2 > 0:
        return "no"
    else:
        return is_power_of_two(number / 2)

res = is_power_of_two(1)
print(res)