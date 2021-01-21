print("This program sums the individuals digits of a two-digit number, i.e for 35 the output is 8.")


def sum_value_of_individual_numbers(number):
    num1 = str(number)[0]
    num2 = str(number)[1]
    sum_nums = int(num1) + int(num2)
    print(sum_nums)


number_input = int(input("Type a two-digit number:\n"))
sum_value_of_individual_numbers(number_input)
