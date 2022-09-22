def two_num_sum(numbers, target):
    solution = []
    for i, number in enumerate(numbers[:-1]):
        difference_num = target - number
        if difference_num in numbers[i+1:]:
            solution.append(difference_num)
            solution.append(number)
            break
    else:
        return "No solutions found"

    return solution

numbers = [3, 5, -4 ,8, 11, 1, -1, 6]
target = 10

print(two_num_sum(numbers, target))
