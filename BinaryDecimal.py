# The code which takes decimal and convert it to binary and add them both
class BinSumer:
    def __init__(self):
        self.divisor = 10
        self.sum_answer = 0

    def binSum(self, b):
        if self.isBinary(b):
            self.sum_answer += self.binToDecimal(b)

    def print_result(self):
        print("The answer is {}".format(self.deciToBinary(self.sum_answer)))

    def deciToBinary(self, d):
        decimal_number = d
        if decimal_number == 0:
            return 0
        binary = 0
        base = 1
        while decimal_number > 0:
            remainder = decimal_number % 2
            binary += remainder * base
            base *= 10
            decimal_number //= 2
        return binary

    def binToDecimal(self, b):
        decimal = 0
        binary_number = b
        power = 0
        while binary_number > 0:
            bit = binary_number % self.divisor
            decimal += bit * (2 ** power)

            binary_number //= self.divisor
            power += 1
        return decimal

    def isBinary(self, b):
        binary = False
        while b > 0:
            remainder = b % self.divisor
            if -1 < remainder < 2:
                binary = True
                b //= self.divisor
            else:
                binary = False
            if not binary:
                break
        return binary


binary_arithmetic = BinSumer()
binaries = [11, 11001, 101001, 1100110]
for i in binaries:
    binary_arithmetic.binSum(i)
binary_arithmetic.print_result()

