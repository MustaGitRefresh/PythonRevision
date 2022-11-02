# def bubble_sort(array_in):
#     size = len(array_in)
#     for j in range(size-1):
#         swapped = False
#         for i in range(size - 1 - j):
#             if array_in[i] > array_in[i + 1]:
#                 temporary = array_in[i]
#                 array_in[i] = array_in[i + 1]
#                 array_in[i + 1] = temporary
#                 swapped = True
#         if not swapped:
#             break
#     return array_in


# if __name__ == '__main__':
# array = [3, 4, 19, 30, 35, 9, 34, 37, 18, 47]
# sorted_array = bubble_sort(array)
# print(sorted_array)
# Exercise - Solved
# def bubble_sort(elements_, key=None):
#     """
#     This will take a list or the elements. it will take the key as by which to sort
#     """
#     keys_list = [element.keys() for element in elements_][0]
#     # validating the whether the correct key given by the user
#     validated = False
#     if key in keys_list:
#         validated = True
#     # Now sorting algorithm
#     if validated:
#         for i in range(len(elements_) - 1):
#             for j in range(len(elements_)-1):
#                 if elements_[j][key] > elements_[j + 1][key]:
#                     temporary = elements_[j][key]
#                     elements_[j][key] = elements_[j + 1][key]
#                     elements_[j + 1][key] = temporary
#     else:
#         raise KeyError('Correct key is not given')
#
#     return elements_
#
#
# if __name__ == '__main__':
#     elements = [
#         {'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'},
#         {'name': 'dhaval', 'transaction_amount': 400, 'device': 'google pixel'},
#         {'name': 'kathy', 'transaction_amount': 200, 'device': 'vivo'},
#         {'name': 'aamir', 'transaction_amount': 800, 'device': 'iphone-8'},
#     ]
#     value = bubble_sort(elements, 'name')
#     for k in value:
#         print(k)
