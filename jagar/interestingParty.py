

def main(first, second):
    cnt = []
    hobbies = first + second
    for i in range(len(hobbies)):
        cnt.append(hobbies.count(hobbies[i]))
    return max(cnt)


print(main(['fishing', 'gardening', 'swimming', 'fishing'],
           ['hunting', 'fishing', 'fishing', 'biting']
           ))
print(main(["variety", "diversity", "loquacity", "courtesy"],
           ["talking", "speaking", "discussion", "meeting"]))
print(main(["snakes", "programming", "cobra", "monty"],
           ["python", "python", "anaconda", "python"]))
print(main(["t", "o", "p", "c", "o", "d", "e", "r", "s", "i", "n", "g", "l", "e", "r",
            "o", "u", "n", "d", "m", "a", "t", "c", "h", "f", "o", "u", "r", "n", "i"],
           ["n", "e", "f", "o", "u", "r", "j", "a", "n", "u", "a", "r", "y", "t", "w",
            "e", "n", "t", "y", "t", "w", "o", "s", "a", "t", "u", "r", "d", "a", "y"]))
