def two_sum(numbers, target):
    solution = []
    for i, number in enumerate(numbers[:-1]):
        difference_num = target - number
        if difference_num in numbers[i+1:]:
            solution.append(difference_num)
            solution.append(number)
            break
    else:
        print("No solutions exist")
    return solution

numbers = [3, 5, 1, -1, 6]
target_number = 2

print(two_sum(numbers, target_number))
