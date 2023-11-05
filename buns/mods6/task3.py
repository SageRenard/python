def get_generator():
    current_num = 10
    while True:
        temp = current_num
        nums = []
        
        while temp > 0:
            nums.append(temp % 10)
            temp = temp // 10

        sum = 0

        for i in nums:
            sum += i ** len(nums)
        if sum == current_num:
            yield current_num

        current_num += 1



generator = get_generator()


def get_armstrong_numbers():
    return next(generator)


for i in range(8):
    print(get_armstrong_numbers(), end=' ')
