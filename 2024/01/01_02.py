
left_list = []
right_list = []

with open('puzzle_input') as file:
    counter = 0
    for line in file:
        left, right = line.strip().split('   ')
        left_list.append(int(left))
        right_list.append(int(right))


def compare():
    global result
    result = 0

    for number in left_list:
        counter = 0
        for num in right_list:
            if number == num:
                counter += 1

        result += counter * number

        

if __name__ == '__main__':
    compare()
    print(result)


## Copilot answer:
##
# from collections import Counter

# def compare():
#     right_counter = Counter(right_list)
#     return sum(num * right_counter[num] for num in left_list)
