from num2words import num2words


result_rafea = num2words(12.01,
                      to='cardinal', lang='ar', rafea=True)
# num2words(12.22,lang='ar', rafea=False)
print(result_rafea)
# from decimal import Decimal
# print(Decimal(0))
# x = 12.01
# x = int(str(12.20000).split(".")[1])
# print(x)
# y = 10

# print(x % y)
