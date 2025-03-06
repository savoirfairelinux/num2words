from num2words import num2words
from num2words.lang_AR import Num2Word_AR


result_rafea = num2words(12.01, to='cardinal', lang='ar', rafea=True)
# num2words(12.22,lang='ar', rafea=False)
print(result_rafea)
# from decimal import Decimal
# print(Decimal(0))
# x = 12.01
# x = int(str(12.20000).split(".")[1])
# print(x)
# y = 10

# print(x % y)
num_converter = Num2Word_AR()

# Test decimal conversion in Rafea case
result_rafea_decimal = num_converter.to_currency(12.345, currency='SR', rafea=True)
print(result_rafea_decimal)  # Expected: "اثنا عشر ريالاً وثلاثمائة وخمسة وأربعون هللة"

# Test decimal conversion in Nasb case
result_nasb_decimal = num_converter.to_currency(12.345, currency='SR', rafea=False)
print(result_nasb_decimal)  # Expected: "اثني عشر ريالاً وثلاثمائة وخمسة وأربعون هللة"
