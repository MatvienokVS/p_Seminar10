# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.


# first_num = int(input('первое число: '))
# second_num = int(input('второе число: '))

# c = 0
# for i in range(first_num + second_num):
#    if c:
#       break
#    for j in range(first_num + second_num):
#         if i + j == first_num and i * j == second_num:
#             c = 1
#             print(*sorted([i, j]))
#             break
class NumberFinder:

    def __init__(self):
        self.first_num = 0
        self.second_num = 0

    def get_input(self):
        self.first_num = int(input('первое число: '))
        self.second_num = int(input('второе число: '))

    def find_numbers(self):
        c = 0
        for i in range(self.first_num + self.second_num):
            if c:
                break
            for j in range(self.first_num + self.second_num):
                if i + j == self.first_num and i * j == self.second_num:
                    c = 1
                    print(*sorted([i, j]))
                    break


if __name__ == '__main__':
    nf = NumberFinder()
    nf.get_input()
    nf.find_numbers()
