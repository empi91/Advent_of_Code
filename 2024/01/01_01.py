
left_list = []
right_list = []

with open('puzzle_input') as file:
    counter = 0
    for line in file:
        left, right = line.strip().split('   ')
        left_list.append(left)
        right_list.append(right)


def compare():
    global result
    result = 0
    size = len(left_list)
    left_list.sort()
    right_list.sort()



    for i in range(size):
        l = int(left_list[0])
        r = int(right_list[0])

        if l > r:
            result += l -r
        elif r > l:
            result += r - l

        left_list.pop(0)
        right_list.pop(0)
        

if __name__ == '__main__':
    compare()
    print(result)