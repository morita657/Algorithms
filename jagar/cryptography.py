def main(numbers):
    numbers.sort()
    numbers[0] = numbers[0] + 1
    calc = 1
    for i in range(len(numbers)):
        calc *= numbers[i]
    return calc


print(main([1, 2, 3]))
print(main([1, 3, 2, 1, 1, 3]))
print(main([1000, 999, 998, 997, 996, 995]))
print(main([1, 1, 1, 1]))
