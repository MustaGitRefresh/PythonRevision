# This file code works with the code arrays and learning arrays
# Writing the code
# importing the array module
# import array

def main():
    """
This function deals with the changing and slicing and creation of the arrays.
"""
    # creating the array of the integer
    # a = array.array('i', [5, 6, -7, -8])
    # print("The array elements ar")
    # for element in a:
    #     print(element)
    # creating the array of characters
    # arr = array.array('u', ['a', "b", "c", "d", "e"])
    # for characters in arr:
    #     print(characters)
    # writing the code that will create the same array from the another array
    # arr1 = array.array('d', [1.5, 2.5, -3.5, 4])
    # arr2 = array.array(arr1.typecode, (a*3 for a in arr1))
    # print('The arr2 elements are:')
    # for elements in arr2:
    # 	print(elements)
    # print('The size is arr1: ', sys.getsizeof(arr1))
    # print('The size is arr2: ', sys.getsizeof(arr2))
    # print('The size is arr2[0]: ', sys.getsizeof(arr2[0]))
    # x = array.array('i', [10, 20, 30, 40, 50])
    # n = len(x)
    # # using for loop
    # for i in range(n):
    #     print(x[i], end=' ')
    # # using while loop
    # i = 0
    # print()
    # while i < n:
    #     print(x[i], end=' ')
    #     i += 1
    # Slicing advance
    # y = x[1:4]
    # print(y)
    # y = x[0:]
    # print(y)
    # y = x[:4]
    # print(y)
    # y = x[-4:]
    # print(y)
    # y = x[-4:-1]
    # print(y)
    # y = x[0:7:2]
    # print(y)
    # changing the values
    # x[1:3] = array.array('i', [5, 7])
    # print(x)
    pass


def processor_arrays():
    """
     This function deals with processing with the array
    """
    # array_on_operand = array.array('i', [10, 20, 30, 50, 60, 70, 80, 90, 100])
    # print(original array {array_on_operand}')
    # array_on_operand.append(110)
    # print(f'After appending {array_on_operand}')
    # array_on_operand.insert(2, 33)
    # print(f'After inserting {array_on_operand}')
    # array_on_operand.remove(20)
    # print(f'After removing {array_on_operand}')
    # array_on_operand.pop()
    # print(f'After pop {array_on_operand}')
    # print(f'Getting the index of the element {array_on_operand.index(80)}')
    # print(f'After converting it to list {array_on_operand.tolist()}')
    # making a array with the user input
    # input_str = input("Enter the marks:\n").split(' ')
    # marks = [int(num) for num in input_str]
    # print(type(marks))
    # sums = 0
    # for x in marks:
    #     print(x)
    #     sums += x
    # print(f"The total marks are:{sums}")
    # percent = sums/len(marks)
    # print(f"Percentage:{percent}")
    pass


def array_sort():
    # creating the array
    # array_ = array.array('i', [])
    # print('How many elements:', end='')
    # total_elements = int(input())
    # for i in range(total_elements):
    #     print("Enter the elements ", end='')
    #     array_.append(int(input()))
    # print(f'Original array {array_}')
    # # bubble sort
    # flag = False
    # for i in range(total_elements - 1):
    #     for j in range(total_elements - 1 - i):
    #         print('array_[j], array_[j+1] {} {} '.format(array_[j], array_[j + 1]))
    #         if array_[j] > array_[j + 1]:
    #             t = array_[j]
    #             print(f't {t}')
    #             print('array_[j] , array_[j+1] {} {} '.format(array_[j], array_[j + 1]))
    #             array_[j] = array_[j + 1]
    #             array_[j + 1] = t
    #             flag = True
    #     if not flag:
    #         break
    #     else:
    #         flag = False
    # print(f'Sorted array {array_}')
    pass


def searching_in_array():
    """
    First this function will include the duplicate but other one will not
    """
    # array_search = array.array('i', [])
    # print("How many elements to be there in", end='')
    # n = int(input())
    #
    # # Then append it
    # for i in range(n):
    #     print(f"Element {i + 1}", end='')
    #     array_search.append(int(input()))
    # print(f"Original array {array_search}")
    # # For finding the element
    # print("Enter the element to find", end='')
    # searching_el = int(input())
    # # Algorithm
    # flag = False
    # for i in range(len(array_search)):
    #     if searching_el == array_search[i]:
    #         print(f"Found at position {i + 1}")
    #         break


def with_super_linear_search():
    # """
    #    First this function will include the duplicate but other one will not
    #    """
    # array_search = array.array('i', [])
    # print("How many elements to be there in", end='')
    # n = int(input())
    #
    # # Then append it
    # for i in range(n):
    #     print(f"Element {i + 1}", end='')
    #     array_search.append(int(input()))
    # print(f"Original array {array_search}")
    # # For finding the element
    # print("Enter the element to find", end='')
    # searching_el = int(input())
    # # Algorithm
    # flag = False
    # for i in array_search:
    #     if searching_el == i:
    #         print(f"Found at position {i + 1}")
    #         break
    pass


if __name__ == '__main__':
    # main()
    # processor_arrays()
    # array_sort()
    # start = time.time()
    # searching_in_array()
    # end = time.time()
    # print(f'Time {end-start}')
    # print('New')
    # start1 = time.time()
    # with_super_linear_search()
    # end1 = time.time()
    # times = end-start
    # times1 = end1-start1
    # if times1 > times:
    #     print("times1 is slower")
    # else:
    #     print("First one is faster")

    pass
