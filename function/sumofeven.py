# def sum():
#     range1 = int(input('enter the number'))
#     range2 = int(input('enter the number'))
#     sum = 0
#     for i in range(range1, range2 + 1):
#         if i % 2 == 0:
#             sum = sum + i
#     print("sum is=", sum)
# sum()
def sum(range1,range2):
    sum = 0
    for i in range(range1, range2 + 1):
        if i % 2 == 0:
            sum = sum + i
            print("sum is=", sum)
sum(1,10)


