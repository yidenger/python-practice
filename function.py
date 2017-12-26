# def sum(x, y):
#     return x + y

# x = int(input('请输入x: '));
# y = int(input('请输入y: '));

# print('x + y = ', sum(x, y));

def sum(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n
    return sum

print(sum(1, 2, 3, 4))