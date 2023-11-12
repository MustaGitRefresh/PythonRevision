# def find_place_value(number, digit):
#     place_value = 1
#     result = 0
#
#     while number > 0:
#         current_digit = number % 10
#         if current_digit == digit:
#             result = current_digit * place_value
#             break
#         place_value *= 10
#         number //= 10
#
#     return result
#
#
# class Scary:
#     num = 0
#
#     def __init__(self, num) -> None:
#         self.count = 0
#         self.num = num
#         self.find13()
#         if self.count == 1:
#             print("The number is scary")
#
#     def find13(self):
#         # Find the 13 in the num and return the count
#         num = self.num
#         modulus_division_value = 10
#         result = 0
#         while num > 0:
#             if not result:
#                 # Using // floor division method
#                 current_digit = num // modulus_division_value
#                 if current_digit == 13:
#                     self.count += 1
#                     result = 1
#                     break
#                 else:
#                     modulus_division_value *= 10
#
#             elif not result and not self.count:
#                 # Using % operator
#                 current_digit = num % modulus_division_value
#                 if current_digit == 13 and not current_digit > num:
#                     self.count += 1
#                     result = 1
#                 elif current_digit == num:
#                     continue
#                 else:
#                     modulus_division_value *= 10
#
#             elif result and self.count:
#                 # If process is complete then the loop is broken
#                 break
#
#
#     def checkScary(self):
#         # Check and print whether the num is scary
#         pass
#
#
# scary = Scary(131)
def is_scary_number(number):
    count_13 = 0
    while number > 0:
        last_two_digits = number % 100
        if last_two_digits == 13:
            count_13 += 1
            if count_13 > 1:
                return False
        number //= 10
    return count_13 == 1


# Test the function
test_numbers = [113, 131, 103, 1313, 133, 131313, 13131313]
for num in test_numbers:
    if is_scary_number(num):
        print(f"{num} is a scary number.")
    else:
        print(f"{num} is not a scary number.")
